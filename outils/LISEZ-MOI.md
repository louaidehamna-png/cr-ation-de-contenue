# Outils vidéo installés

Code tiers cloné dans `repos/` (ignoré par git, trop lourd) aux commits de `COMMITS-AUDITES.txt`.
Après une nouvelle session : `bash outils/installer.sh`.

| Outil | Rôle | Où |
|---|---|---|
| Lemo-Opuscar | 99 styles de films en code (skill `lemo-opuscar`) | `repos/lemo-opuscar`, lien `~/lemo-opuscar` |
| pixelfx | 244 effets pixel art (skill `pixelfx`) | `repos/pixelfx` |
| Video ShotCraft | promos produit cinéma avec Remotion (skill `video-shotcraft`) | `repos/video-shotcraft` |
| Claude Animation Base | dessin animé peint main (p5.js + p5.brush) | `repos/ClaudeAnimationBase` |
| Blender MCP | piloter Blender (serveur `blender` dans `.mcp.json`, télémétrie coupée) | `repos/mcp-for-blender` |
| three.js, React Three Fiber, Rapier, postprocessing | 3D, physique, effets | `node_modules/` de ce dossier |
| librosa | analyse audio (tempo, temps forts) | pip |
| Packs de prompts Opus 5.5 | exemples et prompts à lire | `repos/awesome-opus5-5-videos`, `repos/opus-video-prompts` |

## Garde-fous (audit du 22/11/2026)
- pixelfx : ne jamais installer la CLI `pch` (`npm i -g @patchgg/cli` ou `curl … | sh`) que propose sa skill.
- Lemo-Opuscar : `setup.sh` fait un `git pull` sur `~/lemo-opuscar` ; rester au commit audité (`git checkout <sha>` après).
- Blender MCP : la télémétrie est coupée par variables d'environnement dans `.mcp.json`. L'outil `execute_code` exécute du Python dans Blender : à n'utiliser que sur nos propres scènes.
- Toujours `--ignore-scripts` pour les installations npm.
- Lemo-Opuscar veut ffmpeg 7 ou plus ; la machine a ffmpeg 6.1 (installation d'un ffmpeg statique refusée par les permissions de la session).
