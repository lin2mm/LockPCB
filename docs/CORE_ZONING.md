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

- Put motor driver, motor connector and local high-frequency/energy-storage decoupling in the motor-current zone; place the driver to minimize the switched current loop.
- Reserve the farthest available edge from the motor and metalwork for the BLE antenna module; enforce the selected module vendor's full copper/component keepout after module choice.
- Treat battery contact, motor output, charging, debug and optional-module connectors as interfaces requiring retention/strain-relief/access decisions, not just pin-count decisions.
- Keep optional NFC, keypad, fingerprint and Wi-Fi features off the baseline signal/power budget until selected; use a common expansion interface only after I/O, voltage and connector envelope are assessed.
- Do not place NFC antenna over/adjacent to metal based on the current sketch. Required ferrite, coil dimensions, tuning and metal spacing are TBD.

## Alternatives and decision criteria

| Option | Benefits | Risks / cost | Current position |
|---|---|---|---|
| One main board, 4 layers | Few interconnects; best chance of continuous return plane and RF/motor segregation; simple assembly | Higher PCB cost; narrow board may constrain placement, antenna keepout and motor copper; layer stack may not fit the achievable envelope | **Default to evaluate first** |
| One main board, 2 layers | Lower board cost and easier sourcing | Harder return-path/ground continuity and power/RF separation; may widen/lengthen board or complicate routing | Fallback only if placement/routing proves adequate |
| Split motor/power daughterboard at top | Moves high-current loop and connector toward motor; frees RF/control board area | Adds connector, wires/contacts, assembly/volume, reliability and service risks | Escalation option only if single-board mechanical envelope fails |
| Separate optional feature boards | Isolates optional BOM/antenna/feature variants | More interfaces, assembly, and connector/EMI risk | Preferred for optional feature variants if electrical interface is reusable |

## Physical boundaries remain open

18650 cylinder and contact geometry; PCB max width/length/thickness; shell/lockbody metal volume; motor and gearbox envelope; axis datum, coupling and top-end clearance; service access; RF/NFC antenna geometry. All are maintained as TBD in `MECHANICAL_INPUTS.md` and represented as not-to-scale placeholders in KiCad.
