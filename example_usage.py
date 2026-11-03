"""
Example usage of Pulmonary Body Plethysmography Airway Resistance Skill.
Demonstrates normal tracheobronchial conductance vs asthmatic high airway resistance.
"""

import json
from client import BodyPlethysmographyRawClient


def main():
    print("=== Testing Pulmonary Airway Resistance Skill ===")
    client = BodyPlethysmographyRawClient()

    # 1. Healthy young adult subject (Palv = 1.6 cmH2O at flow = 1.0 L/s, TGV = 3.2 L -> Raw = 1.6 cmH2O/(L/s), sRaw = 5.12, sGaw = 0.195 > 0.15)
    res_normal = client.evaluate_airway_mechanics(
        alveolar_pressure_swing_cmh2o=1.6,
        airflow_rate_l_s=1.0,
        thoracic_gas_volume_l=3.2
    )
    print("\n[Case 1: Normal Airway Caliber & Conductance]")
    print(json.dumps(res_normal, indent=2))

    # 2. Patient during acute asthmatic bronchoconstriction (Palv = 4.8 cmH2O at flow = 0.8 L/s, TGV = 4.5 L -> Raw = 6.0 cmH2O/(L/s), sRaw = 27.0, sGaw = 0.037 < 0.10)
    res_asthma = client.evaluate_airway_mechanics(
        alveolar_pressure_swing_cmh2o=4.8,
        airflow_rate_l_s=0.8,
        thoracic_gas_volume_l=4.5
    )
    print("\n[Case 2: Acute Asthmatic Bronchoconstriction / High Raw]")
    print(json.dumps(res_asthma, indent=2))

    # Assertions
    assert res_normal["mechanics"]["airway_resistance_raw_cmh2o_l_s"] <= 2.4
    assert "Normal" in res_normal["clinical_interpretation"]["obstruction_severity"]
    assert res_asthma["mechanics"]["airway_resistance_raw_cmh2o_l_s"] > 4.0
    assert "Significant" in res_asthma["clinical_interpretation"]["obstruction_severity"]
    print("\n[SUCCESS] Body Plethysmography Airway Resistance tests passed!")


if __name__ == "__main__":
    main()
