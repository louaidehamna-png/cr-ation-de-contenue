# Prompts motion design Opus 5.5 (guide « AI Builders », Tyler Mommsen) : ce qu'on en retient

Source : PDF « Claude Opus 5.5 Motion Graphics: Every Prompt From the Video » (13 pages), lu le 22/11/2026.

## Les leçons

1. **Toujours nommer le framework** : « using HyperFrames ». Sans ça, Claude bricole ses propres outils et le rendu est irrégulier.
2. **Prompt en sections** : PRODUCT, STORY, FORMAT, LOOK, MOTION, SOUND, QUALITY CHECK, RULES.
3. **Être précis** : codes couleur exacts, polices nommées, comment chaque scène devient la suivante, ce que fait la
   caméra, un son pour chaque action.
4. **Le QUALITY CHECK est le plus gros gain** : rendre, regarder une image toutes les 0,5 s (0,25 s pour un logo),
   critiquer comme un motion designer senior, corriger, recommencer. Au moins 3 à 4 tours.
5. **Un fil visuel unique** qui traverse tout le film (une ligne, une forme, une couleur) et finit dans le logo.
6. **Chaque scène se transforme en la suivante**, pas de fondu ni de coupe (= notre règle d'or n° 3, l'objet-pont).
7. **Caméra toujours en mouvement**, vraie profondeur (ombres douces, flou au loin), vrai flou de mouvement.
8. **Une seule couleur d'accent**. À éviter : dégradés, icônes de banque d'images, tout ce qui ressemble à un modèle.
9. **Logo** : l'animation doit *devenir* le logo (pas de fondu ni de zoom d'apparition), dernière seconde immobile,
   lisible en tout petit, exporter aussi une version à fond transparent.
10. **Itérer dans la même conversation**, un détail à la fois. Ou faire écrire le prompt par Claude (méta-prompt plus bas).

## Ce qui change pour nous (règles du projet, CLAUDE.md et AGENTS.md)

- Format par défaut **1080x1920, 9:16**, haut et bas libres pour l'interface des réseaux.
- Charte : crème #F5F0E8, brun #3A2F2A, brun foncé #2C2420, sable #C8A27C (accent unique), police Inter.
- **Chaque chiffre vient de la fiche Shopify**. Pas de superlatif, pas de fausse urgence, pas de faux avis.
- **Mains autorisées**, jamais de visage, de corps ni d'animal.
- Sons : soit faits en code, soit la bibliothèque `.claude/skills/media-use/audio/assets/sfx/` (ce qu'on utilise).
  Pas de musique générée ; la musique, si besoin, est un morceau CC0 fourni par l'utilisateur.
- Voix : ElevenLabs, Nicolas « Petit ton Animateur Radio » (eleven_v4).
- La règle « Don't stop and don't ask me anything » du guide ne remplace pas les étapes validées du skill
  `motion-design` quand on fait un film de marque ; elle convient aux vidéos courtes (UGC, logo).

## Modèle prêt pour la boutique (à remplir)

```
Create a [20] second vertical [UGC ad / explainer / logo sting] for [produit] from etageres-murales.fr, using HyperFrames.

PRODUCT
- [Ce que c'est et pour qui, en une ligne.]
- Promise: [la seule chose à retenir].
- Show [3] points in this order: [points, chacun tiré de la fiche Shopify].

STORY
- Hook, [3] points, call to action. You design the scenes and write the words.
- One idea runs through the whole video: [un fil visuel : une ligne sable, la forme du produit, un mur].
- Every scene must transform into the next one through an object. Nothing fades or cuts.
- End on the logo and "Lien en bio".

FORMAT
- 1080x1920, 9:16, 30 fps, exactly [20] seconds, MP4. Keep the top 250 px and bottom 400 px free of text.

LOOK
- [Calme et chaleureux / vif et rapide.]
- Background #F5F0E8, text #2C2420, one accent only, #C8A27C. Inter everywhere.
- Use the real product photos from produits/[dossier]/ (full frame).
- Avoid: gradients, stock icons, more than one accent color, anything that looks like a template.
- No faces, no bodies, no animals. Hands are allowed.

MOTION
- The camera is always moving. Nothing sits frozen on screen.
- Something new every half second: a word, an object, a highlight.
- Real depth: soft shadows, blur on things far away.

SOUND
- Voice: assets/audio/voix.mp3 (ElevenLabs). Every cut lands on the start of a sentence.
- A sound effect for every action from the sfx library: whoosh on cuts, pop on words, click on numbers,
  low hit on the price. Each sound sits on the exact frame of its action, under the voice. No music.

QUALITY CHECK
- Render it and look at a frame every half second.
- Critique it like a senior motion designer: story, layout, spacing, type, timing, readability,
  whether every number matches the Shopify listing, and whether the sound matches the picture.
- Fix everything, render again, critique again. At least three full rounds.

RULES
- Every number on screen or in the voice comes from the Shopify listing. No superlatives.
- When it's finished, give me the final MP4, confirm it has sound, and list what you fixed in each round.
```

## Méta-prompt : faire écrire le prompt par Claude

> I want to make a motion graphics video with Claude Code and HyperFrames. Here's what it is: [la vidéo, le produit,
> la durée]. Write me a detailed prompt for it with these sections: PRODUCT, STORY, FORMAT, LOOK, MOTION, SOUND,
> QUALITY CHECK and RULES. Be specific: exact hex colors, named fonts, how each scene turns into the next, what the
> camera does, and what sound plays on each action. In QUALITY CHECK, tell Claude to render it, look at a frame every
> half second, critique it like a senior motion designer, fix everything and repeat for at least four rounds. Avoid
> anything that looks like a template.

## Les 20 styles du guide (idée → usage chez nous)

| Style | Exemple du guide | Idée pour la boutique |
|---|---|---|
| Particles | intro de chaîne | des particules sable qui forment le logo |
| Liquid morph | explication d'appli | une tache qui devient une étagère, puis un mur rangé |
| Holographic | révélation produit | (peu adapté au bois) |
| Neon glow | promo Reels | déjà fait : « Tes étagères font fouillis » |
| Wireframe 3D | comment ça marche | une étagère qui s'assemble pièce par pièce, cotes |
| Glassmorphism | vitrine d'appli | fiches produit en cartes givrées |
| Kinetic typography | citation 9:16 | une phrase déco mot par mot sur fond crème |
| Isometric | parcours d'une commande | de la commande au mur |
| Clay 3D | intro de marque | (pas d'animaux : mascotte objet seulement) |
| ASCII art | outil développeur | (hors sujet) |
| Gradient mesh | intro podcast | (dégradés : à éviter avec notre charte) |
| Comic book | annonce de fonction | avant / après en 3 cases |
| Split-flap | chiffres de l'année | stats boutique, si vraies et vérifiées |
| Retro VHS | pub rétro | pub années 80 d'une étagère vintage |
| Halftone | histoire en magazine | histoire de l'étagère murale |
| Bauhaus | graphique animé | formes géométriques : étagères géométriques métal |
| Pixel art | célébration | (avec pixelfx installé) |
| Blueprint | vue éclatée | plan technique : cotes, fixations, charge |
| Art deco | invitation | collection « laiton et noir » |
| Neo-brutalism | annonce sociale | nouveauté ou promo réelle, blocs pleins |

Ligne à ajouter à n'importe quel style pour la boucle de qualité :
> Then render it, look at a frame from every half second, critique it like a senior motion designer, fix everything
> you find and repeat for at least three rounds.
