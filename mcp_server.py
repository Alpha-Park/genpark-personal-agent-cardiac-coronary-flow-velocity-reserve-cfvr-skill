"""
MCP Server for Cardiac Coronary Flow Velocity Reserve (CFVR) Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import CoronaryFlowVelocityReserveClient


def main():
    client = CoronaryFlowVelocityReserveClient()

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
                            "name": "evaluate_cfvr",
                            "description": "Calculates Coronary Flow Velocity Reserve (CFVR = V_hyper / V_rest) and Rate-Pressure Product (RPP) to assess coronary microvascular dysfunction (CMD / INOCA).",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "resting_diastolic_velocity_cm_s": {
                                        "type": "number",
                                        "description": "Baseline resting peak diastolic velocity in cm/s."
                                    },
                                    "hyperemic_diastolic_velocity_cm_s": {
                                        "type": "number",
                                        "description": "Maximal hyperemic peak diastolic velocity during adenosine in cm/s."
                                    },
                                    "resting_heart_rate_bpm": {
                                        "type": "number",
                                        "description": "Resting heart rate in bpm (default: 70.0)."
                                    },
                                    "resting_systolic_bp_mmhg": {
                                        "type": "number",
                                        "description": "Resting systolic blood pressure in mmHg (default: 120.0)."
                                    },
                                    "coronary_artery_segment": {
                                        "type": "string",
                                        "description": "Coronary vessel examined (default: distal LAD)."
                                    }
                                },
                                "required": [
                                    "resting_diastolic_velocity_cm_s",
                                    "hyperemic_diastolic_velocity_cm_s"
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

            if name == "evaluate_cfvr":
                try:
                    out = client.evaluate_cfvr(**args)
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
