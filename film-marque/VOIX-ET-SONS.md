# Voix et effets sonores · « Le mur vide »

## 1. La voix (ElevenLabs, Text to Speech)

Réglages : modèle **Eleven v4**, voix **Théo - UGC Creator et publicité**, langue **Français** (à régler à la main),
Stabilité **45 %**, Similarité **85 %**. Génère **2 ou 3 prises** et garde la meilleure.

Texte à coller tel quel (une phrase par ligne ; les silences du temps muet et du pivot se font au montage, pas dans le
texte) :

```
Six mois que vous avez emménagé.
Et le mur au-dessus du canapé... est toujours vide.

Le problème, ce n'est pas la place.
C'est qu'on n'ose pas choisir.
Une fiche dit « bois »... c'est de l'aggloméré.
La charge ? Introuvable.
Et sur la photo, les vases ont l'air fournis.

Choisir une étagère devrait être simple.

Chez Étagères Murales, chaque fiche dit ce que vous recevez vraiment.
La matière. Les dimensions.
Ce qui est inclus... et ce qui ne l'est pas.
Et quand on ne sait pas, on vous le dit.

Étagères Murales.
Pour sublimer vos murs et finir vos pièces.
Lien dans la bio.
```

Dépose la prise choisie dans `film-marque/assets/audio/voix.mp3` (ou envoie-la-moi) : je recale chaque mot du film
dessus.

## 2. Les effets sonores (ElevenLabs, Sound Effects ; pas de musique)

Chaque son est court, sec, sans musique. Durée conseillée entre parenthèses. Le temps indique où il tombe dans le film.

| Nom du fichier | Prompt à coller | Durée | Où dans le film |
|---|---|---|---|
| crayon.mp3 | Pencil quickly drawing a short line on a plaster wall, dry graphite scratch, close mic, no music | 0,6 s | 0,05 · 0,20 · 0,35 · 1,10 · 2,70 · 10,40 · 10,70 · 11,00 (traits, repères, croquis) |
| whoosh-court.mp3 | Short soft whoosh of a fast camera pan, airy, clean, no music | 0,5 s | 4,90 · 7,40 · 11,55 (mouvements de caméra) |
| pose-objet.mp3 | Small ceramic vase gently set down on a wooden dresser, soft thud, close mic, no music | 0,4 s | 6,10 · 6,60 · 7,00 (la pile monte) |
| annotation.mp3 | Soft UI pop, subtle bubble click for an annotation appearing, clean, no music | 0,3 s | 13,25 · 15,75 · 18,80 (étiquettes « bois ? », « ? », « inclus ? ») |
| rature.mp3 | Quick red pen strike-through on paper, short dry scribble, no music | 0,4 s | 13,80 (« bois » barré) |
| ecran-eteint.mp3 | Smartphone screen turning off, soft electronic click with a short low hum fading out, no music | 0,8 s | 19,95 (l'écran s'éteint) |
| impact-grave.mp3 | Deep soft cinematic low boom, short, warm, no music, no riser | 1,5 s | 20,40 (le pivot) |
| lumiere.mp3 | Gentle shimmering light swell, soft airy rise, short, no music | 1,2 s | 23,80 (le point de lumière s’ouvre) |
| coche.mp3 | Soft satisfying checkmark ping, warm and clean UI sound, no music | 0,4 s | 28,74 · 29,66 · 31,10 · 32,72 (les coches) |
| frappe.mp3 | Light typing on a phone keyboard, a few soft taps, no music | 1,2 s | 34,50 à 35,70 (la réponse s'écrit) |
| pose-etagere.mp3 | Wooden shelf settling on a wall bracket, soft solid knock, close mic, no music | 0,5 s | 37,62 (les étagères se posent) |
| notification.mp3 | Two-tone soft warm notification chime, elegant, no music | 1 s | 37,70 (le son signature) |
| iris.mp3 | Soft deep whoosh, slow and smooth, no music | 0,8 s | 41,40 (la carte de fin s'ouvre) |
| clic.mp3 | Single clean mouse click, crisp, close mic, no music | 0,2 s | 43,05 (le clic sur le bouton) |

Dépose-les dans `film-marque/assets/audio/sfx/` avec ces noms : je les place sur l'image, baissés sous la voix.
