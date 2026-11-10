---
version: 1
name: "Étagères Murales · Film B « Trois onglets »"
description: >
  Charte du film de marque d'Étagères Murales (45 s, 1080×1920 vertical, 30 i/s), version A du script « Le mur vide ».
  Un seul lieu : LE MUR, un grand mur d'enduit beige au-dessus d'un canapé en lin, à côté d'une commode. La caméra le
  parcourt. Un objet porte toute l'histoire : LE TÉLÉPHONE, qui sort d'un croquis au crayon sur le mur (séquence 3),
  montre une fiche produit floue (séquences 4 et 5), s'éteint au noir pour le pivot (séquence 6), se rallume sur la vraie
  fiche d'Étagères Murales (séquences 7 et 8), puis rend l'étagère au mur du début, qui n'est plus vide (séquence 9).
  Charte de la boutique : crème, brun, brun foncé, sable du logo, police Inter. Pas de musique imposée ici (étape 5).
unit: 1080×1920
principle: "un mur, un téléphone, une idée par image, la caméra bouge toujours, du neuf toutes les 0,5 s, chaque transition passe par un objet"
reference: "reference/mur.html (code commun exécutable : polices, couleurs, caméra du mur, mur et ses stations, commode et objets, canapé, croquis au crayon, téléphone et ses deux fiches, sous-titre mot à mot, boîte, trait, coche, curseur ; source UNIQUE, à recopier à l'identique)"

colors:
  canvas: "#2c2420"          # brun foncé : le pivot (séquence 6) et la carte de fin (séquence 9)
  wall: "#e9dfcf"            # LE mur (enduit beige), dégradé doux vers #ddd0bc dans les coins
  wall-shade: "#d6c8b2"      # ombres portées sur le mur
  paper: "#f5f0e8"           # crème : fonds de cartes, écran de la vraie fiche
  card: "#fffdf9"            # cartes et pages web
  ink: "#2c2420"             # texte sur clair
  ink-soft: "rgba(44,36,32,.55)"
  ink-on-dark: "#f5f0e8"
  brown: "#3a2f2a"           # brun : boutons, téléphone, traits forts
  accent: "#a97c50"          # sable profond : SEULEMENT la boîte du mot clé, les traits sous les mots-pics, les coches de la vraie fiche
  accent-light: "#c8a27c"    # sable du logo : halo, point de lumière, carte de fin
  pencil: "#7d7268"          # graphite : croquis au crayon sur le mur
  wrong: "#8c3b2e"           # brique sourde : SEULEMENT les annotations « faux / ? » de la fiche floue (séquences 4 et 5)

fonts:
  Inter: { files: ["assets/fonts/Inter-Regular.otf (400)", "assets/fonts/Inter-Medium.otf (500)", "assets/fonts/Inter-SemiBold.otf (600)"] }

typography:
  subtitle:  { fontFamily: "Inter", px: 60, weight: 600, lineHeight: 72, tracking: "-0.015em", note: "la phrase de la voix, EN BAS AU CENTRE, dans la bande réservée y 1360 à 1520 (classe .em-sub), 2 lignes au plus, 26 caractères par ligne environ, mot par mot : chaque mot arrive à 35 % d'opacité puis passe plein en 0,2 s. Sur le clair : #2c2420 avec un léger halo crème ; sur le sombre : #f5f0e8 (.em-sub.dark). Une seule phrase à la fois." }
  type:      { fontFamily: "Inter", px: 84, weight: 600, lineHeight: 1.1, tracking: "-0.025em", note: "UN moment typographique : le pivot (séquence 6), la phrase centrée EST l'image ; pas de sous-titre en bas pendant ce moment" }
  ui:        { fontFamily: "Inter", px: 30, weight: 500, note: "texte des pages web dans le téléphone (à l'échelle écran du téléphone 1:1)" }
  ui-title:  { fontFamily: "Inter", px: 40, weight: 600 }
  note:      { fontFamily: "Inter", px: 34, weight: 600, note: "annotations reliées (« bois ? », « charge : ? », « inclus ? ») et étiquettes" }
  pencil:    { fontFamily: "Inter", px: 44, weight: 500, note: "écriture au crayon sur le mur (« 6 mois »), couleur pencil, légère rotation -3°" }

