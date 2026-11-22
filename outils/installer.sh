#!/usr/bin/env bash
# Réinstalle les outils aux commits audités (COMMITS-AUDITES.txt). À lancer depuis la racine du dépôt :
#   bash outils/installer.sh
set -e
cd "$(dirname "$0")"
mkdir -p repos
while read -r name url sha; do
  [ -d "repos/$name/.git" ] || git clone -q --filter=blob:none "$url" "repos/$name"
  git -C "repos/$name" fetch -q --depth 1 origin "$sha" && git -C "repos/$name" checkout -q "$sha"
done < COMMITS-AUDITES.txt
npm install --no-fund --no-audit --ignore-scripts
for d in pixelfx ClaudeAnimationBase lemo-opuscar video-shotcraft/template; do (cd "repos/$d" && npm ci --no-fund --no-audit --ignore-scripts); done
pip install -q librosa -r repos/lemo-opuscar/requirements.txt ./repos/mcp-for-blender
ln -sfn "$PWD/repos/lemo-opuscar" ~/lemo-opuscar
echo "Outils prêts."
