#!/usr/bin/env bash
cd "$(dirname "$0")"

cat ../../src/anexo_04_perguntas/técnica_e_ética.csv | shuf | python3 convert_csv.py > ../../src/anexo_04_perguntas/técnica_e_ética.asc
cat ../../src/anexo_04_perguntas/legislação.csv | shuf | python3 convert_csv.py > ../../src/anexo_04_perguntas/legislação.asc
cat ../../src/anexo_04_perguntas/eletronica.csv | shuf | python3 convert_csv.py > ../../src/anexo_04_perguntas/eletronica.asc
