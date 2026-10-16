# Decision 0002 — Candidate Components, BOM and Open Inputs

- Date: 2026-10-16
- Status: all part references are planning placeholders; no MPN, package or footprint approved.

## Candidate comparison

| Block | Default candidate to investigate | Alternatives / trade-off | Selection gate |
|---|---|---|---|
| BLE MCU | Certified nRF52840-based module | Certified module simplifies antenna/RF compliance but may cost/occupy more area and depends on module supply; bare SoC may be smaller but adds RF matching, antenna tuning, RF layout and certification burden | Confirm module outline, antenna keepout, certifications, lifecycle and I/O needs |
| Logic supply | 3.3-V buck-boost | Buck-only may be smaller/efficient if 1S cell never drops below required rail; boost+LDO or buck+boost alternatives depend on load; buck-boost can add quiescent-current/efficiency penalty | Cell range, BLE peak/sleep current, load transient, runtime target |
| Motor driver | DRV8213-class brushed H-bridge | Other H-bridge/current-limit options can be smaller or higher-current; exact device depends on peak/stall pulses, VM range, thermal and protection | Exact motor part, stall current, pulse duration, thermal path and supply range |
| Secure element | ATECC608C-class optional device | Omit initially to save area/power/cost if threat model and provisioning permit; another secure element requires ecosystem/security review | Security requirement, provisioning flow, footprint/package and I2C availability |
| Cell protection/charge | TBD; no charger assumed | Separate protection and optional USB-C charger/power path; protected cell/holder choices can shift volume and cutoff | Exact cell, safe-charge requirement, USB-C yes/no, charge-in-place and thermal limits |
| Optional features | J4 expansion/feature subboards | Direct integrated parts save connector/volume but force a larger main board and variant BOM | User priority, connector envelope/pin budget and RF/metal constraints |

## BOM / pin/net draft rules

- `docs/BOM_DRAFT.csv` lists block references for planning only; every MPN and footprint remains TBD. `U1`–`U4` names are not placed KiCad symbols.
- `docs/PINOUT_DRAFT.csv` uses logical signal names. Specific module pins are deliberately TBD until an exact module is selected.
- `docs/NETLIST_DRAFT.csv` is a block-level connection intent, not a netlist or connected schematic.
- `TP1`–`TP7` are proposed accessible points for VBAT, GND, +3V3, SWDIO, SWCLK, motor-fault and motor-current sense. The latter two are conditional on driver capability; actual test-pad geometry/placement is TBD.
- Prior pin/net records also suggest optional motor fault/current feedback, lock-position and door-state sensing, tamper, and optional NFC/keypad/fingerprint interfaces. These are now represented as logical candidates in `docs/PINOUT_DRAFT.csv` / `docs/NETLIST_DRAFT.csv`; they do not commit features, hardware, pin assignments, or firmware.
- Current designer-source facts and the Agent-derived board outline are recorded only in [`../docs/MECHANICAL_SOURCE_BASELINE.md`](../docs/MECHANICAL_SOURCE_BASELINE.md). Do not infer internal clearance or fit from an external shell envelope.
- The schematic uses annotated block and signal-intent text only. It is not an ERC-cleared electrical circuit; CI reports this status explicitly.

## Six blocking questions (do not invent answers)

1. Exact sampled cell/holder identity (18500 vs 18650) and its mechanical/electrical limits.
2. Maximum PCB length, width and thickness.
3. Motor model, rated voltage, startup and stall current.
4. Motor shaft datum and top gearbox dimensions/coupler.
5. Whether USB-C on-board charging is required.
6. Whether enclosure/lock body contains metal, and where.

Until these are answered, numeric power closure, motor-driver sizing, RF clearance, mechanical fit and manufacturing release remain blocked. Placeholder work continues meanwhile.
