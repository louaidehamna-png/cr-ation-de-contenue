# Kit Katana : « Ton salon a l'air petit » (version fluo sur noir)

À utiliser dans une session **Claude Cowork** (ou Claude chat) avec le connecteur **Higgsfield** activé.
L'illimité Higgsfield ne marche pas depuis Claude Code : c'est pour ça qu'on passe par Cowork.

## Mode d'emploi
1. Ouvre une session Cowork et glisse **tout ce dossier** dedans.
2. Copie-colle le contenu de `01-PROMPT-A-COLLER.md` comme premier message.
3. Laisse tourner. Katana ne pose pas de questions : il analyse, génère les plans, monte et livre la vidéo.
4. Récupère le MP4 final. Si tu veux des retouches (textes, sous-titres, voix), dépose-le dans le dépôt
   `cr-ation-de-contenue` et je m'en occupe côté Claude Code.

## Contenu du dossier
- `01-PROMPT-A-COLLER.md` : le brief complet à coller (style, couleurs, règles, voix).
- `02-PLANS-PHRASE-PAR-PHRASE.md` : les 18 plans, un par phrase, avec le moment exact où chacun commence.
- `03-VOIX.md` : le texte de la voix et les réglages ElevenLabs, si tu veux la régénérer.
- `voix-nicolas.mp3` : la voix déjà prête (Nicolas, ton animateur radio), à garder telle quelle.
- `reference-rythme.mp4` : la version actuelle de la vidéo, à suivre pour le rythme et la structure seulement.
- `logo-em.png` : le logo, à poser en petit sur les 2 dernières secondes.

## Choisir la couleur fluo
Le prompt est écrit pour l'**orange fluo #FF5A00**. Pour changer, remplace ce code partout dans le prompt :
- vert fluo : `#39FF14`
- rouge fluo : `#FF1A1A`
Une seule couleur fluo par vidéo.
