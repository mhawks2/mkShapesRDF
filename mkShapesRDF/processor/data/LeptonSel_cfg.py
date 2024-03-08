LepFilter_dict = {
    "Loose": "isLoose",
    "Veto": "isVeto",
    "WgStar": "isWgs",
    "isLoose": "FakeObjWP",
    "isVeto": "VetoObjWP",
    "isWgs": "WgStarObjWP",
}

ElectronWP = {
    "Full2018v9": {
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts
                    "True": ["False"],
                },
            },
        },
        # ------------
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 3",
                        "Electron_convVeto == 1",
                    ],
                    # Barrel
                    "ROOT::VecOps::abs(Electron_eta)  <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    # EndCap
                    "ROOT::VecOps::abs(Electron_eta)  > 1.479": [
                        "Electron_sieie  < 0.03",
                        "ROOT::VecOps::abs(Electron_eInvMinusPInv) < 0.014",
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.2",
                    ],
                },
            },
        },
        "TightObjWP": {
            # ----- mvaFall17V2Iso
            "mvaFall17V2Iso_WP90": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_mvaFall17V2Iso_WP90",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                    ],
                    # Barrel
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    # EndCap
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'tkSF':  { 
                    '1-1' : '/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/2018_UL/electron.json.gz'
                } ,
                'wpSF':  {
                    '1-1' : 'data/scale_factor/Full2018v9/egammaEffi_TightHWW_2018.txt',
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2018v9/mvaFall17V2Iso_WP90/',
            }
        },
    },
    "Full2022v12": {
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    "True": ["False"],
                },
            },
        },
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 3",
                        "Electron_convVeto == 1",
                    ],
                    "ROOT::VecOps::abs(Electron_eta)  <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    "ROOT::VecOps::abs(Electron_eta)  > 1.479": [
                        "Electron_sieie  < 0.03",
                        "ROOT::VecOps::abs(Electron_eInvMinusPInv) < 0.014",
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.2",
                    ],
                },
            },
        },
        "TightObjWP": {
            "wp90iso": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_mvaIso_WP90",
                        "Electron_convVeto",
                    ],
                },
                'tkSF':  {
                    '1-1' : ["Electron-ID-SF", "data/scale_factor/Full2022v12/electron_POG.json"]
                } ,
                'wpSF':  {
                    '1-1' : ["Electron-ID-SF", 'data/scale_factor/Full2022v12/electron_POG.json'],
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2022v12/wp90iso/',
            },
            "mvaWinter22V2Iso_WP90": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_mvaIso_WP90",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'tkSF':  {
                    '1-1' : ["Electron-ID-SF", "data/scale_factor/Full2022v12/electron_POG.json"]
                } ,
                'wpSF':  {
                    '1-1' : ["NUM_Electron_mvaWinter22V2IsoWP90_DEN_ElectronTrack", 'data/scale_factor/Full2022v12/electron_scale.json'],
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2022v12/mvaWinter22V2Iso_WP90/',
            },
        },
    },
    "Full2022EEv12": {
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "True": ["False"],
                },
            },
        },
        # ------------                                                                                                                                                  
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 3",
                        "Electron_convVeto == 1",
                    ],
                    # Barrel                                                                                                                                            
                    "ROOT::VecOps::abs(Electron_eta)  <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    # EndCap                                                                                                                                            
                    "ROOT::VecOps::abs(Electron_eta)  > 1.479": [
                        "Electron_sieie  < 0.03",
                        "ROOT::VecOps::abs(Electron_eInvMinusPInv) < 0.014",
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.2",
                    ],
                },
            },
        },
        "TightObjWP": {
            "wp90iso": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_mvaIso_WP90",
                        "Electron_convVeto",
                    ],
                },
                'tkSF':  {
                    '1-2' : ["2022FG-Electron-ID-SF", "data/scale_factor/Full2022EEv12/electron_POG.json"]
                } ,
                'wpSF':  {
                    '1-2' : ["2022FG-Electron-ID-SF", 'data/scale_factor/Full2022EEv12/electron_POG.json'],
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2022EEv12/wp90iso/',
            },
            # ----- MVA                                                                                                                                                 
            "mvaWinter22V2Iso_WP90": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_mvaIso_WP90",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                    ],
                    # Barrel                                                                                                                                            
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    # EndCap                                                                                                                                            
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'tkSF':  {
                    '1-2' : ["2022FG-Electron-ID-SF", "data/scale_factor/Full2022EEv12/electron_POG.json"]
                } ,
                'wpSF':  {
                    '1-1' : ["NUM_Electron_mvaWinter22V2IsoWP90_DEN_ElectronTrack", 'data/scale_factor/Full2022EEv12/electron_IsoWinter22_Run2022E.json'],
                    '2-2' : ["NUM_Electron_mvaWinter22V2IsoWP90_DEN_ElectronTrack", 'data/scale_factor/Full2022EEv12/electron_IsoWinter22.json'],
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2022EEv12/mvaWinter22V2Iso_WP90/',
            },
        },
    },
    "Full2022EEv11": {
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "True": ["False"],
                },
            },
        },
        # ------------                                                                                                                                                  
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 3",
                        "Electron_convVeto == 1",
                    ],
                    "ROOT::VecOps::abs(Electron_eta)  <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    "ROOT::VecOps::abs(Electron_eta)  > 1.479": [
                        "Electron_sieie  < 0.03",
                        "ROOT::VecOps::abs(Electron_eInvMinusPInv) < 0.014",
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.2",
                    ],
                },
            },
        },
        "TightObjWP": {
            "cut_Tight_HWWW": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 4",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                    ],
                    # Barrel
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                        "Electron_pfRelIso03_all < (0.0388+0.535/Electron_pt)",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'wpSF':  {
                    '1-1' : ["NUM_Electron_isTightWinter22V1_DEN_ElectronTrack", 'data/scale_factor/Full2022EEv11/electron_scale.json'],
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2022EEv11/cut_Tight_HWW/',
            },
            "cut_Tight_HWWW_tthmva70": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 4",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                        "Electron_mvaTTH > 0.7",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                        "Electron_pfRelIso03_all < (0.0388+0.535/Electron_pt)",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'wpSF':  {
                    '1-1' : ["NUM_Electron_isTightWint22_tthmva_DEN_Electron_isTightWinter22V1", 'data/scale_factor/Full2022EEv11/electron_scale.json'],
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2022EEv11/cut_Tight_HWW_tthmva70/',
            },
            "cut_Medium_HWWW": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 3",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                        "Electron_pfRelIso03_all < (0.0388+0.535/Electron_pt)",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'wpSF':  {
                    '1-1' : ["NUM_Electron_isMediumWinter22V1_DEN_ElectronTrack", 'data/scale_factor/Full2022EEv11/electron_scale.json'],
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2022EEv11/cut_Medium_HWW/',
            },
            "mvaWinter22V2Iso_WP90": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_mvaIso_WP90",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'wpSF':  {
                    '1-1' : ["NUM_Electron_mvaWinter22V2IsoWP90_DEN_ElectronTrack", 'data/scale_factor/Full2022EEv11/electron_scale.json'],
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2022EEv11/mvaWinter22V2Iso_WP90/',
            },
            "mvaWinter22V2Iso_WP90_tthmva70": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_mvaIso_WP90",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                        "Electron_mvaTTH > 0.7",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'wpSF':  {
                    '1-1' : ["NUM_Electron_mvaWinter22_tthmva_DEN_Electron_mvaWinter22V2IsoWP90", 'data/scale_factor/Full2022EEv11/electron_scale.json'],
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2022EEv11/mvaWinter22V2Iso_WP90_tthmva70/',
            },
        },
    },
}

