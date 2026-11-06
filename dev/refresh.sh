#!/usr/bin/env bash
# Оновлення під нову версію системи Daggerheart.
# Використання: dev/refresh.sh 2.13.0
set -euo pipefail
TAG="${1:?вкажіть тег системи, напр. 2.13.0}"
cd "$(dirname "$0")/.."
rm -rf tmp_data && mkdir -p tmp_data
git clone --depth 1 --branch "$TAG" https://github.com/Foundryborne/daggerheart tmp_data/original-daggerheart
node scripts/generate_originals.js
# Нові рядки, яких ще немає в dev/work/*.src.tsv, потрапляють у dev/work/n<дата>.src.tsv
P="n$(date +%Y%m%d)"
python3 dev/tools/extract.py "$P" original/daggerheart.*.json original/lang/en.json || true
python3 dev/tools/todo.py "$P" 0 99999 | tail -1
python3 dev/tools/build_packs.py
python3 dev/tools/build_lang.py module/i18n/systems/daggerheart.json
echo "Перекладіть рядки з dev/work/$P.src.tsv у dev/tm/$P.tsv (формат: id<TAB>переклад) і запустіть build_packs/build_lang ще раз."