world:
  summary: >
    Le mur est un plan de 4000 × 5000 u (1 u = 1 px à l'échelle 1). Caméra 2D emCam(x, y, s) : le point (x, y) du mur au
    centre de l'image (540, 960), à l'échelle s. Le mur a sa texture d'enduit (bruit fixe) et une ombre douce en vignette :
    elle rend la dérive visible.
  stations:
    mur-nu:   "centre (1500, 1500) : la grande zone vide au-dessus du canapé ; repères au crayon autour de (1500, 1450) ; « 6 mois » écrit au crayon en (1120, 1180)"
    canape:   "dossier du canapé en lin (#cfc3b0 → #bfb29e), de x 820 à 2180, haut du dossier en y 2050, assise jusqu'à y 2500 ; deux coussins"
    commode:  "commode en chêne clair (#c9a77c), de x 2500 à 3300, plateau en y 2200 ; la pile d'objets posée dessus (livres, vase, cadre, bougie) autour de x 2900"
    croquis:  "trois croquis d'étagères au crayon sur le mur au-dessus du canapé : (1150, 1500), (1500, 1380), (1850, 1500), chacun 300 × 40 u avec deux équerres"
    etageres: "à la fin, la vraie photo détourée des 3 étagères VASAGLE posée sur le mur nu, centrée en (1500, 1450), largeur 900 u"
  framings:
    F-large:   "emCam(1500, 1700, 0.42) : tout le mur, le canapé en bas"
    F-mur:     "emCam(1500, 1450, 0.75) : le mur nu au-dessus du canapé"
    F-commode: "emCam(2900, 2050, 1.10) : la pile d'objets sur la commode"
    F-croquis: "emCam(1500, 1460, 0.95) : les trois croquis"
  phone:
    summary: >
      LE téléphone : un smartphone générique sans marque, coque #3a2f2a, rayon 64, 640 × 1300 px à l'échelle 1, écran
      590 × 1250 rayon 52, îlot de caméra en haut. En gros plan il est en couche écran (pas dans le mur). Cadrage de référence PH : centre (540, 772), échelle
      0,85 (haut 220, bas 1325 : la bande des sous-titres reste libre). Son écran affiche une page web à l'échelle
      1:1 (texte ui 28 à 38 px). Écran éteint = calque .off #2c2420 (le brun du pivot).
    page-floue: "fiche d'une boutique anonyme (aucun nom de marque, aucune adresse) : barre d'adresse « …/etagere-murale-bois » ; photo dessinée d'une étagère avec deux vases ; titre « Étagère murale en bois » ; prix « 39,90 € » ; lignes « Matière : bois », « Charge : – », « Dimensions : voir photo »."
    page-em:    "VRAIE fiche d'Étagères Murales : barre d'adresse « etageres-murales.fr » ; photo assets/img/vasagle-3-etageres.png ; titre « Étagères murales flottantes lot de 3 VASAGLE » ; « 49,90 € » ; lignes avec coche sable : « Matière : panneau de particules, effet bois vintage », « Dimensions : 30, 35 et 40 cm, profondeur 12 cm », « Dans le colis : 3 étagères, accessoires de montage et clé Allen, notice en français », « Les objets des photos ne sont pas inclus » ; puis la carte FAQ d'une autre vraie fiche : « Étagère d'angle de douche en inox 304 », question « Quelle charge peut-elle porter ? », réponse « Le vendeur ne l'a pas encore communiquée. Nous lui avons posé la question. »"

components:
  key-box:  "le mot clé de chaque phrase : rectangle accent #a97c50, angles presque nets (rayon 4), qui déborde de 0,14 em ; le texte passe en #f5f0e8. Se trace de gauche à droite (scaleX 0 → 1, 0,16 s power3.out), 0 à 2 images avant le mot."
  peak-stroke: "trait fin accent de 5 px, arrondi, sous LE mot-pic ; se dessine de gauche à droite (scaleX 0 → 1, 0,35 s power2.out) pendant le mot. 3 pics dans le film : « vide » (séq. 1), « vraiment » (séq. 7), « dit » (séq. 8)."
  annotation: "annotation reliée à un élément de la fiche floue : cercle ou rature au trait brique #8c3b2e 4 px qui se dessine (stroke-dashoffset), relié par un trait fin à une étiquette note sur carte blanche."
  check:    "coche de la vraie fiche : disque accent 40 px, coche crème qui se dessine en 0,2 s ; la ligne cochée passe d'ink-soft à ink."
  cursor:   "flèche blanche à contour brun, ombre ; arrive d'UN seul mouvement en courbe (0,45 s power3.out) et clique directement (échelle 0,85 en 0,06 s + onde accent)."
  arrival:  "toute apparition : trop grande (×1,1 à ×1,3) et floue (8 px) → nette à sa taille en 0,16 à 0,2 s expo.out. Sorties plus rapides que les entrées."

negative:
  - "Jamais de sous-titre ailleurs qu'en bas au centre ; la bande y 1360 à 1520 ne porte que la phrase."
  - "Rien d'important au-dessus de y 200 ni sous y 1600 (interface des réseaux), ni à droite de x 960 entre y 900 et 1600 (boutons des réseaux)."
  - "Aucun être vivant à l'image (ni personne, ni main, ni animal, ni plante)."
  - "La fiche floue n'imite aucune boutique réelle : aucun nom de marque, aucun logo, aucune adresse réelle."
  - "Aucun chiffre ni texte hors du script, des lignes Scene et des fiches décrites ici. Pas de superlatif, pas d'emoji, pas de tiret cadratin."
  - "Accent sable seulement pour la boîte du mot clé, les 3 traits-pics, les coches de la vraie fiche, le point de lumière et la carte de fin."
  - "Pas d'easing élastique ni back.out ; pas de boucle infinie ; aucune image figée : la caméra dérive toujours."
  - "Typographie française : espace insécable avant « : », espace fine insécable avant « ? », apostrophe ’, guillemets « »."

fabrication:
  - "BLOQUANT. Canevas 1080 × 1920, 30 i/s ; la racine de chaque séquence porte data-width=\"1080\" data-height=\"1920\"."
  - "BLOQUANT. Tout <template id> interne est À L'INTÉRIEUR de <div id=\"root\"> et son id porte le préfixe de la séquence."
  - "BLOQUANT. Jamais style.visibility = \"visible\" : toujours \"inherit\"."
  - "BLOQUANT. Tout élément absent à t = 0 part de opacity: 0 en CSS ; immediateRender: false sur tout fromTo placé après t = 0."
  - "BLOQUANT. Transforms seulement (x, y, scale, rotation, opacity, filter) ; jamais top, left, width, height ni letterSpacing."
  - "BLOQUANT. Pas de backdrop-filter ; pas de clip-path polygon interpolé (circle, ellipse, inset permis)."
  - "BLOQUANT. Tous les ids commencent par une lettre et portent le préfixe de la séquence (s01- à s09-)."
  - "BLOQUANT. Le décor (mur, canapé, commode, croquis, téléphone, fiches) vient de reference/mur.html, recopié à l'identique."
