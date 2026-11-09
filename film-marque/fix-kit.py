"""Rend les fonctions du décor commun (em*) visibles depuis le script de chaque séquence, et corrige emPen
(autoRound: false, sinon les traits de crayon sautent au lieu de se dessiner). Idempotent : à relancer après
toute réécriture d'une séquence."""
import re, glob
for f in sorted(glob.glob('compositions/frames/*.html')):
    s = open(f, encoding='utf-8').read(); o = s
    m = re.search(r'(<script[^>]*id="s\d\d-em-kit-js"[^>]*>)(.*?)(</script>)', s, re.S)
    if m:
        body = m.group(2)
        body = re.sub(r'\n?/\* em-expose \*/.*?/\* /em-expose \*/\n?', '\n', body, flags=re.S)
        names = sorted(set(re.findall(r'function (em\w+)\s*\(', body)))
        expo = '\n/* em-expose */ Object.assign(window, {' + ', '.join(names) + '}); /* /em-expose */\n'
        s = s[:m.start(2)] + body.rstrip() + expo + s[m.end(2):]
    s = s.replace('{strokeDashoffset:0,duration:dur||0.4,ease:"power2.out"}', '{strokeDashoffset:0,duration:dur||0.4,ease:"power2.out",autoRound:false}')
    if s != o:
        open(f, 'w', encoding='utf-8').write(s); print('corrigé', f, '(kit)' if m else '(pas de bloc kit)')
    else:
        print('inchangé', f, '' if m else '(pas de bloc kit trouvé)')
