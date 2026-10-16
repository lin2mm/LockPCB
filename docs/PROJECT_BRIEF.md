# Project Brief — LockPCB

## Product and scope

- Product: compact indoor retrofit smart lock; installation must not require drilling or new wiring.
- Mechanical concept: one vertical single-cell lithium battery beside a long PCB; motor, reduction gearing and coupler near the top.
- Power architecture: the current PCB variant (V1) is directed to use one 1S 18650 form factor. Exact cell MPN, chemistry, protection, contacts and installed envelope remain TBD. Factory functional TXT says 18500 and STEP node `DC-18650-SX` measures about 18 × 18 × 50 mm; treat this as a source/sample size conflict, not as a change to the V1 target.
- BLE is the primary wireless direction; NFC/keypad/fingerprint and other interfaces remain optional unless explicitly confirmed by the factory package or product owner. A second product series with different dimensions is possible, but its geometry is not yet defined and is not part of V1 placement.
- Current work is PCB engineering only. No firmware flashing, purchasing, fabrication, or real hardware testing.
- Unknown dimensions, MPNs, footprints, electrical ratings, and tolerances remain TBD. Do not claim fit, safety, or fabrication readiness.

## Designer-confirmed mechanical inputs

- All eight files in Drive folder `锁-PCB-外壳设计稿-260729` are designer-confirmed prototype documents already sent to the factory for sampling. Designer-provided ZIPs containing CAD/DWG/STEP are also confirmed source packages.
- Designer enclosure parts have been sampled and assembled; the physical assembly is the mechanical anchor for PCB fit work.
- DWG/JPG/STEP support a notched 14 × 50 mm PCB plan envelope. The DWG calls out 1.20 mm board thickness and two Ø3.10 mm end holes.
- Exact datum mapping, conversion warning, cell identity discrepancy, and distinction between source drawing geometry and Agent board implementation are recorded in [`MECHANICAL_SOURCE_BASELINE.md`](MECHANICAL_SOURCE_BASELINE.md).

## Current Agent PCB state

- KiCad `Edge.Cuts` contains the source-derived notched board outline; hole/ring references are graphical only and do not define manufactured holes, copper pads or polarity.
- Required annotations: `BATTERY_KEEP_OUT`, `BATTERY_CONTACT_ZONE`, `PCB_MAX_OUTLINE`, `MOTOR_GEARBOX_ZONE`, `SHAFT_AXIS`, `NFC_ANTENNA_ZONE`, `METAL_LOCKBODY_ZONE`, `SERVICE_ACCESS_ZONE`, `NO_COMPONENT_ZONE`.
- Functional zones and block-level electrical architecture are Agent engineering placeholders. The PCB has no components, pads, nets, copper pours or routing; the schematic is text-only intent.
- A four-layer stack is a starting preference for evaluation, not a frozen fabrication stackup.

## Engineering gates

1. Map the selected designer CAD revision to the sampled assembly and establish datums.
2. Verify the source-derived outline/holes against clean native-mm CAD before manufacturing-feature implementation.
3. Select a specific 18650 SKU and verify its installed envelope, protection and contact design; obtain motor/gearbox, shaft and current/torque data.
4. Establish actual component, antenna and service clearances with the physical assembly and tolerance stack.
5. Complete real schematic pins/nets, component selection, pad/drill definitions, routing, and DRC/manufacturing review only after the required inputs are confirmed.
