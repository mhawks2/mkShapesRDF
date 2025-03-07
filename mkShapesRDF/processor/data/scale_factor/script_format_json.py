'''
python3 script_format_json.py
'''

import gzip
import json

# Percorso del file
input_path  = "leptonSF_2016APV.json.gz"
output_path = "leptonSF_2016preVFP_formatted.json"

# Decomprimere e leggere il file JSON
with gzip.open(input_path, "rt", encoding="utf-8") as f:
    data = json.load(f)

# Scrivere il JSON formattato
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"File formattato salvato in {output_path}")
