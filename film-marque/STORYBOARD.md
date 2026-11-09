---
format: 1080x1920
duration: "45.00s"
message: "Chez Étagères Murales, chaque fiche dit ce que vous recevez vraiment : on ose enfin habiller le mur vide."
arc: Hook → Silence → Problem → Pivot → Solution → Proof → CTA
audience: "Particuliers qui veulent habiller un mur ou ranger une pièce et qui hésitent à acheter une étagère en ligne"
mode: autonomous
captions: disabled
music: "pre-mixed with voice and SFX in assets/audio/mix.wav (mounted at root by the orchestrator)"
direction: "A « Le mur vide » (script A de SCRIPT.md), choisie par l'utilisateur ; monde unique : le mur, objet fil : le téléphone"
styleframes: "reference/mur.html (aperçus ?v=mur, commode, croquis, floue, em, faq, fin)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

# Storyboard · « Le mur vide » (45 s, 1080×1920)

> **Minutage provisoire.** La voix n'est pas encore enregistrée : les temps des mots ci-dessous sont estimés à 170 mots
> par minute avec les pauses du texte ElevenLabs (SCRIPT.md, version A). Quand `assets/audio/voix.mp3` existera, on
> recalera chaque `Word cues` sur `onsets.json` (method.md § 4) ; les séquences sont construites pour supporter un
> décalage de ± 0,3 s (chaque mot, boîte et trait est posé sur son cue, jamais sur une durée fixe).

## Video direction

- **Un seul monde** : LE MUR (frame.md, `reference/mur.html`) : enduit beige au-dessus d'un canapé en lin, une commode à
  droite. Acte clair du problème (séquences 1 à 5, sur le mur puis dans le téléphone), pivot sur le brun foncé
  (séquence 6), acte clair de la solution (séquences 7 et 8, la vraie fiche dans le téléphone), retour au mur puis carte
  de fin brune (séquence 9). Chaque séquence peint son propre fond sur un calque `class="clip"` de toute sa durée.
- **Coutures invisibles** : toutes les séquences s'enchaînent en `cut` ; chaque couture tombe au sommet du flou d'un
  geste de caméra ou d'un objet, et le `handoff_out` de N est recopié mot pour mot dans le `handoff_in` de N+1. Aucune
  coupe franche, aucun fondu : les transitions passent toutes par un objet (règle d'or 3).
- **Les 3 règles d'or** (CLAUDE.md) : la caméra bouge tout le temps (dérive chiffrée dans chaque plan + crans datés) ;
  du neuf toutes les 0,5 s (chaque plan liste ses étapes, jamais plus de 0,6 s sans événement) ; les transitions passent
  par un objet (le crayon, la pile, le croquis, le téléphone, l'écran éteint, le point de lumière, la photo).
- **Texte** : la phrase de la voix en sous-titre en bas au centre (`emSub`, 60 px, bande y 1360 à 1520 réservée, 2
  lignes au plus), mot par mot sur ses cues ; un mot clé par phrase dans la boîte sable [boîte : …] ; 3 mots-pics
  soulignés d'un trait sable [trait : …] (« vide. », « vraiment. », « dit. ») ; UN moment typographique (le pivot, 84 px
  centré). Aucun autre texte que celui des lignes Scene, du mur (« 6 mois ») et des pages du téléphone (frame.md).
- **Une seule chose à regarder** : la caméra isole le sujet de chaque phrase ; zoom franc dans un seul sens, jamais
  d'aller-retour ; rien d'important au-dessus de y 200, sous y 1600, ni à droite de x 960 entre y 900 et 1600.
- **Vraies interfaces** : la vraie fiche d'Étagères Murales (VASAGLE, photo réelle `assets/img/vasagle-3-etageres.png`,
  textes de la fiche Shopify) et la vraie FAQ de l'étagère d'angle de douche ; la fiche floue est volontairement
  anonyme (aucune marque).
- **Grammaire de mouvement** : deux vitesses (gestes de 0,15 à 0,5 s en expo.out ou power3.inOut, dérives linéaires
  permanentes) ; toute apparition arrive trop grande (×1,1 à ×1,3) et floue (8 px) puis se pose en 0,16 à 0,2 s ;
  sorties plus rapides que les entrées ; aucune tenue figée.
- **Négatifs** : diaporama (tout à t = 0), écran de veille (tout qui flotte sans but), objet dédoublé, être vivant
  (personne, main, animal, plante), texte inventé, chiffre hors fiche.

**MONDE**
- Acte 1 (0.00 à 20.40) : le mur, stations mur-nu (1500, 1500), commode (2900, 2050), croquis (1150/1500/1850, 1500) ;
  puis le téléphone en couche écran sur le mur flou (fiche floue). Fond : enduit beige texturé (la dérive se lit dans le
  grain).
- Pivot (20.40 à 24.40) : brun foncé #2c2420, la phrase seule, puis un point de lumière sable.
- Acte 2 (24.40 à 37.00) : le téléphone allumé sur la vraie fiche, devant le mur flou.
- Fin (37.00 à 45.00) : le mur nu du début, les 3 vraies étagères posées dessus, puis la carte de fin brune.
- Couleurs de rôle : accent sable #a97c50 = ce qui compte (boîte, 3 traits, coches de la vraie fiche, point de lumière,
  carte de fin) ; brique #8c3b2e = le faux et le flou de la fiche anonyme (annotations, séquences 4 et 5 seulement) ;
  graphite #7d7268 = le crayon (le projet qui n'ose pas).

**SIGNATURES**
- Mécanisme 1 « le crayon » : 0.05 (traits « 6 mois »), 2.70 (repères), 9.80 (trois croquis), 37.60 (les traits
  s'effacent quand les étagères arrivent).
- Mécanisme 2 « l'annotation reliée » : 13.00 (« bois »), 15.50 (« charge »), 18.50 (« vases »). Rime inversée :
  les coches sable de la vraie fiche à 28.80, 29.80, 31.20, 32.70.
- Mécanisme 3 « la plongée dans l'objet » : 11.60 (dans le croquis → téléphone), 19.60 (dans l'écran → noir), 23.40
  (dans le point → lumière), 36.40 (la photo sort du téléphone → le mur).
- Registres de texte : sous-titre mot à mot = monte de 10 px à 35 % puis plein ; boîte = se trace de gauche à droite ;
  trait = se dessine sous le mot ; moment typographique = mots qui tombent de la caméra (×1,2, flou 8 → net).
- Rimes : le mur nu du début (0 à 5,4 s) revient à 37 s, cette fois avec les étagères ; le « 6 mois » au crayon
  s'efface.