MuonWP = {
    # ____________________Full2018v9__________________________
    "Full2018v9": {
        # ------------
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_pt > 10.0",
                    ]
                },
            }
        },
        # ------------
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.4",
                    ],
                    # dxy for pT < 20 GeV
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
            },
        },
        # ------------
        "TightObjWP": {
            "cut_Tight_HWWW": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfIsoId == 4",
                    ],
                    # dxy for pT < 20 GeV
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": [
                        "data/scale_factor/Full2018v9/NUM_TightHWW_DEN_TrackerMuons_eta_pt.root"
                    ],
                },
                "isoSF": {
                    "1-1": [
                        "data/scale_factor/Full2018v9/NUM_TightHWW_ISO_DEN_TightHWW_eta_pt.root"
                    ],
                },
                "fakeW": "data/fake_prompt_rates/Full2018v9/cut_Tight_HWWW/",
            },
            "cut_Tight_HWWW_tthmva_80": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfIsoId == 4",
                        "Muon_mvaTTH > 0.8",
                    ],
                    # dxy for pT < 20 GeV
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                # Update with new SFs
                "idSF": {
                    "1-1": "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_DEN_TrackerMuons_eta_pt.root",
                },
                "isoSF": {
                    "1-1": "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_ISO_DEN_TightHWW_eta_pt.root",
                },
                "tthMvaSF": {
                    "1-1": [
                        "NUM_TightHWW_tth_ISO_DEN_TightHWW_ISO_eta_pt",  # Hist name
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_tth_ISO_DEN_TightHWW_ISO_eta_pt.root",
                    ]  # Nominal+Stat+Syst
                    # 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/ttHMVA0p8_TightHWWCut_SFs_SYS_2018.root', ] # Syst
                },
                "fakeW": "data/fake_prompt_rates/Full2018v9/cut_Tight_HWWW_tthmva_80/",
            },
        },
    },    
    ### ------------------- Full2022 --------------------
    "Full2022v12": {
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_pt > 10.0",
                    ]
                },
            }
        },
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.4",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
            },
        },
        "TightObjWP": {
            "cut_TightID_POG": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.2",
                        "ROOT::VecOps::abs(Muon_dxy) < 0.5",
                        "Muon_pfIsoId >= 4",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022v12/muon_POG.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_TightPFIso_DEN_TightID", "data/scale_factor/Full2022v12/muon_POG.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022v12/cut_TightID_POG/",
            },
            "cut_Tight_HWW": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfIsoId >= 4",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022v12/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_TightIDIso_DEN_TightID", "data/scale_factor/Full2022v12/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022v12/cut_Tight_HWW/",
            },
            "cut_TightMiniIso_HWW": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_miniIsoId >= 3",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022v12/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_TightIDMiniIso_DEN_TightID", "data/scale_factor/Full2022v12/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022v12/cut_TightMiniIso_HWW/",
            },
        },
    },
    "Full2022EEv12": {
        # ------------                                                                                                                                                  
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_pt > 10.0",
                    ]
                },
            }
        },
        # ------------                                                                                                                                                  
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.4",
                    ],
                    # dxy for pT < 20 GeV                                                                                                                               
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV                                                                                                                               
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
            },
        },
        # ------------                                                                                                                                                  
        "TightObjWP": {
            "cut_TightID_POG": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.2",
                        "ROOT::VecOps::abs(Muon_dxy) < 0.5",
                        "Muon_pfIsoId >= 4",
                    ],
                },
                "idSF": {
                    "1-2": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv12/muon_POG.json"],
                },
                "isoSF": {
                    "1-2": ["NUM_TightPFIso_DEN_TightID", "data/scale_factor/Full2022EEv12/muon_POG.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022EEv12/cut_TightID_POG/",
            },
            "cut_Tight_HWW": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfIsoId >= 4",
                    ],
                    # dxy for pT < 20 GeV                                                                                                                               
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV                                                                                                                               
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv12/muon_scale_Run2022E.json"],
                    "2-2": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv12/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_TightIDIso_DEN_TightID", "data/scale_factor/Full2022EEv12/muon_scale_Run2022E.json"],
                    "2-2": ["NUM_TightIDIso_DEN_TightID", "data/scale_factor/Full2022EEv12/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022EEv12/cut_Tight_HWW/",
            },
            "cut_TightMiniIso_HWW": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_miniIsoId >= 3",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv12/muon_scale_Run2022E.json"],
                    "2-2": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv12/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_TightIDMiniIso_DEN_TightID", "data/scale_factor/Full2022EEv12/muon_scale_Run2022E.json"],
                    "2-2": ["NUM_TightIDMiniIso_DEN_TightID", "data/scale_factor/Full2022EEv12/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022EEv12/cut_TightMiniIso_HWW/",
            },
            "cut_Tight_HWW_tthmva_80": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfIsoId >= 4",
                        "Muon_mvaTTH > 0.8",
                    ],
                    # dxy for pT < 20 GeV                                                                                                                               
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV                                                                                                                               
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                # Update with new SFs                                                                                                                                   
                "idSF": {
                    "1-1": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv12/muon_scale_Run2022E.json"],
                    "2-2": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv12/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_TightIDIso_DEN_TightID", "data/scale_factor/Full2022EEv12/muon_scale_Run2022E.json"],
                    "2-2": ["NUM_TightIDIso_DEN_TightID", "data/scale_factor/Full2022EEv12/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022EEv12/cut_Tight_HWW_tthmva_80/",
            },
        },
    },
    ### ------------------- Full2022EE --------------------
    "Full2022EEv11": {
        # ------------                                                                                                                                                  
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_pt > 10.0",
                    ]
                },
            }
        },
        # ------------                                                                                                                                                  
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                       
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.4",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
            },
        },
        # ------------                                                                                                                                                  
        "TightObjWP": {
            "cut_Tight_HWWW": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfIsoId >= 4",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_TightIDIso_DEN_TightID", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022EEv11/cut_TightHWW/",
            },
            "cut_Medium_HWWW": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_mediumId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfIsoId >= 4",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_MediumID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_MediumIDIso_DEN_MediumID", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022EEv11/cut_Medium_HWW/",
            },
            "cut_TightTrkIso_HWWW": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_tkIsoId >= 2",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_TightIDTrkIso_DEN_TightID", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022EEv11/cut_Tight_HWW/",
            },
            "cut_TightMiniIso_HWWW": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_miniIsoId >= 3",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_TightIDMiniIso_DEN_TightID", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022EEv11/cut_Tight_HWW/",
            },
            "cut_Tight_HWWW_tthmva_80": { 
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfIsoId >= 4",
                        "Muon_mvaTTH > 0.8",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_TightID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_TightIDIso_DEN_TightID", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022EEv11/cut_Tight_HWW_tthmva_80/",
            },
            "cut_Medium_HWWW_tthmva_80": {
                "cuts": {
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_mediumId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfIsoId >= 4",
                        "Muon_mvaTTH > 0.8",
                    ],
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": ["NUM_MediumID_DEN_TrackerMuons", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "isoSF": {
                    "1-1": ["NUM_MediumIDIso_DEN_MediumID", "data/scale_factor/Full2022EEv11/muon_scale.json"],
                },
                "fakeW": "data/fake_prompt_rates/Full2022EEv11/cut_Medium_HWW_tthmva_80/",
            },
        },
    }
}
