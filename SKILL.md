---
name: genpark-personal-agent-cardiac-coronary-flow-velocity-reserve-cfvr-skill
version: 1.0.0
description: Calculates Coronary Flow Velocity Reserve (CFVR = V_hyper / V_rest) and Rate-Pressure Product (RPP) to assess coronary microvascular dysfunction (CMD / INOCA).
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - cardiology
  - hemodynamics
  - cfvr
  - coronary-flow
  - cmd
  - zero-dependency
---

# Cardiac Coronary Flow Velocity Reserve (CFVR) Skill

## Mathematical Formulation

Coronary Flow Velocity Reserve ratio:

$$\text{CFVR} = \frac{V_{\text{hyperemic}}}{V_{\text{resting}}}$$

Rate-Pressure Product (RPP, index of myocardial oxygen demand):

$$\text{RPP} = \text{Heart Rate} \, (\text{bpm}) \times \text{Systolic BP} \, (\text{mmHg})$$

Velocity augment:

$$\Delta V = V_{\text{hyperemic}} - V_{\text{resting}} \quad (\text{cm/s})$$

## Clinical Diagnostic Stratification (ESC INOCA Consensus)
- **Normal Coronary Reserve**: $\text{CFVR} \ge 2.5$ (healthy coronary arteriolar reactivity)
- **Borderline Microvascular Reserve**: $2.0 \le \text{CFVR} < 2.5$
- **Coronary Microvascular Dysfunction (CMD)**: $\text{CFVR} < 2.0$ (arteriolar remodeling, endothelial/vascular smooth muscle dysfunction; diagnostic criterion for microvascular angina)
