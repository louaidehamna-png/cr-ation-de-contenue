# Contenus Étagères Murales

Vidéos et visuels pour la boutique etageres-murales.fr.

- Motion design : suivre la méthode installée (skill `motion-design`, garde-fous dans `AGENTS.md`, grammaire dans
  `patterns/`). Chaque nouveau film dans son dossier à la racine :
  `bash .claude/skills/motion-design/scripts/new-project.sh <projet>`.
- Format par défaut : vertical 9:16 (1080x1920) pour Reels, TikTok et Shorts, sauf demande contraire. La méthode est
  écrite pour du 16:9 : adapter les cadrages et garder libres le haut et le bas (interface des réseaux).
- Charte : crème #F5F0E8, brun #3A2F2A, brun foncé #2C2420, sable #C8A27C (logo), police Inter. Logos HD dans
  `vasagle-video/tuto-mur/assets/` (logo-em-hd.png, logo-texte-hd.png).
- Visuels produits sur fond blanc : `produits/` (un dossier par produit, avec sa fiche).
- Chaque chiffre affiché vient de la fiche Shopify. Pas de superlatif, pas de fausse urgence, pas de faux avis.
- Rendu de vérification d'images de style : Python playwright avec `executable_path="/opt/pw-browsers/chromium"`.
- Les anciens projets (`vasagle-video/montage`, `vasagle-video/tuto-mur`) restent en HyperFrames 0.9.26 :
  les relancer avec leur `npm run render`.

@AGENTS.md
