#include <iostream>
#include <cmath>

using namespace std;

// This macro is used to compute the supercluster eta for electrons and photons as described here: 
// https://twiki.cern.ch/twiki/bin/view/CMS/EgammaNanoAOD#How_to_get_photon_supercluster_e

float scEta(float eta, float phi, float PV_x, float PV_y, float PV_z) 
{

    float tg_theta_over_2 = exp(-eta);
    float tg_theta = 2 * tg_theta_over_2 / (1 - tg_theta_over_2 * tg_theta_over_2);
    float tg_sctheta;
    if (abs(eta) <= 2.5) 
    {
        float R = 130;
        float angle_x0_y0 = 0;
        if (PV_x > 0) angle_x0_y0 = atan(PV_y / PV_x);
        else if (PV_x < 0) angle_x0_y0 = M_PI + atan(PV_y / PV_x);
        else if (PV_y > 0) angle_x0_y0 = M_PI / 2;
        else angle_x0_y0 = -M_PI / 2;
        float alpha = angle_x0_y0 + (M_PI - phi);
        float sin_beta = sqrt(PV_x * PV_x + PV_y * PV_y) / R * sin(alpha);
        float beta = abs(asin(sin_beta));
        float gamma = M_PI / 2 - alpha - beta;
        float l = sqrt(R * R + (PV_x * PV_x + PV_y * PV_y) - 2 * R * sqrt(PV_x * PV_x + PV_y * PV_y) * cos(gamma));
        float z0_zSC = l / tg_theta;
        tg_sctheta = R / (PV_z + z0_zSC);
    } 
    else if (abs(eta) > 2.5) 
    {
        float intersection_z = (eta > 0) ? 310 : -310;
        float base = intersection_z - PV_z;
        float r = base * tg_theta;
        float crystalX = PV_x + r * cos(phi);
        float crystalY = PV_y + r * sin(phi);
        tg_sctheta = sqrt(crystalX * crystalX + crystalY * crystalY) / intersection_z;
    } 
    else 
    {
        return eta;
    }
    float sctheta = atan(tg_sctheta);
    if (sctheta < 0) sctheta += M_PI;
    float tg_sctheta_over_2 = tan(sctheta / 2);
    float SCEta = -log(tg_sctheta_over_2);
    //cout << "Computed SCEta: " << SCEta << endl;
    return SCEta;
}