**PARTITION CAMÉRA** (temps globaux) : 0.00 très gros plan « 6 mois » cam(1250, 1180, 1.60) · 2.30 recul vers le mur
nu cam(1500, 1450, 0.75) · 3.50 descente sur le canapé cam(1500, 1700, 0.50) · 4.90 cran droite vers la commode ·
5.75 arrivée F-commode cam(2900, 2050, 1.10) · 7.40 whip gauche · 8.30 F-mur cam(1500, 1480, 0.62) · 10.80 poussée
vers les croquis · 11.60 plongée dans le croquis du milieu (×3, flou) · 12.20 téléphone PH · 12.50 à 14.40 cran vers
la ligne « Matière » · 14.70 cran vers « Charge » · 16.70 cran vers la photo · 19.60 plongée dans l'écran (noir) ·
20.40 à 24.00 pivot : dérive lente · 24.40 recul hors de l'écran allumé · 28.40 à 32.80 crans de ligne en ligne ·
33.10 glissement vers la FAQ · 36.40 recul : le téléphone rapetisse vers le mur · 37.00 F-fin cam(1500, 1650, 0.55) ·
41.60 iris vers la carte de fin · 42.30 à 45.00 dérive lente sur la carte.

**VOIX** (provisoire, à recaler sur `onsets.json`) ; silences de plus de 0,4 s, chacun écrit comme un plan :
5.40 à 8.00 (temps muet : la pile sur la commode) · 22.80 à 24.40 (pivot : le point de lumière) · 35.90 à 37.30 (la
photo rejoint le mur) · 42.80 à 45.00 (le clic, la tenue).

**COUPES** : aucune coupe franche, aucun fondu (toutes les coutures par objet ou par caméra).

**RYTHME** : accroche, un événement toutes les 0,1 à 0,3 s ; problème, 4 plans / 10 s ; solution, 3 plans / 10 s plus
un événement de fiche toutes les 0,5 s.

**SON** (temps globaux, calé sur les gestes) : crayon 0.05, 0.20, 0.35 (traits), 2.70 · whoosh-short 4.90, 7.40,
11.60 · pop 6.10, 6.60, 7.00 (objets qui se posent) · pop 13.00, 15.50, 18.50 (annotations) · whoosh 19.60 (écran
qui s'éteint) · impact grave 20.40 · ping 28.80, 29.80, 31.20, 32.70 (coches) · whoosh 36.40 · pop 37.60 (étagères
posées) · whoosh 41.60 (iris) · click 43.40 · notification (signature) 37.70.

---

## Frame 1 : Le mur vide · 0.00 → 5.40

- scene: Très gros plan sur le mur : des traits au crayon comptent les mois et « 6 mois » s'écrit ; la caméra recule sur le grand mur nu marqué de repères au crayon, descend jusqu'au canapé, puis part en cran vers la droite, vers la commode
- duration: 5.40s
- transition_in: cut
- status: animated
- src: compositions/frames/01-mur-vide.html
- voiceover: "Six mois que vous avez emménagé. Et le mur au-dessus du canapé… est toujours vide."
- type: hook
- blueprint: camera-journey (Adapt)
- focal: le « 6 mois » au crayon, puis le grand mur nu au-dessus du canapé
- rules: svg-path-draw, depth-of-field-blur
- world: light
- handoff_in: aucun (ouverture du film) ; première image = mur beige en très gros plan cam(1250, 1180, 1.60), aucun trait de crayon encore dessiné, sous-titre vide
- handoff_out: à 5.40 : cam(2300, 1950, 0.70) flou 6 px ; caméra en plein cran vers la droite (base x qui avance de +3000 u/s, power3.inOut entamé à 4.90) ; dérive 0 ; mur avec « 6 mois », les traits et les repères au crayon dessinés ; canapé à gauche ; commode entrant par la droite avec sur son plateau SEULEMENT les livres et la bougie (pas de vase, pas de cadre) ; aucun téléphone ; sous-titre « Et le mur au-dessus du canapé… est toujours vide. » sorti à 5.30 (rien en bas) ; grain du mur fixe

Word cues: Six@0.30 mois@0.52 que@0.86 vous@0.98 avez@1.16 emménagé.@1.36 Et@2.40 le@2.52 mur@2.64 au-dessus@2.92 du@3.38 canapé…@3.52 est@4.30 toujours@4.48 vide.@4.86

Scene 1 (0.00 à 2.30 s) : P1, « 6 mois » s'écrit au crayon
  TEXTE ÉCRAN : sous-titre « Six mois que vous avez emménagé. » mot par mot sur ses cues, [boîte : mois] ; sort à 2.10 ; écart synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.05 premier trait du compte (emPen sur la partie tally, 0,12 s) ; 0.20 deuxième ; 0.35 troisième ; 0.50 quatrième ; 0.62 cinquième ; 0.76 la barre en travers ; 0.30 « 6 mois » (W.months) arrive trop grand ×1,2 flou 8 → net en 0,2 s ; 1.10 sixième trait (le sixième mois) ; 1.40 les repères au crayon commencent à se tracer (W.marks, 0,9 s) ; 1.90 le compte entier s'éclaircit légèrement (opacité 1 → 0,8).
  PISTE CAMÉRA : dérive x +40 u/s, y +12 u/s, échelle -0,03/s de 0.00 à 2.30 ; aucun cran.
  COUCHES ET PROFONDEUR : avant-plan aucun ; sujet le crayon net ; fond le mur et son grain (la dérive se lit dans le grain) ; pic 2 couches (le plan est un très gros plan).
  OBJET-PONT ET VECTEUR : les traits au crayon restent sur le mur jusqu'à la séquence 9 (ils s'effacent à 37.60).
  SON : crayon à 0.05, 0.20, 0.35, 1.10.
  IMAGE CLÉ : 0.80 : « 6 mois » net au crayon, cinq traits barrés, mur beige en très gros plan.

Scene 2 (2.30 à 4.90 s) : P2, le mur nu au-dessus du canapé
  TEXTE ÉCRAN : sous-titre « Et le mur au-dessus du canapé… est toujours vide. » mot par mot, [trait : vide.] (le trait se dessine à 4.91) ; écart synchro ; reste jusqu'à 5.30 puis sort.
  IMAGE DE DÉPART : le « 6 mois » en gros plan, la caméra commence son recul.
  ÉTAPES : 2.30 recul (voir caméra) ; 2.70 les quatre coins des repères au crayon finissent de se tracer ; 3.10 la croix centrale des repères se trace (0,25 s) ; 3.50 la caméra plonge vers le bas et le dossier du canapé entre par le bas ; 3.90 les coussins se posent d'un léger tassement (y +6 → 0, 0,2 s) ; 4.30 le mur nu est cadré entier (repères au centre, canapé en bas) ; 4.86 « vide. » : les repères pâlissent d'un coup (opacité 1 → 0,55, 0,15 s) ; 4.90 départ du cran à droite.
  PISTE CAMÉRA : 2.30 à 3.20 recul expo.out vers cam(1500, 1450, 0.75) ; 3.40 à 4.30 descente power3.inOut vers cam(1500, 1700, 0.50) ; dérive pendant tout le plan x +20 u/s, échelle -0,01/s ; 4.90 à 5.40 cran à droite power3.inOut vers cam(2900, 2050, 1.10) avec flou max 6 px (emCamTo blurPeak 6, durée 0,85 : il n'est qu'à mi-course à 5.40).
  COUCHES ET PROFONDEUR : avant-plan le dossier du canapé flou 4 px quand il entre ; sujet le mur nu et ses repères ; fond le grain ; pic 3 couches à 4.30.
  OBJET-PONT ET VECTEUR : vecteur : cran vers la droite (power3.inOut), repris tel quel au début de la séquence 2 ; la commode et sa pile deviennent le sujet.
  SON : crayon à 2.70 ; whoosh-short à 4.90.
  IMAGE CLÉ : 4.88 : le grand mur nu, les repères pâles au crayon, le canapé en bas, « … est toujours vide. » avec le trait sable sous « vide. ».

