# Contenus Étagères Murales

Vidéos et visuels pour la boutique etageres-murales.fr.

- Motion design : suivre la méthode installée (skill `motion-design`, garde-fous dans `AGENTS.md`, grammaire dans
  `patterns/`). Chaque nouveau film dans son dossier à la racine :
  `bash .claude/skills/motion-design/scripts/new-project.sh <projet>`.
- **3 règles d'or, pour chaque vidéo** (à vérifier sur le storyboard puis sur le rendu) :
  1. **La caméra bouge tout le temps** : jamais d'image figée, même pendant une phrase (poussée lente, travelling,
     zoom franc dans un seul sens, sans aller-retour).
  2. **Quelque chose de neuf toutes les demi-secondes** : un mot qui apparaît, un objet qui arrive, une mise en
     valeur, une annotation. Compter les événements sur la planche contact toutes les 0,5 s : aucune case vide.
  3. **Le maximum de transitions passe par un objet** (l'objet-pont) : un élément de la scène change de rôle et
     devient la scène suivante. Les coupes franches et les fondus restent l'exception.
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
