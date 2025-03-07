'''
python3 script_restructure_json.py
'''

import json

### Supporting dictionaries

# Systematic variations
syst_dictionary = {
    ""      : "sf",
    "_elup" : "sfup",
    "_eldn" : "sfdown",
}

def restructure_json(input_file_name, scale_factor, year, working_point = '2lss', latinos_wp = 'ttH_ID'):

    # Selection to be corrected (ID, Isolation, ttHMVA, ...)
    sf_dictionary = {
        "mu_1_allflavor_channels" : ["Muon-ID-SF",              f"Muon ttH-MVA ID scale factors for the {year} era",                      f"muonSF_{year}_ttH_ID.json",         "13"],
        "mu_2_allflavor_channels" : ["Muon-Iso-SF",             f"Muon ttH-MVA Isolation scale factors for the {year} era",               f"muonSF_{year}_ttH_Iso.json",        "13"],
        "el1_allflavor_channels"  : ["Electron-ID-SF",          f"Electron ttH-MVA ID scale factors for the {year} era",                  f"electronSF_{year}_ttH_ID.json",     "11"],
        "el2_allflavor_channels"  : ["Electron-Iso-SF",         f"Electron ttH-MVA Isolation scale factors for the {year} era",           f"electronSF_{year}_ttH_Iso.json",    "11"],
        "el3_allflavor_channels"  : ["Electron-RecoToLoose-SF", f"Electron ttH-MVA Reco-to-Loose scale factors for the {year} era",       f"electronSF_{year}_ttH_Reco.json",   "11"],
        "el4_allflavor_channels"  : ["Electron-ptge20-SF",      f"Electron ttH-MVA scale factors for pt above 20 GeV for the {year} era", f"electronSF_{year}_ttH_lowpt.json",  "11"],
        "el5_allflavor_channels"  : ["Electron-ptlt20-SF",      f"Electron ttH-MVA scale factors for pt below 20 GeV for the {year} era", f"electronSF_{year}_ttH_highpt.json", "11"],
    }
    
    title_name        = sf_dictionary[scale_factor][0]
    title_description = sf_dictionary[scale_factor][1]
    output_file_name  = sf_dictionary[scale_factor][2]
    flavor            = sf_dictionary[scale_factor][3]

    # Carica il file JSON originale
    with open(input_file_name, "r") as f:
        data = json.load(f)
    
    # Lista per i nuovi dati ristrutturati
    restructured_data = {
        "schema_version" : 2,
        "description" : "ttH electron scale factors",
        "corrections" : [
            {
                "name" : title_name,
                "description" : title_description,
                "version" : 2,
                "inputs" : [
                    {
                        "name": "year",
                        "type": "string",
                        "description": "year/scenario: example, 2017, 2022FG etc"
                    },
                    {
                        "name": "ValType",
                        "type": "string",
                        "description": "sf/sfup/sfdown (sfup = sf + syst, sfdown = sf - syst) "
                    },
                    {
                        "name": "WorkingPoint",
                        "type": "string",
                        "description": "Working Point of choice : Loose, Medium etc."
                    },
                    {
                        "name": "eta",
                        "type": "real",
                        "description": "supercluster eta"
                    },
                    {
                        "name": "pt",
                        "type": "real",
                        "description": "electron pT"
                    }
                ],
                "output": {
                    "name": "weight",
                    "type": "real",
                    "description": "value of scale factor (nominal, up or down)"
                },
                "data": {
                    "nodetype": "category",
                    "input": "year",
                    "content": [
                        {
                            "key": year,
                            "value": {
                                "nodetype": "category",
                                "input": "ValType",
                                "content": [
                                ],
                            }
                        }
                    ]
                }
            }
        ]
    }
    
    # Itera sulle correzioni per trovare quelle relative agli elettroni
    
    # Input file structure:
    # channel  : 2lss, 3l
    # abspdgid : 11, 13
    # syst     : "", "_muup, "_mudn", "_elup", "_eldn"
    # pt       : real values
    # eta      : real values
    
    for correction in data["corrections"]:
        print("===========")
        print("CORRECTION:")
        for key, value in correction.items():
            print(f"{key} : {value}")
            print()
    
        print(f"Correction name: {correction['name']}")
        # Ignora le voci non relative agli elettroni
        if not correction["name"].startswith(scale_factor):
            continue
        
        for category in correction["data"]["content"]:
            print("+++++++++")
            print("CATEGORY:")
            for key, value in category.items():
                print(f"{key} : {value}")
                print()
    
            print(f"Category key: {category['key']}")
            if category["key"] != working_point:
                continue
            
            syst_entries = category["value"]["content"]
            for syst_entry in syst_entries:
                print("-----------")
                print("SYST ENTRY:")
                for key, value in syst_entry.items():
                    print(f"{key} : {value}")
                    print()
    
                val_type = syst_entry["key"]
                if isinstance(syst_entry["value"], dict) and "content" in syst_entry["value"]:
    
                    print("Syst entry content:")
                    print(syst_entry["value"]["content"])
                    print()
    
                    for idx in range(len(syst_entry["value"]["content"])):
                        print(idx)
                    
                        print("Syst entry content value:")
                        print(syst_entry["value"]["content"][idx]["value"])
                        print()
    
                        print("Syst entry content key:")
                        print(syst_entry["value"]["content"][idx]["key"])
                        print()
                    
                        bins_eta, bins_pt = syst_entry["value"]["content"][idx]["value"]["edges"]
                        print("Bins:")
                        print(bins_eta, bins_pt)
                        print()
                        content = syst_entry["value"]["content"][idx]["value"]["content"]
                        syst_variation = syst_entry["value"]["content"][idx]["key"]
    
                        print(f"Syst variation: {syst_variation}")
                        if "mu" in syst_variation :
                            print("Skipping muons")
                            continue
    
                        syst_var = syst_dictionary[syst_variation]
                        
                        restructured_data["corrections"][0]["data"]["content"][0]["value"]["content"].append({
                            "key" : syst_var,
                            "value" : {
                                "nodetype" : "category",
                                "input" : "WorkingPoint",
                                "content" : [
                                    {
                                        "key" : latinos_wp,
                                        "value": {
                                            "nodetype": "multibinning",
                                            "inputs": [
                                                "eta",
                                                "pt"
                                            ],
                                            "edges" : [
                                                bins_eta,
                                                bins_pt
                                            ],
                                            "content" : content,
                                            "flow": "error"
                                        }
                                    },
                                ]
                            }
                        })
    
    # Salva il nuovo JSON
    with open(output_file_name, "w") as f:
        json.dump(restructured_data, f, indent=4)
    
    print(f"File ristrutturato salvato come {output_file_name}")

    

# Inputs
# working_point    = "2lss"
# latinos_wp       = "ttH_ID"

scale_factors    = [
    "mu_1_allflavor_channels",
    "mu_2_allflavor_channels",
    "el1_allflavor_channels",
    "el2_allflavor_channels",
    "el3_allflavor_channels",
    "el4_allflavor_channels",
    "el5_allflavor_channels",
]

years = [
    "2016HIPM",
    "2016noHIPM",
    "2017",
    "2018",
]

for year in years:
    print(f"Analyzing year {year}")
    input_file_name  = f"leptonSF_{year}_formatted.json"
    print(f"Input file name: {input_file_name}")

    for scale_factor in scale_factors:
        print(f"Analyzing scale factor {scale_factor}")
        restructure_json(input_file_name, scale_factor, year)    