## Frame 2 : Le temps muet · 5.40 → 8.00

- scene: Sans voix : la caméra arrive sur la commode où les objets qui n'ont pas de place s'empilent un à un, la pile penche, puis la caméra repart en whip vers la gauche, vers le mur
- duration: 2.60s
- transition_in: cut
- status: animated
- src: compositions/frames/02-pile.html
- voiceover: ""
- type: pain_point
- blueprint: camera-journey (Adapt)
- focal: la pile d'objets sur la commode
- rules: depth-scatter-assemble
- world: light
- handoff_in: à 0.00 : cam(2300, 1950, 0.70) flou 6 px ; caméra en plein cran vers la droite (base x qui avance de +3000 u/s, power3.inOut entamé à 4.90) ; dérive 0 ; mur avec « 6 mois », les traits et les repères au crayon dessinés ; canapé à gauche ; commode entrant par la droite avec sur son plateau SEULEMENT les livres et la bougie (pas de vase, pas de cadre) ; aucun téléphone ; sous-titre « Et le mur au-dessus du canapé… est toujours vide. » sorti à 5.30 (rien en bas) ; grain du mur fixe
- handoff_out: à 2.60 : cam(2350, 1800, 0.85) flou 10 px ; caméra en plein whip vers la gauche (base x qui recule de -4000 u/s, power3.inOut entamé à 2.00) ; dérive 0 ; commode à droite avec la pile complète (livres, bougie, vase, cadre) penchée de -4° ; mur avec le crayon ; aucun téléphone ; aucun texte ; grain du mur fixe

Word cues: (aucun mot : silence)

