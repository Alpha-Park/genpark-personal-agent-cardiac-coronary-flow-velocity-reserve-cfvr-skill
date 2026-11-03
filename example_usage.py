"""
Example usage of Cardiac Coronary Flow Velocity Reserve (CFVR) Skill.
Demonstrates normal coronary microvascular reserve vs severe coronary microvascular dysfunction (CMD).
"""

import json
from client import CoronaryFlowVelocityReserveClient


def main():
    print("=== Testing Cardiac Coronary Flow Velocity Reserve Skill ===")
    client = CoronaryFlowVelocityReserveClient()

    # 1. Healthy adult subject with robust coronary reserve (Resting V = 22.0 cm/s, Hyperemic V = 68.0 cm/s -> CFVR = 3.09 >= 2.5)
    res_normal = client.evaluate_cfvr(
        resting_diastolic_velocity_cm_s=22.0,
        hyperemic_diastolic_velocity_cm_s=68.0,
        resting_heart_rate_bpm=68.0,
        resting_systolic_bp_mmhg=118.0
    )
    print("\n[Case 1: Normal Coronary Vasomotor Capacity]")
    print(json.dumps(res_normal, indent=2))

    # 2. Patient with microvascular angina / CMD (Resting V = 26.0 cm/s, Hyperemic V = 42.0 cm/s -> CFVR = 1.62 < 2.0)
    res_cmd = client.evaluate_cfvr(
        resting_diastolic_velocity_cm_s=26.0,
        hyperemic_diastolic_velocity_cm_s=42.0,
        resting_heart_rate_bpm=74.0,
        resting_systolic_bp_mmhg=132.0
    )
    print("\n[Case 2: Coronary Microvascular Dysfunction (CMD / INOCA)]")
    print(json.dumps(res_cmd, indent=2))

    # Assertions
    assert res_normal["hemodynamic_velocities"]["coronary_flow_velocity_reserve_cfvr"] >= 2.5
    assert "Preserved" in res_normal["clinical_interpretation"]["microvascular_status"]
    assert res_cmd["hemodynamic_velocities"]["coronary_flow_velocity_reserve_cfvr"] < 2.0
    assert "Impaired" in res_cmd["clinical_interpretation"]["microvascular_status"]
    print("\n[SUCCESS] Coronary Flow Velocity Reserve tests passed!")


if __name__ == "__main__":
    main()
