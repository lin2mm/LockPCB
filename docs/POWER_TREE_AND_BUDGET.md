# 1S Power Tree & First-Pass Budget (TBD)

Status: architecture proposal, not an approved electrical design. No components or electrical pins are placed in the schematic yet. All current draw, voltage limits, efficiency, cell capacity, and thermal values remain TBD until the selected cell, motor, and module datasheets are available.

## Recommended starting power tree

```text
1S 18650 (evaluate Molicel INR-18650-P28A; exact cell TBD)
  ├─ cell/contact/protection strategy (polarity, overcurrent, undervoltage TBD)
  │   ├─ VBAT_1S ──> motor driver candidate ──> brushed geared motor (direct battery rail preferred)
  │   │                 └─ optional fault/current feedback to BLE MCU, subject to driver capability
  │   └─ VBAT_1S ──> 3.3 V buck-boost candidate ──> certified BLE module + logic + optional secure element
  │                                     └─ optional lock/door/tamper sensor and NFC/expansion interfaces
  └─ optional charge input: USB-C only if user confirms; charger/power-path TBD
```

**Default recommendation:** retain a 1S battery rail, evaluate a low-voltage brushed DC gearmotor and driver that can operate directly from VBAT, and use a dedicated 3.3 V buck-boost rail for BLE/logic. Evaluate a high-drain cell such as Molicel P28A against a capacity-oriented 30Q alternative once current needs and authentic sourcing are checked. Default to no on-board USB-C charging in the first architecture unless in-device charging is a product requirement. Do not select the converter, driver, protection device, or charger until peak and sleep loads and electrical ratings are known. Direct motor drive avoids a high-power motor boost converter but makes motor voltage range, brownout, current peaks, and EMI constraints decisive.

## Budget equations (no invented load values)

| Budget item | Current estimate | Design relation / required input |
|---|---:|---|
| Cell usable capacity | TBD | Datasheet capacity at actual discharge rate, cutoff, temperature, and aging |
| Sleep / BLE standby | TBD | `I_logic_sleep = module + secure element + sensors + regulator quiescent current` |
| BLE active / advertising | TBD | `I_logic_peak = module RF peak + other active logic`; duty cycle TBD |
| Motor startup / stall | TBD | Must use motor datasheet and driver limit; `I_motor_peak` is currently the dominant unknown |
| Buck-boost output | TBD | `P_3V3 = 3.3 V × I_3V3`; output peak and transient response TBD |
| Battery-side converter input | TBD | `I_conv_in ≈ (3.3 V × I_3V3)/(η × V_bat)`; η and operating Vbat range TBD |
| Combined battery peak | TBD | Conservatively evaluate `I_bat_peak = I_motor_peak + I_conv_in_peak + other loads`, including startup coincidence |
| Runtime | TBD | `t ≈ C_usable / I_bat_avg`; requires duty-cycle, cell, converter, and motor measurements/specifications |
| Thermal / copper drop | TBD | Check driver, cell contacts, connector, and copper against stall/start pulse duration and repetition |

A provisional 1S Li-ion voltage envelope is **not** frozen here. Confirm the selected 18650 chemistry, protection and operating limits before setting undervoltage, converter input, or motor-voltage requirements. Do not infer a runtime from nominal cell capacity alone.

## Power integrity and layout assumptions

- Keep motor-current switching loop, driver, local bulk/ceramic decoupling, and motor connector together in the motor-current region.
- Keep the RF module/antenna edge and its documented ground/clearance environment away from motor switching nodes, motor wiring, and the cell/metal lock body as far as the verified outline permits.
- The proposed 4-layer stack is a starting point only: F.Cu component/signal, In1.Cu continuous reference ground candidate, In2.Cu power/low-speed routing candidate, B.Cu signals. Final layer usage depends on a placement/return-current review.
- Do not split reference planes under RF or fast edges without an explicit return-path analysis. Motor return-current routing must not cross the RF return/reference region.
- If the required mechanical dimensions do not permit separation on one board, compare a compact top motor/power daughterboard against a single board; connector reliability, added volume, wire/connector loss, assembly and serviceability must be weighed.

## Open inputs blocking numeric power closure

Exact 18650 model; motor part number/rated voltage/start and stall current; driver current/thermal rating and available fault/current-sense outputs; BLE module peak and sleep consumption; selected sensor/accessory functions; charge/USB-C requirement; regulator efficiency at the real load; cell/pack protection and cutoff policy. Until then, no numerical battery budget, runtime claim, current rating, or BOM MPN is released.

The dated pre-CAD archive and earlier CAD handoff include historical estimates and candidate blocks, but they are not datasheet-verified load data for the current product. Those numbers are intentionally not carried into this active budget. Only the equation-based budget above is current.
