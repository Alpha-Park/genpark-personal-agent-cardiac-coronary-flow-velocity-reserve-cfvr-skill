"""
Cardiac Coronary Flow Velocity Reserve (CFVR) Client.
Zero-mock pure Python standard library implementation.
Calculates Coronary Flow Velocity Reserve (CFVR = V_hyper / V_rest),
Rate-Pressure Product (RPP), and stratifies Coronary Microvascular Dysfunction (CMD).
"""

import math
from typing import Dict, Any, Optional


class CoronaryFlowVelocityReserveClient:
    """
    Evaluates epicardial and coronary microvascular vasodilatory capacity via transthoracic Doppler:
    - V_rest (cm/s): baseline peak diastolic coronary flow velocity in LAD
    - V_hyper (cm/s): maximal hyperemic peak diastolic coronary flow velocity during adenosine
    - CFVR: V_hyper / V_rest
    - Rate-Pressure Product (RPP): Heart Rate * Systolic BP (hemodynamic myocardial oxygen demand)
    """

    def __init__(self):
        pass

    def evaluate_cfvr(
        self,
        resting_diastolic_velocity_cm_s: float,
        hyperemic_diastolic_velocity_cm_s: float,
        resting_heart_rate_bpm: Optional[float] = 70.0,
        resting_systolic_bp_mmhg: Optional[float] = 120.0,
        coronary_artery_segment: Optional[str] = "distal LAD"
    ) -> Dict[str, Any]:
        """
        Calculates CFVR parameters.
        resting_diastolic_velocity_cm_s: baseline velocity (15 to 45 cm/s).
        hyperemic_diastolic_velocity_cm_s: adenosine velocity (35 to 120 cm/s).
        resting_heart_rate_bpm, resting_systolic_bp_mmhg: for RPP workload estimation.
        """
        if resting_diastolic_velocity_cm_s <= 0 or hyperemic_diastolic_velocity_cm_s <= 0:
            raise ValueError("Coronary blood flow velocities must be strictly positive.")
        if hyperemic_diastolic_velocity_cm_s < resting_diastolic_velocity_cm_s:
            raise ValueError("Hyperemic velocity cannot be lower than baseline resting velocity.")

        # CFVR ratio
        cfvr = hyperemic_diastolic_velocity_cm_s / resting_diastolic_velocity_cm_s

        # Rate-Pressure Product (RPP in bpm*mmHg)
        rpp = resting_heart_rate_bpm * resting_systolic_bp_mmhg

        # Absolute velocity delta
        velocity_delta_cm_s = hyperemic_diastolic_velocity_cm_s - resting_diastolic_velocity_cm_s

        # Clinical microvascular dysfunction staging (ESC INOCA Guidelines):
        # CFVR >= 2.5: Normal Coronary Vasomotor Capacity (healthy microcirculation)
        # CFVR 2.0 - 2.49: Borderline Coronary Flow Reserve / Mild Microvascular Impairment
        # CFVR < 2.0: Definite Coronary Microvascular Dysfunction (CMD) / Ischemia with Non-Obstructive Coronary Arteries (INOCA)
        if cfvr >= 2.5:
            microvascular_status = "Preserved Coronary Flow Reserve / Normal Microvascular Function"
            clinical_risk = "Robust arteriolar vasodilatory reserve; low probability of microvascular angina."
        elif cfvr >= 2.0:
            microvascular_status = "Borderline Coronary Vasomotor Reserve"
            clinical_risk = "Subclinical microvascular impairment; consider lifestyle optimization and statin/ACE-i therapy."
        else:
            microvascular_status = "Impaired Coronary Flow Reserve (CMD / INOCA)"
            clinical_risk = "Significant arteriolar remodeling or endothelial/smooth-muscle dysfunction; high prognostic risk for MACE."

        return {
            "status": "success",
            "hemodynamic_velocities": {
                "resting_diastolic_velocity_cm_s": round(resting_diastolic_velocity_cm_s, 1),
                "hyperemic_diastolic_velocity_cm_s": round(hyperemic_diastolic_velocity_cm_s, 1),
                "velocity_delta_cm_s": round(velocity_delta_cm_s, 1),
                "coronary_flow_velocity_reserve_cfvr": round(cfvr, 2)
            },
            "myocardial_workload": {
                "rate_pressure_product_rpp": round(rpp, 0),
                "resting_heart_rate_bpm": resting_heart_rate_bpm,
                "resting_systolic_bp_mmhg": resting_systolic_bp_mmhg,
                "artery_segment": coronary_artery_segment
            },
            "clinical_interpretation": {
                "microvascular_status": microvascular_status,
                "prognostic_risk": clinical_risk
            }
        }
