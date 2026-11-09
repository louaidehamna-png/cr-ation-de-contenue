"""Scène Blender (bpy) : « Mur plein ou mur creux ? » + étagères VASAGLE.

Clip A = frames 1-450 (15 s), clip B = frames 1001-1270 (9 s), 30 fps.
Aucun texte, aucun être vivant.

Usage :
  python3 scene.py --test            # stills 480x854 de contrôle -> out/test/
  python3 scene.py --clip A|B [--res 1080 1920]   # séquence PNG -> out/frames_X/
"""
import bpy, bmesh, math, os, sys, argparse
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
FPS = 30
A0, A1 = 1, 450
B0, B1 = 1001, 1270

# ---------- helpers ----------
def hexrgb(h, a=1.0):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return (*c, a)

def mat(name, color, rough=0.5, metal=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = hexrgb(color) if isinstance(color, str) else color
    b.inputs['Roughness'].default_value = rough
    b.inputs['Metallic'].default_value = metal
    return m

def noisy(m, scale, c1, c2, stretch=(1, 1, 1)):
    nt = m.node_tree; n = nt.nodes; L = nt.links
    tc = n.new('ShaderNodeTexCoord'); mp = n.new('ShaderNodeMapping')
    mp.inputs['Scale'].default_value = stretch
    nz = n.new('ShaderNodeTexNoise'); nz.inputs['Scale'].default_value = scale
    nz.inputs['Detail'].default_value = 8
    cr = n.new('ShaderNodeValToRGB')
    cr.color_ramp.elements[0].color = hexrgb(c1); cr.color_ramp.elements[1].color = hexrgb(c2)
    L.new(tc.outputs['Object'], mp.inputs['Vector']); L.new(mp.outputs['Vector'], nz.inputs['Vector'])
    L.new(nz.outputs['Fac'], cr.inputs['Fac'])
    L.new(cr.outputs['Color'], n['Principled BSDF'].inputs['Base Color'])
    return m

def wood_mat():
    m = mat('Bois', '#5a3d28', 0.65)
    img = os.path.join(HERE, 'assets', 'detail-support.png')
    nt = m.node_tree
    if os.path.exists(img):
        t = nt.nodes.new('ShaderNodeTexImage'); t.image = bpy.data.images.load(img)
        t.projection = 'BOX'; t.projection_blend = 0.2
        tc = nt.nodes.new('ShaderNodeTexCoord'); mp = nt.nodes.new('ShaderNodeMapping')
        mp.inputs['Scale'].default_value = (2.5, 2.5, 2.5)
        nt.links.new(tc.outputs['Object'], mp.inputs['Vector']); nt.links.new(mp.outputs['Vector'], t.inputs['Vector'])
        nt.links.new(t.outputs['Color'], nt.nodes['Principled BSDF'].inputs['Base Color'])
    else:  # veinage procédural marron vintage (placeholder)
        noisy(m, 2.5, '#5a3618', '#a06a38', stretch=(1.2, 30, 30))
        cr = [n for n in m.node_tree.nodes if n.type == 'VALTORGB'][0]
        e = cr.color_ramp.elements.new(0.35); e.color = hexrgb('#3a2312')
        e = cr.color_ramp.elements.new(0.6); e.color = hexrgb('#8a5a2c')
    return m

def emission_ring_mat(name, color='#3A2F2A'):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; n = nt.nodes; n.clear()
    out = n.new('ShaderNodeOutputMaterial'); mix = n.new('ShaderNodeMixShader')
    tr = n.new('ShaderNodeBsdfTransparent'); em = n.new('ShaderNodeEmission')
    em.inputs['Color'].default_value = hexrgb(color); em.inputs['Strength'].default_value = 1.0
    nt.links.new(tr.outputs[0], mix.inputs[1]); nt.links.new(em.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs[0])
    mix.inputs[0].default_value = 0.0
    if hasattr(m, 'surface_render_method'): m.surface_render_method = 'BLENDED'
    return m, mix.inputs[0]

def box(name, size, loc, material=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object; o.name = name; o.scale = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if material: o.data.materials.append(material)
    return o

def bevel(o, w=0.002, seg=2):
    md = o.modifiers.new('bev', 'BEVEL'); md.width = w; md.segments = seg

def cyl(name, r, depth, loc, rot=(math.pi / 2, 0, 0), material=None, verts=32):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=depth, location=loc, rotation=rot)
    o = bpy.context.object; o.name = name
    if material: o.data.materials.append(material)
    return o

def key(o, path, frame, value, idx=-1):
    if idx < 0: setattr(o, path, value)
    else: getattr(o, path)[idx] = value
    o.keyframe_insert(path, frame=frame)

def keysock(sock, frame, value):
    sock.default_value = value; sock.keyframe_insert('default_value', frame=frame)

def look_at(cam, target):
    d = Vector(target) - cam.location
    cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

def camera(name, loc, target, lens=50, focus=None, fstop=5.6):
    c = bpy.data.cameras.new(name); c.lens = lens
    if focus is not None:
        c.dof.use_dof = True; c.dof.focus_distance = focus; c.dof.aperture_fstop = fstop
    o = bpy.data.objects.new(name, c); bpy.context.collection.objects.link(o)
    o.location = loc; look_at(o, target); return o

def set_top_material(o, m):
    o.data.materials.append(m); idx = len(o.data.materials) - 1
    for p in o.data.polygons:
        if p.normal.z > 0.9: p.material_index = idx

# ---------- scène ----------
def build():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.fps = FPS
    sc.frame_start, sc.frame_end = A0, B1

    world = bpy.data.worlds.new('W'); sc.world = world; world.use_nodes = True
    bg = world.node_tree.nodes['Background']
    bg.inputs['Color'].default_value = hexrgb('#2C2420'); bg.inputs['Strength'].default_value = 0.6

    M = {
        'mur': noisy(mat('Mur', '#E9DFCF', 0.92), 60, '#E4D8C6', '#EEE5D7'),
        'acier': noisy(mat('Acier noir mat', '#151515', 0.6, 0.6), 400, '#101010', '#1d1d1d'),
        'trou': mat('Trou', '#050505', 1.0),
        'bois': wood_mat(),
        'beton': noisy(mat('Beton', '#7a736a', 0.95), 25, '#5f5952', '#8e877c'),
        'platre': mat('Plaque de platre', '#F2EFE8', 0.9),
        'montant': mat('Montant metal', '#8A8D90', 0.4, 0.9),
        'cheville': mat('Cheville', '#D8D8D4', 0.45),
        'fond': mat('Fond sombre', '#2C2420', 1.0),
        'livre': mat('Livre', '#3A2F2A', 0.8),
        'pages': mat('Pages', '#EDE6D6', 0.9),
        'vase': mat('Vase ceramique', '#CFC6B6', 0.35),
    }

    # --- mur principal (plein cadre) ---
    box('Mur', (4, 0.1, 3.2), (0, 0.05, 1.6), M['mur'])
    box('Sol', (4, 2, 0.02), (0, -1, -0.01), mat('Sol', '#6b5340', 0.7))

    # --- étagères : (longueur, x centre, z de l'axe du bras horizontal) ---
    T = 0.018      # épaisseur plateau : non communiquée, prise fine, jamais cotée
    D = 0.12       # profondeur
    H = 0.11       # hauteur
    LEG = 0.0015   # demi-épaisseur de la bande acier
    shelves = [(0.30, 0.06, 1.50, 'Haut'), (0.35, 0.035, 1.23, 'Milieu'), (0.40, 0.0, 0.96, 'Bas')]  # ordre infographie
    rig = []
    for si, (Lg, x, z, nm) in enumerate(shelves):
        pz = z + LEG + T / 2
        p = box(f'Plateau_{nm}', (Lg, D, T), (x, -D / 2, pz), M['bois']); bevel(p, 0.002, 3)
        brs = []
        for side in (-1, 1):
            br = make_bracket(f'Support_{nm}_{side}', D + 0.004, H, M['acier'])
            br.location = (x + side * (Lg / 2 - 0.035), 0, z)
            br.rotation_euler = (0, math.pi, 0)   # montage « supports vers le bas »
            brs.append((br, side, Lg, x))
        rig.append((p, brs, z, pz))

    # Clip A, 10-15 s : supports qui glissent vers le mur, puis plateaux qui se posent dessus
    for si, (p, brs, z, pz) in enumerate(rig):
        f0 = 301 + si * 12
        for br, side, Lg, x in brs:
            br.scale = (0, 0, 0); br.keyframe_insert('scale', frame=A0); br.keyframe_insert('scale', frame=f0 - 1)
            key(br, 'location', A0, -0.45, 1); key(br, 'location', f0, -0.45, 1)
            key(br, 'scale', f0, (1, 1, 1)); key(br, 'location', f0 + 30, 0.0, 1)
        f1 = 366 + si * 10
        p.scale = (0, 0, 0); p.keyframe_insert('scale', frame=A0); p.keyframe_insert('scale', frame=f1 - 1)
        key(p, 'location', A0, pz + 0.3, 2); key(p, 'location', f1, pz + 0.3, 2)
        key(p, 'scale', f1, (1, 1, 1)); key(p, 'location', f1 + 26, pz, 2)

    # Clip B : retournement « bas -> haut ». Chaque support glisse hors du plateau,
    # pivote vers l'extérieur, puis revient : le plateau passe dans le triangle.
    for p, brs, z, pz in rig:
        for br, side, Lg, x in brs:
            x_in = x + side * (Lg / 2 - 0.035); x_out = x + side * (Lg / 2 + 0.025)
            key(br, 'location', B0 + 8, x_in, 0); key(br, 'location', B0 + 22, x_out, 0)
            key(br, 'rotation_euler', B0 + 22, math.pi, 1)
            key(br, 'rotation_euler', B0 + 52, math.pi - side * math.pi, 1)
            key(br, 'location', B0 + 52, x_out, 0); key(br, 'location', B0 + 68, x_in, 0)
    p, brs, z, pz = rig[0]

    # Livre + vase (non inclus) sur l'étagère du haut, apparaissent ~3,6 s dans le clip B
    zt = pz + T / 2
    book = box('Livre', (0.03, 0.11, 0.17), (-0.02, -0.062, zt + 0.085), M['livre']); bevel(book, 0.003)
    pages = box('Pages', (0.026, 0.104, 0.162), (-0.02, -0.0585, zt + 0.085), M['pages'])
    vase = make_vase('Vase', M['vase']); vase.location = (0.08, -0.06, zt)
    for i, o in enumerate((book, pages, vase)):
        f = B0 + 84 + (0 if o is not vase else 8)
        o.scale = (0, 0, 0); o.keyframe_insert('scale', frame=A0); o.keyframe_insert('scale', frame=f)
        key(o, 'scale', f + 12, (1, 1, 1))

    # --- onde d'intro (0-3,5 s) sur le mur principal ---
    for i in range(3):
        ring(f'Onde_intro_{i}', (0.02, -0.003, 1.28), 12 + i * 22, 50, 0.32, 0.9)

    # --- coupe du mur (3,5-10 s), décor séparé à x=20 ---
    build_cut(M)

    # --- lumières ---
    key_l = bpy.data.lights.new('Cle', 'AREA'); key_l.energy = 260; key_l.size = 1.2
    key_l.color = (1.0, 0.82, 0.62)
    o = bpy.data.objects.new('Cle', key_l); sc.collection.objects.link(o)
    o.location = (-1.7, -1.4, 2.3); look_at(o, (0.0, 0, 1.25))
    fill = bpy.data.lights.new('Fill', 'AREA'); fill.energy = 60; fill.size = 2.0; fill.color = (1.0, 0.93, 0.85)
    o = bpy.data.objects.new('Fill', fill); sc.collection.objects.link(o)
    o.location = (1.6, -2.2, 1.4); look_at(o, (0.0, 0, 1.25))
    cut_l = bpy.data.lights.new('CleCoupe', 'AREA'); cut_l.energy = 220; cut_l.size = 1.0; cut_l.color = (1.0, 0.84, 0.66)
    o = bpy.data.objects.new('CleCoupe', cut_l); sc.collection.objects.link(o)
    o.location = (19.2, -1.0, 2.0); look_at(o, (20, 0.05, 0.8))

    # --- caméras + découpage ---
    camA = camera('Cam_Mur', (0.6, -1.95, 1.5), (0.03, 0, 1.27), 50, focus=2.05, fstop=8)
    camCut = camera('Cam_Coupe', (20.0, -0.72, 1.36), (20.0, 0.07, 0.6), 30, focus=1.05, fstop=8)
    camB = camera('Cam_B', (0.42, -0.72, 1.70), (0.10, -0.04, 1.56), 32, focus=0.75, fstop=4)
    # Clip B : plan serré (0-5 s) puis recul vers le plan d'ensemble (5-9 s)
    key(camB, 'location', B0 + 140, camB.location.copy())
    rot_close = camB.rotation_euler.copy(); camB.keyframe_insert('rotation_euler', frame=B0 + 140)
    camB.location = (0.6, -2.05, 1.5); look_at(camB, (0.03, 0, 1.27))
    camB.keyframe_insert('location', frame=B0 + 175); camB.keyframe_insert('rotation_euler', frame=B0 + 175)
    key(camB, 'location', B1, Vector((0.5, -1.65, 1.45)))
    camB.data.dof.focus_distance = 0.75; camB.data.dof.keyframe_insert('focus_distance', frame=B0 + 140)
    camB.data.dof.focus_distance = 2.1; camB.data.dof.keyframe_insert('focus_distance', frame=B0 + 175)

    for f, c in ((A0, camA), (106, camCut), (301, camA), (B0, camB)):
        mk = sc.timeline_markers.new(f'cam{f}', frame=f); mk.camera = c
    sc.camera = camA

    # rendu
    sc.render.engine = 'BLENDER_EEVEE'
    ee = sc.eevee
    for attr, val in (('use_shadows', True), ('taa_render_samples', 32), ('use_raytracing', False)):
        if hasattr(ee, attr): setattr(ee, attr, val)
    sc.view_settings.view_transform = 'AgX'
    sc.render.image_settings.file_format = 'PNG'
    return sc

def fillet_loop(pts, r, n=8):
    """Polygone fermé (y,z) -> contour à coins arrondis de rayon r."""
    out = []
    N = len(pts)
    for i in range(N):
        p0, p1, p2 = Vector(pts[i - 1]), Vector(pts[i]), Vector(pts[(i + 1) % N])
        a, b = (p0 - p1).normalized(), (p2 - p1).normalized()
        ang = math.acos(max(-1, min(1, a.dot(b))))
        t = r / math.tan(ang / 2)
        s0, s1 = p1 + a * t, p1 + b * t
        bis = (a + b).normalized(); c = p1 + bis * (r / math.sin(ang / 2))
        v0, v1 = s0 - c, s1 - c
        a0, a1 = math.atan2(v0.y, v0.x), math.atan2(v1.y, v1.x)
        da = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
        for k in range(n + 1):
            th = a0 + da * k / n
            out.append((c.x + r * math.cos(th), c.y + r * math.sin(th)))
    return out

def make_bracket(name, depth, height, m):
    """Triangle fermé en bande d'acier (photos fiche) : plaque murale, bras horizontal sous le plateau,
    diagonale, coins arrondis. Origine = axe du bras horizontal, contre le mur.
    rotation y = 0 -> triangle au-dessus du plateau ; rotation y = pi -> triangle en dessous."""
    W, Tk = 0.022, 0.003
    h = Tk / 2
    loop = fillet_loop([(-h, h), (-h, height - h), (-depth + h, h)], 0.012)
    loop = loop[::-1]
    me = bpy.data.meshes.new(name); bm = bmesh.new()
    vin, vout = [], []
    for y, z in loop:
        # contour moyen ; épaisseur via solidify
        vin.append(bm.verts.new((-W / 2, y, z - h))); vout.append(bm.verts.new((W / 2, y, z - h)))
    N = len(loop)
    for i in range(N):
        j = (i + 1) % N
        try: bm.faces.new((vin[i], vin[j], vout[j], vout[i]))
        except ValueError: pass
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
    bm.to_mesh(me); bm.free()
    o = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(o)
    sd = o.modifiers.new('ep', 'SOLIDIFY'); sd.thickness = Tk; sd.offset = 0
    o.data.materials.append(m)
    # trous en serrure sur la plaque murale (simples pastilles sombres)
    for k, zz in enumerate((height * 0.45, height * 0.78)):
        hole = cyl(f'{name}_trou{k}', 0.0035, 0.0005, (0, -Tk - 0.0002, zz - h), material=bpy.data.materials['Trou'], verts=16)
        hole.parent = o; hole.location = (0, -Tk - 0.0002, zz - h)
    return o

def make_vase(name, m):
    prof = [(0.0, 0.0), (0.035, 0.0), (0.045, 0.03), (0.046, 0.07), (0.03, 0.11), (0.018, 0.13), (0.02, 0.15), (0.0, 0.15)]
    me = bpy.data.meshes.new(name); bm = bmesh.new()
    seg = 48; rings = []
    for r, zz in prof:
        rings.append([bm.verts.new((r * math.cos(2 * math.pi * k / seg), r * math.sin(2 * math.pi * k / seg), zz)) for k in range(seg)])
    for a, b in zip(rings, rings[1:]):
        for k in range(seg):
            try: bm.faces.new((a[k], a[(k + 1) % seg], b[(k + 1) % seg], b[k]))
            except ValueError: pass
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me); bm.free()
    for p in me.polygons: p.use_smooth = True
    o = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(o); o.data.materials.append(m)
    return o

