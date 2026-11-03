# Cardiac Coronary Flow Velocity Reserve (CFVR) Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Coronary Flow Velocity Reserve ($\text{CFVR} = V_{\text{hyper}} / V_{\text{rest}}$) and Rate-Pressure Product (RPP) to diagnose coronary microvascular dysfunction (CMD / INOCA).

## Architecture

```mermaid
flowchart TD
    A[LAD Transthoracic Doppler Baseline] --> B[Measure Resting Peak Diastolic Velocity V_rest]
    B --> C[Adenosine Infusion & Measure Hyperemic Velocity V_hyper]
    C --> D[Compute CFVR Ratio = V_hyper / V_rest]
    D --> E[Compute Rate-Pressure Product RPP]
    E --> F[Classify Normal >= 2.5 vs CMD < 2.0]
```

## Quickstart

```python
from client import CoronaryFlowVelocityReserveClient

client = CoronaryFlowVelocityReserveClient()
result = client.evaluate_cfvr(
    resting_diastolic_velocity_cm_s=22.0,
    hyperemic_diastolic_velocity_cm_s=68.0,
    resting_heart_rate_bpm=68.0,
    resting_systolic_bp_mmhg=118.0
)
print(result)
```

## License

Apache-2.0
