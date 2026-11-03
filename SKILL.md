---
name: genpark-personal-agent-pulmonary-airway-resistance-plethysmography-raw-skill
version: 1.0.0
description: Calculates Airway Resistance (Raw in cmH2O/(L/s)), Specific Airway Resistance (sRaw), and Specific Airway Conductance (sGaw) via body plethysmography.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - pulmonary
  - airway-resistance
  - plethysmography
  - raw
  - sgaw
  - zero-dependency
---

# Pulmonary Airway Resistance (Raw) Plethysmography Skill

## Mathematical Formulation

Airway Resistance from body plethysmography:

$$R_{\text{aw}} = \frac{\Delta P_{\text{alv}}}{\Delta \dot{V}} \quad \left(\frac{\text{cmH}_2\text{O}}{\text{L/s}}\right)$$

Specific Airway Resistance:

$$sR_{\text{aw}} = R_{\text{aw}} \times \text{TGV} \quad (\text{cmH}_2\text{O} \cdot \text{s})$$

Specific Airway Conductance:

$$sG_{\text{aw}} = \frac{1}{sR_{\text{aw}}} = \frac{1}{R_{\text{aw}} \times \text{TGV}} \quad \left(\frac{1}{\text{cmH}_2\text{O} \cdot \text{s}}\right)$$

Where $\text{TGV}$ is the thoracic gas volume at end-expiratory resting lung volume.

## Clinical Severity Classification
- **Normal Airway Mechanics**: $R_{\text{aw}} \le 2.4\text{ cmH}_2\text{O}/(\text{L/s})$, $sG_{\text{aw}} \ge 0.15\text{ s}^{-1} \cdot \text{cmH}_2\text{O}^{-1}$
- **Mild Obstruction**: $R_{\text{aw}} \in [2.5, 4.0]$, $sG_{\text{aw}} \in [0.10, 0.14]$
- **Significant / Severe Airway Obstruction**: $R_{\text{aw}} > 4.0\text{ cmH}_2\text{O}/(\text{L/s})$ or $sG_{\text{aw}} < 0.10$ (asthma attack, COPD exacerbation, central stenosis)