def ring(name, loc, f_start, dur, r_end, alpha, thick=0.008):
    bpy.ops.mesh.primitive_torus_add(major_radius=1, minor_radius=thick, major_segments=96, minor_segments=8,
                                     location=loc, rotation=(math.pi / 2, 0, 0))
    o = bpy.context.object; o.name = name
    m, fac = emission_ring_mat(name + '_mat'); o.data.materials.append(m)
    o.scale = (0.01, 0.01, 1); o.keyframe_insert('scale', frame=A0); o.keyframe_insert('scale', frame=f_start)
    key(o, 'scale', f_start + dur, (r_end, r_end, 1))
    keysock(fac, A0, 0.0); keysock(fac, f_start, 0.0); keysock(fac, f_start + 3, alpha)
    keysock(fac, f_start + dur, 0.0)
    for fc in o.animation_data.action.fcurves if o.animation_data.action and hasattr(o.animation_data.action, 'fcurves') else []:
        for kp in fc.keyframe_points: kp.interpolation = 'SINE'; kp.easing = 'EASE_OUT'
    return o

def build_cut(M):
    X = 20.0; H = 0.3; z0 = 0.4; zc = z0 + H / 2; top = z0 + H
    # fond sombre
    box('Fond_coupe', (6, 0.05, 4), (X, 1.2, 1.5), M['fond'])
    box('Socle_coupe', (6, 3, 0.02), (X, 0.0, z0 - 0.01), M['fond'])
    # gauche : mur plein (béton/brique), 20 cm
    left = box('Mur_plein', (0.27, 0.2, H), (X - 0.155, 0.1, zc), M['mur']); set_top_material(left, M['beton'])
    # droite : cloison, 2 plaques de plâtre + vide + montant
    pf = box('Plaque_avant', (0.27, 0.013, H), (X + 0.155, 0.0065, zc), M['mur']); set_top_material(pf, M['platre'])
    pb = box('Plaque_arriere', (0.27, 0.013, H), (X + 0.155, 0.0935, zc), M['platre'])
    box('Cavite_fond', (0.27, 0.074, 0.01), (X + 0.155, 0.05, z0 + 0.005), M['fond'])
    box('Montant', (0.04, 0.074, 0.002), (X + 0.265, 0.05, top - 0.002), M['montant'])
    box('Montant_aile', (0.002, 0.074, H), (X + 0.285, 0.05, zc), M['montant'])
    # impacts + ondes : gauche courte et sourde, droite qui résonne
    zi = top - 0.12
    ring('Onde_g', (X - 0.155, -0.003, zi), 140, 14, 0.06, 1.0, 0.004)
    for i in range(4):
        ring(f'Onde_d_{i}', (X + 0.155, -0.003, zi), 214 + i * 9, 34, 0.12, 0.95 - i * 0.18, 0.004)
    # chevilles (agrandies pour la lisibilité), axe au niveau de la coupe
    zc_ = top
    g = cyl('Cheville_expansion', 0.016, 0.11, (X - 0.155, 0.045, zc_), material=M['cheville'])
    for k in range(4):
        rib = cyl(f'Cheville_exp_rib{k}', 0.019, 0.007, (X - 0.155, 0.02 + k * 0.02, zc_), material=M['cheville']); rib.parent = g
        rib.location = (0, 0, 0.03 - k * 0.025) ; rib.rotation_euler = (0, 0, 0)
    d = cyl('Cheville_placo', 0.012, 0.06, (X + 0.155, 0.02, zc_), material=M['cheville'])
    wings = []
    for s in (-1, 1):
        w = box(f'Cheville_placo_aile{s}', (0.005, 0.035, 0.014), (0, 0, 0), M['cheville']); w.parent = d
        w.location = (s * 0.014, 0.0, -0.015); wings.append(w)
    for o, f, y_end in ((g, 195, 0.045), (d, 264, 0.02)):
        o.scale = (0, 0, 0); o.keyframe_insert('scale', frame=A0); o.keyframe_insert('scale', frame=f - 1)
        key(o, 'scale', f, (1, 1, 1))
        key(o, 'location', f, y_end - 0.16, 1); key(o, 'location', f + 18, y_end, 1)
    for w in wings:
        w.rotation_euler = (0, 0, 0); w.keyframe_insert('rotation_euler', frame=278)
        key(w, 'rotation_euler', 292, (0, 0, math.copysign(1.2, w.location.x)))

