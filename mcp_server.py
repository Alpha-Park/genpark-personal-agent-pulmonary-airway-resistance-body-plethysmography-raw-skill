"""
MCP Server for Pulmonary Body Plethysmography Airway Resistance Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import BodyPlethysmographyRawClient


def main():
    client = BodyPlethysmographyRawClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_airway_mechanics",
                            "description": "Calculates Airway Resistance (Raw in cmH2O/(L/s)), Specific Airway Resistance (sRaw), and Specific Airway Conductance (sGaw) via body plethysmography.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "alveolar_pressure_swing_cmh2o": {
                                        "type": "number",
                                        "description": "Alveolar pressure swing delta Palv in cmH2O."
                                    },
                                    "airflow_rate_l_s": {
                                        "type": "number",
                                        "description": "Airflow rate delta V_dot in L/s."
                                    },
                                    "thoracic_gas_volume_l": {
                                        "type": "number",
                                        "description": "Thoracic gas volume (TGV/FRC_pleth) in Liters."
                                    },
                                    "barometric_pressure_mmhg": {
                                        "type": "number",
                                        "description": "Barometric pressure in mmHg (default: 760.0)."
                                    }
                                },
                                "required": [
                                    "alveolar_pressure_swing_cmh2o",
                                    "airflow_rate_l_s",
                                    "thoracic_gas_volume_l"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_airway_mechanics":
                try:
                    out = client.evaluate_airway_mechanics(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
