#include <iostream>
#include "TString.h"
#include "TFile.h"
#include "TRandom3.h"   
#include <string>
#include <vector>
#include "correction.h"

static TRandom3 rng(125);

std::vector<float> elept_smear_mc(float Lepton_pt, float Electron_r9, float sc_eta)
{
    std::vector<float> result(3);
    float Lepton_newPt = Lepton_pt;
    float smear = elecset_smear->evaluate({"smear", Lepton_pt, Electron_r9, abs(sc_eta)});
    float random_number = rng.Gaus(0.0, 1.0);
    Lepton_newPt = Lepton_pt * (1 + smear * random_number);
    float unc_smear = elecset_smear->evaluate({"esmear", Lepton_pt, Electron_r9, abs(sc_eta)});
    float smearing_up = Lepton_pt * (1 + (smear + unc_smear) * random_number);
    float smearing_down = Lepton_pt * (1 + (smear - unc_smear) * random_number);
    result[0] = Lepton_newPt;
    result[1] = smearing_up;
    result[2] = smearing_down; 
    return result;
}

float elept_scale_data(float Lepton_pt, float Electron_seedGain, float Electron_r9, float run, float sc_eta)
{
    float Lepton_newPt = Lepton_pt;
    float scale = elecset_scale->evaluate({"scale", run, sc_eta, Electron_r9, abs(sc_eta), Lepton_pt, Electron_seedGain});
    Lepton_newPt = scale * Lepton_pt;
    return Lepton_newPt;
}

std::vector<float> elept_scale_mc(float Lepton_pt, float Electron_r9, float sc_eta)
{
    std::vector<float> result(2);
    float Lepton_newPt = Lepton_pt;
    float unc_scale = elecset_scale->evaluate({"escale", Lepton_pt, Electron_r9, abs(sc_eta)});
    result[0] = (1 + unc_scale) * Lepton_newPt;
    result[1] = (1 - unc_scale) * Lepton_newPt;
    return result;
}