def render_frames(sc, frames, res, outdir, prefix=''):
    os.makedirs(outdir, exist_ok=True)
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 100
    for f in frames:
        sc.frame_set(f)
        sc.render.filepath = os.path.join(outdir, f'{prefix}{f:04d}.png')
        bpy.ops.render.render(write_still=True)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--test', action='store_true')
    ap.add_argument('--clip', choices=['A', 'B'])
    ap.add_argument('--res', nargs=2, type=int, default=[1080, 1920])
    ap.add_argument('--frames', default='')
    ap.add_argument('--save', action='store_true')
    a = ap.parse_args()
    sc = build()
    if a.save: bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, 'out', 'scene.blend'))
    if a.test:
        fr = [int(x) for x in a.frames.split(',')] if a.frames else [60, 165, 240, 290, 340, 440, B0 + 30, B0 + 60, B0 + 135, B1 - 5]
        render_frames(sc, fr, (480, 854), os.path.join(HERE, 'out', 'test'))
    elif a.clip:
        lo, hi = (A0, A1) if a.clip == 'A' else (B0, B1)
        fr = [int(x) for x in a.frames.split(',')] if a.frames else range(lo, hi + 1)
        render_frames(sc, fr, tuple(a.res), os.path.join(HERE, 'out', f'frames_{a.clip}'))