Scene 1 (0.00 à 2.00 s) : P3, la pile monte
  TEXTE ÉCRAN : aucun texte (temps muet, l'image seule raconte).
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.35 la caméra finit son cran et se pose sur la commode ; 0.70 le vase tombe de la caméra (trop grand ×1,3, flou 8) et se pose sur les livres (0,2 s, expo.out) ; 1.20 le cadre arrive de la même façon, appuyé contre le vase ; 1.60 un livre de plus glisse sur le haut de la pile (x +40 → 0) ; 1.80 la pile penche (rotation 0 → -4°, origine bas, 0,25 s power2.out), le cadre bascule de 2° ; 2.00 départ du whip.
  PISTE CAMÉRA : 0.00 à 0.35 fin du cran vers cam(2900, 2050, 1.10) (la séquence 1 a lancé un emCamTo de 0,85 s : rejouer sa fin à l'identique en partant de l'état du handoff_in) ; dérive 0.35 à 2.00 x -15 u/s, échelle +0,03/s (lente poussée sur la pile) ; 2.00 à 2.60 whip gauche power3.inOut vers cam(1500, 1480, 0.62) avec flou max 10 px (emCamTo blurPeak 10, durée 0,9 : il n'est qu'à mi-course à 2.60).
  COUCHES ET PROFONDEUR : avant-plan le bord du plateau de la commode, flou 3 px, coupé par le bas ; sujet la pile nette ; fond le mur et son grain ; pic 3 couches.
  OBJET-PONT ET VECTEUR : vecteur : whip à gauche repris au début de la séquence 3 ; la pile reste sur la commode hors champ jusqu'à la fin.
  SON : pop à 0.70, 1.20, 1.60 (objets qui se posent) ; whoosh-short à 2.00.
  IMAGE CLÉ : 1.85 : la pile complète qui penche sur la commode, le mur nu derrière.

## Frame 3 : On n'ose pas choisir · 8.00 → 12.20

- scene: Le whip finit sur le grand mur nu (toute cette place) ; trois croquis d'étagère au crayon se tracent, un point d'interrogation sur chacun ; la caméra plonge dans le croquis du milieu, qui devient le téléphone
- duration: 4.20s
- transition_in: cut
- status: animated
- src: compositions/frames/03-croquis.html
- voiceover: "Le problème, ce n'est pas la place. C'est qu'on n'ose pas choisir."
- type: pain_point
- blueprint: camera-journey (Adapt)
- focal: le mur nu entier, puis les trois croquis, puis le croquis du milieu
- rules: svg-path-draw, scale-swap-transition
- world: light
- handoff_in: à 0.00 : cam(2350, 1800, 0.85) flou 10 px ; caméra en plein whip vers la gauche (base x qui recule de -4000 u/s, power3.inOut entamé à 2.00) ; dérive 0 ; commode à droite avec la pile complète (livres, bougie, vase, cadre) penchée de -4° ; mur avec le crayon ; aucun téléphone ; aucun texte ; grain du mur fixe
- handoff_out: à 4.20 : mur flou 12 px en cam(1500, 1380, 3.00) ; caméra au bout de sa plongée (expo.out presque fini) ; téléphone en couche écran au centre (540, 772), échelle 0,85, net, rotation 0, écran allumé sur la fiche floue (haut de page : barre « …/etagere-murale-bois » et photo) ; aucune annotation ; aucun texte en bas

Word cues: Le@0.10 problème,@0.24 ce@0.80 n'est@0.94 pas@1.14 la@1.34 place.@1.46 C'est@2.30 qu'on@2.50 n'ose@2.70 pas@2.98 choisir.@3.18

Scene 1 (0.00 à 2.00 s) : P4, toute cette place
  TEXTE ÉCRAN : sous-titre « Le problème, ce n'est pas la place. » mot par mot, [boîte : place.] ; sort à 1.95 ; écart synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.40 le whip se termine sur le mur nu entier (repères pâles, canapé en bas) ; 0.50 les repères au crayon s'allongent : les quatre coins glissent vers l'extérieur (scale 1 → 1,25 depuis le centre des repères, 0,4 s power2.out), pour dire « toute cette place » ; 1.00 « 6 mois » s'estompe (opacité → 0,5) ; 1.46 « place. » : les coins finissent leur course ; 1.70 la caméra commence sa poussée vers le centre du mur.
  PISTE CAMÉRA : 0.00 à 0.40 fin du whip vers cam(1500, 1480, 0.62) (la séquence 2 a lancé un emCamTo de 0,9 s : rejouer sa fin à l'identique) ; dérive 0.40 à 2.00 y -20 u/s, échelle +0,02/s ; 1.70 à 2.30 poussée expo.out vers cam(1500, 1460, 0.95) (F-croquis).
  COUCHES ET PROFONDEUR : avant-plan le dossier du canapé flou 4 px en bas ; sujet le mur nu et ses repères ; fond le grain ; pic 3 couches.
  OBJET-PONT ET VECTEUR : les repères laissent la place aux croquis (ils pâlissent à 2.30).
  SON : aucun bruitage nouveau (fin du whoosh précédent).
  IMAGE CLÉ : 1.50 : le mur nu immense, les repères au crayon ouverts, « Le problème, ce n'est pas la place. » avec « place. » en boîte.

Scene 2 (2.00 à 4.20 s) : P5, trois croquis qui hésitent, puis la plongée
  TEXTE ÉCRAN : sous-titre « C'est qu'on n'ose pas choisir. » mot par mot, [boîte : choisir.] ; sort à 3.95 ; écart synchro.
  IMAGE DE DÉPART : les repères pâles au centre du mur, cadrage F-croquis en approche.
  ÉTAPES : 2.30 les repères pâlissent (→ 0,25) ; 2.40 croquis gauche se trace (emPen 0,3 s) ; 2.70 croquis du milieu ; 3.00 croquis droit ; 2.60, 2.90, 3.20 un « ? » apparaît au-dessus de chacun (trop grand ×1,3, flou 8 → net, 0,18 s) ; 3.30 les trois « ? » oscillent une fois (rotation ±4°, 0,3 s) ; 3.45 les croquis gauche et droit pâlissent (→ 0,35) ; 3.55 la caméra plonge dans le croquis du milieu ; 3.75 sous le flou, le téléphone arrive de la caméra (échelle 1,6 → 0,85, flou 14 → 0, rotation -6° → 0, 0,45 s expo.out) en couche écran, écran déjà allumé sur la fiche floue ; 4.05 la page du téléphone glisse de 20 px vers le haut (elle se charge).
  PISTE CAMÉRA : 2.30 à 3.50 dérive x +10 u/s, échelle +0,04/s ; 3.55 à 4.30 plongée expo.out vers cam(1500, 1380, 3.00) avec flou du mur 0 → 12 px (le mur reste flou derrière le téléphone).
  COUCHES ET PROFONDEUR : avant-plan le téléphone qui arrive (flou puis net) ; sujet le croquis du milieu puis le téléphone ; fond le mur flou ; pic 3 couches à 3.80.
  OBJET-PONT ET VECTEUR : le croquis du milieu devient le téléphone (la plongée dans le croquis passe le relais au téléphone qui sort de la caméra) ; le téléphone reste à l'écran jusqu'à la séquence 9.
  SON : crayon à 2.40, 2.70, 3.00 ; whoosh-short à 3.55.
  IMAGE CLÉ : 3.30 : trois croquis d'étagère au crayon, un « ? » sur chacun, « … n'ose pas choisir. » avec « choisir. » en boîte.

## Frame 4 : « Bois »… aggloméré · 12.20 → 15.20

- scene: Dans le téléphone, la fiche d'une boutique anonyme ; la caméra cadre la ligne « Matière : bois » ; un cercle brique entoure « bois », une étiquette « bois ? » s'y relie, puis le mot est barré et l'étiquette devient « aggloméré »
- duration: 3.00s
- transition_in: cut
- status: animated
- src: compositions/frames/04-bois.html
- voiceover: "Une fiche dit « bois »… c'est de l'aggloméré."
- type: pain_point
- blueprint: device-surface-showcase (Adapt)
- focal: la ligne « Matière : bois » de la fiche floue
- rules: svg-path-draw, coordinate-target-zoom
- world: light
- handoff_in: à 0.00 : mur flou 12 px en cam(1500, 1380, 3.00) ; caméra au bout de sa plongée (expo.out presque fini) ; téléphone en couche écran au centre (540, 772), échelle 0,85, net, rotation 0, écran allumé sur la fiche floue (haut de page : barre « …/etagere-murale-bois » et photo) ; aucune annotation ; aucun texte en bas
- handoff_out: à 3.00 : mur flou 12 px en cam(1500, 1380, 3.00) avec dérive y -15 u/s ; téléphone en plein cran vers le haut (power3.inOut entamé à 2.60) qui amène la ligne « Charge : – » vers y 700 de l'écran, échelle du téléphone 1,15 ; ligne « Matière : bois » encore visible en haut avec « bois » barré brique et l'étiquette « aggloméré » ; aucun texte en bas (sous-titre sorti à 2.85)

Word cues: Une@0.10 fiche@0.26 dit@0.56 « bois »…@0.76 c'est@1.60 de@1.78 l'aggloméré.@1.90

Scene 1 (0.00 à 3.00 s) : P6, la matière annoncée
  TEXTE ÉCRAN : sous-titre « Une fiche dit « bois »… c'est de l'aggloméré. » mot par mot, [boîte : l'aggloméré.] ; sort à 2.85 ; dans le téléphone, la fiche floue (frame.md) ; annotations « bois ? » puis « aggloméré » (frame.md, composant annotation).
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.10 la page défile jusqu'au titre (page y -60 px, 0,3 s power3.out) ; 0.30 cran du téléphone vers la ligne r1 (voir caméra) ; 0.70 la ligne « Matière : bois » passe en encre pleine ; 0.80 un cercle brique se dessine autour de « bois » (0,25 s) ; 1.05 l'étiquette « bois ? » arrive à droite de la ligne, reliée par un trait fin (×1,2 flou 8 → net, 0,18 s), restant à gauche de x 960 ; 1.60 « bois » est barré d'un trait brique (0,2 s) ; 1.95 le texte de l'étiquette bascule de « bois ? » à « aggloméré » (rotationX ou sortie y -10 / entrée y +10, 0,2 s) ; 2.30 l'étiquette donne un petit coup (scale 1 → 1,06 → 1, 0,2 s) ; 2.60 départ du cran vers la ligne « Charge ».
  PISTE CAMÉRA : le téléphone est la caméra : 0.30 à 0.80 cran power3.inOut, échelle 0,85 → 1,15 et translation pour amener la ligne r1 à y 720 de l'écran (calculer sur le DOM) ; dérive 0.80 à 2.60 échelle +0,02/s, y -6 px/s ; 2.60 à 3.20 cran vers le haut vers la ligne r2 (power3.inOut, il n'est qu'aux deux tiers à 3.00) ; mur derrière : dérive y -15 u/s, flou 12 px constant.
  COUCHES ET PROFONDEUR : avant-plan l'étiquette d'annotation (elle déborde un peu du téléphone) ; sujet la ligne « Matière » nette ; fond le mur flou ; pic 3 couches.
  OBJET-PONT ET VECTEUR : vecteur : cran du téléphone vers le haut repris au début de la séquence 5 ; le téléphone continue.
  SON : pop à 1.05 (étiquette) ; crayon (trait sec) à 1.60.
  IMAGE CLÉ : 2.10 : « Matière : bois » avec « bois » entouré et barré en brique, étiquette « aggloméré » reliée, sous-titre « … c'est de l'aggloméré. » en boîte.

## Frame 5 : Charge introuvable, vases fournis · 15.20 → 20.40

- scene: La ligne « Charge : – » est entourée, l'étiquette dit « ? » ; le téléphone remonte à la photo, les deux vases sont entourés avec l'étiquette « inclus ? » ; la caméra plonge dans l'écran, qui s'éteint au brun
- duration: 5.20s
- transition_in: cut
- status: animated
- src: compositions/frames/05-charge-vases.html
- voiceover: "La charge ? Introuvable. Et sur la photo, les vases ont l'air fournis."
- type: pain_point
- blueprint: device-surface-showcase (Adapt)
- focal: la ligne « Charge : – », puis les deux vases de la photo
- rules: svg-path-draw, coordinate-target-zoom
- world: light
- handoff_in: à 0.00 : mur flou 12 px en cam(1500, 1380, 3.00) avec dérive y -15 u/s ; téléphone en plein cran vers le haut (power3.inOut entamé à 2.60) qui amène la ligne « Charge : – » vers y 700 de l'écran, échelle du téléphone 1,15 ; ligne « Matière : bois » encore visible en haut avec « bois » barré brique et l'étiquette « aggloméré » ; aucun texte en bas (sous-titre sorti à 2.85)
- handoff_out: à 5.20 : écran plein cadre entièrement éteint (calque .off du téléphone, brun #2c2420, opacité 1) ; téléphone à l'échelle 3,4 centré sur les vases, son cadre hors de l'image ; mur hors de l'image ; aucune annotation visible ; aucun texte

Word cues: La@0.10 charge@0.24 ?@0.24 Introuvable.@0.90 Et@2.10 sur@2.22 la@2.38 photo,@2.50 les@3.10 vases@3.24 ont@3.66 l'air@3.80 fournis.@4.00

Scene 1 (0.00 à 1.60 s) : P7, la charge
  TEXTE ÉCRAN : sous-titre « La charge ? Introuvable. » mot par mot (« charge ? » en un seul mot), [boîte : Introuvable.] ; sort à 1.60 ; annotation « ? ».
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.40 le téléphone finit son cran sur « Charge : – » ; 0.30 un cercle brique se dessine autour du tiret (0,25 s) ; 0.55 étiquette « ? » reliée (×1,2 flou 8 → net) ; 0.90 « Introuvable. » : l'étiquette tremble deux fois (x ±4 px, 0,2 s) ; 1.20 la ligne « Dimensions : voir photo » reçoit un trait ondulé brique dessous (0,25 s) ; 1.40 départ du cran vers la photo.
  PISTE CAMÉRA : fin du cran du téléphone (séquence 4 : rejouer sa fin à l'identique) ; dérive 0.40 à 1.40 échelle +0,02/s ; 1.40 à 2.10 cran power3.inOut vers la photo (le téléphone redescend : la photo vient au centre, échelle 1,15 → 1,30) ; mur : dérive y -15 u/s, flou 12.
  COUCHES ET PROFONDEUR : avant-plan l'étiquette « ? » ; sujet la ligne « Charge » ; fond le mur flou.
  OBJET-PONT ET VECTEUR : le trait ondulé sous « voir photo » envoie le regard vers la photo (le cran suit sa direction).
  SON : pop à 0.55 ; crayon à 1.20.
  IMAGE CLÉ : 1.00 : « Charge : – » entouré, étiquette « ? », sous-titre « Introuvable. » en boîte.

Scene 2 (1.60 à 5.20 s) : P8, les vases de la photo, puis l'écran s'éteint
  TEXTE ÉCRAN : sous-titre « Et sur la photo, les vases ont l'air fournis. » mot par mot, [boîte : fournis.] ; sort à 4.70 ; annotation « inclus ? ».
  IMAGE DE DÉPART : la photo de la fiche floue arrive au centre.
  ÉTAPES : 2.10 la photo est cadrée ; 2.50 « photo, » : un flash blanc très bref sur la photo (opacité d'un calque blanc 0 → 0,35 → 0, 0,2 s) ; 3.00 les deux vases sont entourés d'un même trait brique (0,3 s) ; 3.30 « vases » : les vases montent de 6 px (ils se détachent) ; 3.60 étiquette « inclus ? » reliée, à gauche de x 960 ; 4.00 « fournis. » : l'étiquette donne un coup (×1,06) ; 4.30 les annotations s'effacent vite (0,15 s) ; 4.40 la caméra plonge dans les vases (téléphone échelle 1,30 → 3,40, flou 0 → 6 → 0) ; 4.75 l'écran s'éteint : le calque .off monte 0 → 1 en 0,3 s ; 5.05 l'écran éteint couvre toute l'image.
  PISTE CAMÉRA : dérive 2.10 à 4.40 échelle +0,03/s, x -4 px/s ; 4.40 à 5.20 plongée power2.in vers l'échelle 3,40 centrée sur les vases ; mur : flou 12 → 18 px pendant la plongée, il sort de l'image.
  COUCHES ET PROFONDEUR : avant-plan l'étiquette ; sujet les vases ; fond le cadre du téléphone puis le mur flou ; pic 3 couches à 3.60.
  OBJET-PONT ET VECTEUR : l'écran du téléphone devient le fond noir du pivot (même brun #2c2420).
  SON : pop à 3.60 ; whoosh à 4.40 ; impact grave à 5.20 (couture).
  IMAGE CLÉ : 3.80 : les deux vases entourés en brique, étiquette « inclus ? », sous-titre « … ont l'air fournis. » avec « fournis. » en boîte.

## Frame 6 : Le pivot · 20.40 → 24.40

- scene: Sur le brun, la phrase « Choisir une étagère devrait être simple. » tombe mot par mot au centre ; dans le silence, il ne reste que « simple. », dont le point devient un point de lumière sable qui grandit jusqu'à remplir l'image de crème
- duration: 4.00s
- transition_in: cut
- status: animated
- src: compositions/frames/06-pivot.html
- voiceover: "Choisir une étagère devrait être simple."
- type: pivot
- blueprint: kinetic-type-beats (Adapt)
- focal: la phrase centrée, puis le point de lumière
- rules: center-outward-expansion, ambient-glow-bloom
- world: dark
- handoff_in: à 0.00 : écran plein cadre entièrement éteint (calque .off du téléphone, brun #2c2420, opacité 1) ; téléphone à l'échelle 3,4 centré sur les vases, son cadre hors de l'image ; mur hors de l'image ; aucune annotation visible ; aucun texte
- handoff_out: à 4.00 : image entièrement crème #f4efe7 (le cercle de lumière couvre tout) ; aucun texte, aucun objet ; c'est le haut de l'écran allumé du téléphone vu à l'échelle 3,4 (la barre d'adresse de la vraie fiche, couleur #f4efe7)

Word cues: Choisir@0.30 une@0.70 étagère@0.84 devrait@1.30 être@1.60 simple.@1.80

Scene 1 (0.00 à 2.40 s) : P9, la phrase seule
  TEXTE ÉCRAN : moment typographique (.em-type, 84 px, centré, 2 lignes : « Choisir une étagère » / « devrait être simple. ») ; chaque mot tombe de la caméra sur son cue (×1,2, flou 8 → net, 0,2 s expo.out) ; pas de sous-titre en bas ; aucun mot clé en boîte.
  IMAGE DE DÉPART : handoff_in (brun plein).
  ÉTAPES : 0.30, 0.70, 0.84, 1.30, 1.60, 1.80 les six mots tombent ; 2.10 tout le bloc se resserre d'un cran (scale 1 → 0,98, 0,3 s).
  PISTE CAMÉRA : dérive permanente du bloc de texte : échelle 1 → 1,04 de 0.00 à 2.40 (poussée lente), y -6 px/s.
  COUCHES ET PROFONDEUR : sujet la phrase ; fond le brun avec une vignette très douce (radial #2c2420 → #241d1a) ; 2 couches (moment typographique voulu).
  OBJET-PONT ET VECTEUR : le point final de « simple. » devient le point de lumière.
  SON : impact grave à 0.00 (posé par le mix), rien d'autre (silence voulu).
  IMAGE CLÉ : 1.95 : « Choisir une étagère / devrait être simple. » centré sur le brun.

Scene 2 (2.40 à 4.00 s) : P10, le point de lumière (silence)
  TEXTE ÉCRAN : aucun nouveau texte.
  IMAGE DE DÉPART : la phrase centrée.
  ÉTAPES : 2.40 tous les mots sauf « simple. » sortent vite (opacité → 0, y -10, 0,15 s, stagger 0,03) ; 2.70 « simple » sort à son tour, son point reste ; 2.90 le point devient un disque sable 24 px avec halo (accent-light #c8a27c) ; 3.20 le disque grossit à 60 px, halo plus large ; 3.40 le disque devient un cercle crème #f4efe7 qui s'ouvre depuis ce point (clip-path circle 0 → 120 %, 0,6 s power2.in) ; 4.00 l'image est entièrement crème.
  PISTE CAMÉRA : dérive y -6 px/s puis 3.40 à 4.00 poussée vers le point (échelle du calque 1 → 1,15).
  COUCHES ET PROFONDEUR : sujet le point de lumière ; halo ; fond brun.
  OBJET-PONT ET VECTEUR : le cercle crème est l'écran rallumé du téléphone (la séquence 7 recule et révèle le téléphone).
  SON : (silence) ; whoosh doux à 3.40.
  IMAGE CLÉ : 3.10 : un point de lumière sable seul au centre du brun.

## Frame 7 : La vraie fiche · 24.40 → 30.50

- scene: La caméra recule hors de l'écran allumé : le téléphone apparaît devant le mur, sur la vraie fiche d'Étagères Murales ; la caméra descend de ligne en ligne, la matière puis les dimensions se cochent en sable
- duration: 6.10s
- transition_in: cut
- status: animated
- src: compositions/frames/07-vraie-fiche.html
- voiceover: "Chez Étagères Murales, chaque fiche dit ce que vous recevez vraiment. La matière. Les dimensions."
- type: demo
- blueprint: device-surface-showcase (Adapt)
- focal: le téléphone allumé sur la vraie fiche, puis les lignes Matière et Dimensions
- rules: zoom-out-workspace-reveal, svg-path-draw
- world: light
- handoff_in: à 0.00 : image entièrement crème #f4efe7 (le cercle de lumière couvre tout) ; aucun texte, aucun objet ; c'est le haut de l'écran allumé du téléphone vu à l'échelle 3,4 (la barre d'adresse de la vraie fiche, couleur #f4efe7)
- handoff_out: à 6.10 : mur flou 12 px en cam(1500, 1380, 3.00) avec dérive y -10 u/s ; téléphone en couche écran en plein cran vers le haut (power3.inOut entamé à 5.60) qui amène la ligne r3 « Dans le colis » vers y 720 de l'écran, échelle 1,15 ; lignes r1 et r2 cochées sable (texte en encre pleine) ; r3 et r4 encore grises sans coche ; aucun texte en bas (sous-titre sorti à 5.95)

Word cues: Chez@0.20 Étagères@0.38 Murales,@0.80 chaque@1.40 fiche@1.68 dit@1.96 ce@2.16 que@2.28 vous@2.40 recevez@2.56 vraiment.@3.10 La@4.20 matière.@4.34 Les@5.10 dimensions.@5.26

Scene 1 (0.00 à 3.80 s) : P11, le téléphone rallumé
  TEXTE ÉCRAN : sous-titre « Chez Étagères Murales, chaque fiche dit ce que vous recevez vraiment. » mot par mot (2 lignes), [trait : vraiment.] (pic 2) ; sort à 3.75 ; dans le téléphone, la vraie fiche (frame.md page-em) : barre « etageres-murales.fr », photo réelle, titre, « 49,90 € », lignes grises.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.80 recul (voir caméra) : le cadre du téléphone entre dans l'image, puis le mur flou autour ; 0.38 « Étagères » : la barre d'adresse « etageres-murales.fr » se détache d'un léger flash (fond blanc → #f4efe7, 0,2 s) ; 0.90 la photo réelle des 3 étagères se pose dans la page (×1,1 flou 6 → net, 0,2 s) ; 1.40 le titre s'écrit en encre (opacité 0,35 → 1 ligne par ligne, 0,2 s) ; 1.96 « dit » : le prix « 49,90 € » se pose ; 2.40 les quatre lignes grises arrivent en cascade (y +12 → 0, stagger 0,08) ; 3.10 « vraiment. » : le trait sable se dessine ; 3.40 départ du cran vers la ligne r1.
  PISTE CAMÉRA : 0.00 à 0.80 recul expo.out du téléphone : échelle 3,40 → 0,85, centre vers (540, 772) (le haut de l'écran sort de la caméra) ; le mur flou 12 px en cam(1500, 1380, 3.00) apparaît autour ; dérive 0.80 à 3.40 téléphone échelle +0,01/s, y -4 px/s ; mur dérive y -10 u/s.
  COUCHES ET PROFONDEUR : avant-plan aucun ; sujet le téléphone ; fond le mur flou ; pic 2 couches puis 3 avec la photo qui se pose.
  OBJET-PONT ET VECTEUR : le cercle de lumière de la séquence 6 EST le haut de l'écran : le recul le révèle.
  SON : whoosh doux à 0.00 ; pop à 0.90.
  IMAGE CLÉ : 3.20 : le téléphone devant le mur flou, la vraie fiche VASAGLE, sous-titre « … ce que vous recevez vraiment. » avec le trait sable sous « vraiment. ».

Scene 2 (3.80 à 6.10 s) : P12, la matière, les dimensions
  TEXTE ÉCRAN : sous-titre « La matière. Les dimensions. » mot par mot, [boîte : dimensions.] ; sort à 5.95.
  IMAGE DE DÉPART : la fiche cadrée en entier.
  ÉTAPES : 3.40 à 4.00 cran du téléphone vers la ligne r1 (échelle 0,85 → 1,15, r1 à y 720 de l'écran, calculé sur le DOM) ; 4.34 « matière. » : la coche c1 se dessine (0,2 s) et la ligne r1 passe en encre pleine ; 4.60 la ligne r1 glisse de 6 px vers la droite et revient (0,25 s) ; 4.80 cran court vers r2 ; 5.26 « dimensions. » : coche c2 + r2 en encre pleine ; 5.40 sur la photo (hors cadre haut, visible en bord) rien ne bouge ; 5.60 départ du cran vers r3.
  PISTE CAMÉRA : crans du téléphone power3.inOut aux temps ci-dessus (0,5 s chacun) ; dérive entre les crans y -4 px/s ; mur : dérive y -10 u/s, flou 12.
  COUCHES ET PROFONDEUR : avant-plan la coche qui se dessine ; sujet la ligne cochée ; fond le mur flou.
  OBJET-PONT ET VECTEUR : vecteur : cran vers le haut repris au début de la séquence 8.
  SON : ping à 4.34, 5.26.
  IMAGE CLÉ : 5.30 : les lignes « Matière » et « Dimensions » cochées en sable, sous-titre « Les dimensions. » en boîte.

## Frame 8 : Inclus, pas inclus, on vous le dit · 30.50 → 37.00

- scene: Le contenu du colis se coche, puis la ligne « Les objets des photos ne sont pas inclus » ; la page glisse vers la FAQ d'une autre fiche : la question de la charge, et la réponse honnête qui s'écrit ; le téléphone recule et rapetisse vers le mur
- duration: 6.50s
- transition_in: cut
- status: animated
- src: compositions/frames/08-inclus-faq.html
- voiceover: "Ce qui est inclus… et ce qui ne l'est pas. Et quand on ne sait pas, on vous le dit."
- type: payoff
- blueprint: device-surface-showcase (Adapt)
- focal: les lignes r3 et r4, puis la réponse de la FAQ
- rules: svg-path-draw, typewriter-reveal
- world: light
- handoff_in: à 0.00 : mur flou 12 px en cam(1500, 1380, 3.00) avec dérive y -10 u/s ; téléphone en couche écran en plein cran vers le haut (power3.inOut entamé à 5.60) qui amène la ligne r3 « Dans le colis » vers y 720 de l'écran, échelle 1,15 ; lignes r1 et r2 cochées sable (texte en encre pleine) ; r3 et r4 encore grises sans coche ; aucun texte en bas (sous-titre sorti à 5.95)
- handoff_out: à 6.50 : téléphone en couche écran en plein recul (expo.out entamé à 5.90) : centre (720, 760), échelle 0,40, rotation -4°, écran allumé sur la FAQ ; le mur se rapproche du net (flou 12 → 4 px en cours) en cam(1500, 1450, 1.20) ; aucun texte en bas

Word cues: Ce@0.20 qui@0.32 est@0.44 inclus…@0.60 et@1.50 ce@1.62 qui@1.74 ne@1.88 l'est@2.00 pas.@2.22 Et@3.10 quand@3.22 on@3.42 ne@3.52 sait@3.64 pas,@3.86 on@4.40 vous@4.52 le@4.68 dit.@4.80

Scene 1 (0.00 à 2.70 s) : P13, le colis
  TEXTE ÉCRAN : sous-titre « Ce qui est inclus… et ce qui ne l'est pas. » mot par mot, [boîte : inclus…] ; sort à 2.65.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.30 fin du cran vers r3 ; 0.60 « inclus… » : coche c3, r3 en encre pleine ; 0.85 dans r3, les trois éléments du colis s'éclairent l'un après l'autre (« 3 étagères », « accessoires de montage et clé Allen », « notice en français » : soulignement sable fin 0,15 s chacun, stagger 0,2) ; 1.50 cran court vers r4 ; 2.22 « pas. » : coche c4, r4 en encre, « pas inclus » en gras ; 2.40 sur la photo, dans le haut de l'écran, rien ne change (aucun objet n'est ajouté à la photo réelle) ; 2.50 la page commence à glisser vers le haut.
  PISTE CAMÉRA : fin du cran (séquence 7 : rejouer sa fin à l'identique) ; dérive y -4 px/s ; 1.50 à 2.00 cran r3 → r4 ; mur dérive y -10 u/s.
  COUCHES ET PROFONDEUR : avant-plan la coche ; sujet la ligne ; fond le mur flou.
  OBJET-PONT ET VECTEUR : la page qui glisse vers le haut amène la FAQ (la fiche continue sous le doigt du défilement).
  SON : ping à 0.60, 2.22.
  IMAGE CLÉ : 2.30 : les quatre lignes cochées, « Les objets des photos ne sont pas inclus » en encre, sous-titre « … ce qui ne l'est pas. ».

Scene 2 (2.70 à 6.50 s) : P14, la réponse honnête, puis le recul
  TEXTE ÉCRAN : sous-titre « Et quand on ne sait pas, on vous le dit. » mot par mot, [trait : dit.] (pic 3) ; sort à 5.75 ; dans le téléphone, la carte FAQ (frame.md, emFaq) : « Questions fréquentes », « Étagère d’angle de douche en inox 304 », « Quelle charge peut-elle porter ? », réponse.
  IMAGE DE DÉPART : la page qui glisse.
  ÉTAPES : 2.70 la carte FAQ monte depuis le bas de l'écran du téléphone (y +400 → 0, 0,4 s expo.out) et couvre la fiche ; 3.10 la question passe en encre pleine ; 3.64 « sait » : un petit cercle de chargement (3 points) apparaît dans la bulle de réponse ; 4.00 la phrase « Le vendeur ne l’a pas encore communiquée. » s'écrit mot à mot (typewriter, 0,6 s) ; 4.70 « Nous lui avons posé la question. » s'écrit (0,5 s) ; 4.80 « dit. » : trait sable sous le mot ; 5.30 la bulle de réponse donne un léger coup (×1,03) ; 5.90 départ du recul : le téléphone rapetisse et part vers le haut gauche, vers le mur (voir caméra).
  PISTE CAMÉRA : 2.70 à 3.30 le téléphone revient à l'échelle 0,95 centré (540, 772) ; dérive 3.30 à 5.90 échelle +0,02/s ; 5.90 à 6.80 recul expo.out : téléphone vers centre (720, 760), échelle 0,30, rotation -6° (il n'est qu'en cours à 6.50 : échelle 0,40, rotation -4°) ; mur : 5.90 à 6.80 cam(1500, 1380, 3.00) → cam(1500, 1600, 0.60) et flou 12 → 0 (à 6.50 : cam(1500, 1450, 1.20), flou 4).
  COUCHES ET PROFONDEUR : avant-plan la bulle de réponse ; sujet la FAQ ; fond le mur qui se précise ; pic 3 couches à 6.20.
  OBJET-PONT ET VECTEUR : le téléphone qui recule vers le mur va y déposer la photo des étagères (séquence 9).
  SON : pop à 2.70 ; typing de 4.00 à 5.20 ; whoosh à 5.90.
  IMAGE CLÉ : 5.00 : la FAQ, « Quelle charge peut-elle porter ? », la réponse « Le vendeur ne l’a pas encore communiquée. Nous lui avons posé la question. », sous-titre « … on vous le dit. » avec le trait sable sous « dit. ».

## Frame 9 : Le mur n'est plus vide · 37.00 → 45.00

- scene: Le téléphone dépose la photo des étagères sur le mur nu du début : les vraies étagères s'y posent, les traits au crayon s'effacent ; « Étagères Murales » et le logo arrivent ; l'iris s'ouvre depuis le logo sur la carte de fin brune ; le curseur clique « etageres-murales.fr »
- duration: 8.00s
- transition_in: cut
- status: animated
- src: compositions/frames/09-fin.html
- voiceover: "Étagères Murales. Pour sublimer vos murs et finir vos pièces. Lien dans la bio."
- type: cta
- blueprint: cta-morph-press (Adapt)
- focal: les étagères posées sur le mur, puis le logo, puis le bouton
- rules: cursor-click-ripple, center-outward-expansion
- world: light
- handoff_in: à 0.00 : téléphone en couche écran en plein recul (expo.out entamé à 5.90) : centre (720, 760), échelle 0,40, rotation -4°, écran allumé sur la FAQ ; le mur se rapproche du net (flou 12 → 4 px en cours) en cam(1500, 1450, 1.20) ; aucun texte en bas
- handoff_out: aucun (fin du film, noir à 8.00)

Word cues: Étagères@0.30 Murales.@0.80 Pour@1.70 sublimer@1.86 vos@2.40 murs@2.56 et@3.00 finir@3.14 vos@3.50 pièces.@3.66 Lien@4.70 dans@4.94 la@5.12 bio.@5.24

Scene 1 (0.00 à 4.40 s) : P15, la photo rejoint le mur
  TEXTE ÉCRAN : pas de sous-titre pour « Étagères Murales. » (le logo le dit : logo-em.png + logo-texte.png, couleur d'origine, en haut du cadre, y 260 à 520, centrés, petits : logo 150 px, texte 520 px de large) ; puis sous-titre « Pour sublimer vos murs et finir vos pièces. » mot par mot, [boîte : murs] ; sort à 4.30.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.50 le téléphone finit son recul ; 0.30 la photo des étagères sort de l'écran du téléphone (copie écran de la photo, échelle qui grandit) et vole vers sa place sur le mur (W.shelves, centre (1500, 1450), largeur 900 u) ; 0.55 le téléphone sort par le bas, vite (y +900, 0,25 s power2.in) ; 0.60 relais : W.shelves passe à opacité 1 exactement sous la copie, la copie disparaît ; 0.62 contact : petit tassement des étagères (y -6 → 0, 0,15 s) ; 0.65 les traits au crayon (« 6 mois », compte, repères, croquis) s'effacent (opacité → 0, 0,3 s, stagger 0,05) ; 0.80 le logo É arrive (×1,2 flou 8 → net) ; 1.00 le texte « Étagères Murales » arrive ; 1.70 à 3.66 la caméra glisse lentement sur le mur rempli ; 2.56 « murs » : boîte ; 3.66 « pièces. » : les coussins du canapé se tassent d'un léger temps (rime avec 3.90 de la séquence 1) ; 4.40 départ de l'iris.
  PISTE CAMÉRA : 0.00 à 0.60 fin du recul du mur vers cam(1500, 1650, 0.55) (F-fin) et flou 4 → 0 ; dérive 0.60 à 4.40 x +12 u/s, échelle +0,012/s.
  COUCHES ET PROFONDEUR : avant-plan le téléphone qui sort (flou) puis le dossier du canapé flou 3 px ; sujet les étagères sur le mur ; fond le grain ; pic 3 couches.
  OBJET-PONT ET VECTEUR : la photo de la fiche devient les vraies étagères au mur (le mur du début n'est plus vide) ; le logo devient le centre de l'iris.
  SON : whoosh à 0.30 ; pop à 0.62 ; notification (signature) à 0.70.
  IMAGE CLÉ : 2.60 : le mur du début avec les 3 étagères posées, le canapé dessous, le logo en haut, sous-titre « … vos murs … » avec « murs » en boîte.

Scene 2 (4.40 à 8.00 s) : P16, la carte de fin
  TEXTE ÉCRAN : carte de fin brune #3a2f2a : logo-em.png 220 px, logo-texte.png 640 px de large, le bouton « etageres-murales.fr » (fond #f5f0e8, texte #3a2f2a, Inter 600 44 px, rayon 48, 520 × 104) en y 1150 ; sous-titre clair (.em-sub.dark) « Lien dans la bio. » mot par mot, [boîte : bio.] ; reste jusqu'à 7.60.
  IMAGE DE DÉPART : le mur rempli et le logo en haut.
  ÉTAPES : 4.40 iris : un cercle brun #3a2f2a s'ouvre depuis le centre du logo (clip-path circle 0 → 150 %, 0,6 s power2.inOut) ; 4.70 le logo et le texte se placent sur la carte (ils glissent de leur place du plan 1 vers leur place sur la carte, y 600 et 860) ; 5.10 le bouton arrive (×1,15 flou 8 → net) ; 5.40 le halo sable du bouton respire une fois (opacité 0,4 → 0,7 → 0,4, 0,8 s) ; 5.60 le curseur arrive d'un seul mouvement depuis (980, 1700) vers le bouton (emClick, 0,45 s) ; 6.05 clic : le bouton se remplit de sable #a97c50, texte crème ; 6.30 onde du clic ; 6.60 à 8.00 tenue vivante : le logo dérive (y -4 px/s), le halo respire une seconde fois (6.80) ; 7.60 sous-titre sort ; 7.80 à 8.00 sortie au noir (calque noir 0 → 1).
  PISTE CAMÉRA : dérive de la carte entière échelle 1 → 1,03 de 4.40 à 8.00 ; aucun cran.
  COUCHES ET PROFONDEUR : avant-plan le curseur ; sujet le bouton ; fond la carte brune avec vignette douce.
  OBJET-PONT ET VECTEUR : aucun (fin du film).
  SON : whoosh à 4.40 ; click à 6.05.
  IMAGE CLÉ : 6.20 : carte brune, logo É, « Étagères Murales », bouton « etageres-murales.fr » rempli de sable sous le curseur, sous-titre « Lien dans la bio. » avec « bio. » en boîte.
