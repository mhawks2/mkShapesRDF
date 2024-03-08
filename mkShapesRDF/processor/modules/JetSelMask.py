from mkShapesRDF.processor.framework.module import Module
import correctionlib
correctionlib.register_pyroot_binding()

class JetSelMask(Module):
    def __init__(self, jetId, puJetId, minPt, maxEta, UL2016fix=False, pathToJson="",globalTag=""):
        super().__init__("JetSelMask")
        self.jetId = jetId
        self.puJetId = puJetId
        self.minPt = minPt
        self.maxEta = maxEta
        self.doMask = True
        self.UL2016fix = UL2016fix
        if pathToJson!="":
            self.doMask = True
            self.pathToJson = pathToJson
            self.globalTag = globalTag
        
    def runModue(self, df, values):
        # jetId = 2
        # wp = "loose"
        # minPt = 15.0
        # maxEta = 4.7
        # UL2016fix = False

        if self.UL2016fix:
            wp_dict = {
                "loose": "(1<<0)",
                "medium": "(1<<1)",
                "tight": "(1<<2)",
            }
        else:
            wp_dict = {
                "loose": "(1<<2)",
                "medium": "(1<<1)",
                "tight": "(1<<0)",
            }
        
        df = df.Define(
            "CleanJetMask",
            f"CleanJet_pt >= {self.minPt} && CleanJet_eta <= {self.maxEta} && Take(Jet_jetId, CleanJet_jetIdx) >= {self.jetId}",
        )

        if self.doMask:

            ROOT.gROOT.ProcessLine(
                f"""
                auto jetMaskFile = correction::CorrectionSet::from_file("{self.pathToJson}");
                correction::Correction::Ref cset_jet_Map = (correction::Correction::Ref) jetMaskFile->at("{self.globalTag}");
                """
            )

            ROOT.gInterpreter.Declare(
                """
                ROOT::RVecB getJetMask(ROOT::RVecF CleanJet_pt,ROOT::RVecF CleanJet_eta, ROOT::RVecF CleanJet_phi, ROOT::RVecF Jet_neEmEF,ROOT::RVecF Jet_chEmEF,ROOT::RVecI CleanJet_jetIdx){
                    float tmp_value;
                    float cleanJet_EM;
                    float eta, phi;
                    RVecB CleanJet_isNotVeto = RVecB(CleanJet_pt.size(), true);
                    for (int i=0; i<CleanJet_pt.size(); i++){
                        phi = ROOT::VecOps::Max(ROOT::RVecF{ROOT::VecOps::Min(ROOT::RVecF{CleanJet_phi[i], 3.1415}), -3.1415});
                        eta = ROOT::VecOps::Max(ROOT::RVecF{ROOT::VecOps::Min(ROOT::RVecF{CleanJet_eta[i], 5.19}), -5.19});
                        
                        cleanJet_EM = Jet_neEmEF[CleanJet_jetIdx[i]] + Jet_chEmEF[CleanJet_jetIdx[i]];
                        tmp_value = cset_jet_Map->evaluate({"jetvetomap", eta, phi});
                    
                        if (cleanJet_EM<0.9 && CleanJet_pt[i]>15.0 && tmp_value!=0.0){
                            CleanJet_isNotVeto[i] = false;
                        }
                    }
                    return CleanJet_isNotVeto;
                }
                """
            )

            ROOT.gInterpreter.Declare(
                """
                bool getEventMask(ROOT::RVecF CleanJet_pt,ROOT::RVecF CleanJet_eta, ROOT::RVecF CleanJet_phi, ROOT::RVecF Jet_neEmEF,ROOT::RVecF Jet_chEmEF,ROOT::RVecI CleanJet_jetIdx){
                    float tmp_value;
                    float cleanJet_EM;
                    float eta,phi;
                    for (int i=0; i<CleanJet_pt.size(); i++){
                        phi = ROOT::VecOps::Max(ROOT::RVecF{ROOT::VecOps::Min(ROOT::RVecF{CleanJet_phi[i], 3.1415}), -3.1415});
                        eta = ROOT::VecOps::Max(ROOT::RVecF{ROOT::VecOps::Min(ROOT::RVecF{CleanJet_eta[i], 5.19}), -5.19});
                        
                        cleanJet_EM = Jet_neEmEF[CleanJet_jetIdx[i]] + Jet_chEmEF[CleanJet_jetIdx[i]];
                        tmp_value = cset_jet_Map->evaluate({"jetvetomap_eep", eta, phi});
                        if (cleanJet_EM<0.9 && CleanJet_pt[i]>15.0 && tmp_value!=0.0){
                            return false;
                        }
                    }
                    return true;
                }
                """
            )

            df = df.Define(
                "CleanJetMask",
                "CleanJetMask && getJetMask(CleanJet_pt,CleanJet_eta,CleanJet_phi,Jet_neEmEF,Jet_chEmEF,CleanJet_jetIdx)"
            )

            df = df.Define(
                "CleanEventMask",
                "getEventMask(CleanJet_pt,CleanJet_eta,CleanJet_phi,Jet_neEmEF,Jet_chEmEF,CleanJet_jetIdx)"
            )

            df = df.Filter("CleanEventMask")
            
        values.append(
            [
                df.Define("test", "CleanJet_pt.size()").Sum("test"),
                "Original size of CleanJet",
            ]
        )

        branches = ["jetIdx", "pt", "eta", "phi", "mass"]
        for prop in branches:
            df = df.Redefine(f"CleanJet_{prop}", f"CleanJet_{prop}[CleanJetMask]")

        df = df.DropColumns("CleanJetMask")

        values.append(
            [
                df.Define("test", "CleanJet_pt.size()").Sum("test"),
                "Final size of CleanJet",
            ]
        )

        return df
