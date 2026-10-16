# Core Board Functional Zoning — Placeholder

## Default recommendation

Try to keep a **single longitudinal 4-layer main PCB** first. This minimizes board-to-board connectors and assembly interfaces. Use the 4-layer stack as a soft preference, not a constraint: hold all copper/placement geometry until the real envelope, motor current, certified module outline, and antenna clearance are known.

```text
TOP / DRIVE END (mechanical TBD)
┌───────────────────────────────┐
│ Motor connector + H-bridge     │  MOTOR_CURRENT_ZONE (top end)
│ motor pulse-current loop       │  driver/decoupling close; details TBD
├───────────────────────────────┤
│ Power entry + 3V3 buck-boost   │  transition / power region
├───────────────────────────────┤
│ BLE module + antenna edge      │  RF_SENSITIVE_ZONE (far from motor)
│ optional secure element        │  NFC/metal clearance TBD
├───────────────────────────────┤
│ service/debug/optional headers │  access direction TBD
└───────────────────────────────┘
BOTTOM / SERVICE END
```

The drawing is a logical sequence only, not a measured layout. The current board placeholder has the required mechanical zone names on KiCad user layers; `Eco1.User` and `Eco2.User` additionally sketch the motor-current and RF-sensitive functional regions. Their shapes are illustrative and must not be used as placement or RF rules without mechanical/radio input confirmation.

## Separation and interfaces

- Put motor driver, motor connector and local high-frequency/energy-storage decoupling in the motor-current zone; place the driver to minimize the switched current loop. Keep a hardware-default-disabled motor control path and expose driver fault/current feedback only if the selected driver provides a suitable interface.
- For V1, reserve the battery interface for an 18650 cell; exact MPN, maximum envelope, polarity/overcurrent protection, contacts and measurement path remain TBD. Keep any future size-series variant mechanically separate until its requirements are known.
- Reserve the farthest available edge from the motor and metalwork for the BLE antenna module; enforce the selected module vendor's full copper/component keepout after module choice.
- Retain logical interface options for lock-position and door-state sensing, plus tamper input. Sensor type, magnet/target location, external wiring, power state and voltage are not selected; keep these as interface candidates rather than placing components now.
- Treat battery contact, motor output, charging, debug, sensor, NFC antenna and optional-module connectors as interfaces requiring retention/strain-relief/access/protection decisions, not just pin-count decisions. Consider ESD protection only after exposed connector use and the transient environment are defined.
- Keep optional NFC, keypad, fingerprint and Wi-Fi features off the baseline signal/power budget until selected; use a common expansion interface only after I/O, voltage and connector envelope are assessed. Wi-Fi remains a daughterboard-only option outside the baseline.
- Do not place NFC antenna over/adjacent to metal based on the current sketch. Required ferrite, coil dimensions, tuning and metal spacing are TBD.
- Include accessible VBAT, GND, 3V3, debug, and—if the chosen driver supports them—motor-fault/current-sense test access in the later component-level placement review.

## Alternatives and decision criteria

| Option | Benefits | Risks / cost | Current position |
|---|---|---|---|
| One main board, 4 layers | Few interconnects; best chance of continuous return plane and RF/motor segregation; simple assembly | Higher PCB cost; narrow board may constrain placement, antenna keepout and motor copper; layer stack may not fit the achievable envelope | **Default to evaluate first** |
| One main board, 2 layers | Lower board cost and easier sourcing | Harder return-path/ground continuity and power/RF separation; may widen/lengthen board or complicate routing | Fallback only if placement/routing proves adequate |
| Split motor/power daughterboard at top | Moves high-current loop and connector toward motor; frees RF/control board area | Adds connector, wires/contacts, assembly/volume, reliability and service risks | Escalation option only if single-board mechanical envelope fails |
| Separate optional feature boards | Isolates optional BOM/antenna/feature variants | More interfaces, assembly, and connector/EMI risk | Preferred for optional feature variants if electrical interface is reusable |

## Physical boundaries remain open

V1 18650 target; exact cell/contact envelope remains TBD; potential V2 series dimensions are TBD; PCB max width/length/thickness; shell/lockbody metal volume; motor and gearbox envelope; axis datum, coupling and top-end clearance; service access; RF/NFC antenna geometry. All remain TBD in `MECHANICAL_INPUTS.md` and are planning annotations in KiCad.
