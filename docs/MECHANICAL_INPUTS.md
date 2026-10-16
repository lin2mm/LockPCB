# Mechanical Inputs — Current Status

This index points to the single current mechanical record: [`MECHANICAL_SOURCE_BASELINE.md`](MECHANICAL_SOURCE_BASELINE.md). It distinguishes designer-confirmed sources from Agent PCB annotations and records the 14 × 50 mm board outline source, the unresolved cell identity, sampled enclosure status, and engineering gates.

## Inputs still required

| Input | Status | Required evidence/action |
|---|---|---|
| Sampled battery SKU | **TBD** (factory TXT says 18500; prior brief says 18650; STEP label/geometry conflict) | Read sample label/BOM; capture installed length/diameter, sleeve, terminals and protection. |
| Battery contacts | **TBD** | Confirm polarity, material/plating, preload, current, screw/washer stack, insulation and short-circuit protection. |
| PCB contour and datums | Source-derived 14 × 50 mm contour is in KiCad; native-mm datum check still open | Verify against clean native source/export before drills/pads or fabrication outputs. |
| Enclosure variant and assembly datums | User confirms designer parts sampled and assembled | Match exact CAD variant/revision to sample; establish coordinate transform from physical assembly. |
| Motor, gearbox and shaft | **TBD** | Obtain exact model, envelope, mounting face, output axis, coupler, voltage/current/torque and stall limits. |
| Metal and RF/NFC regions | **TBD** | Derive from selected assembled CAD/material and antenna/coil data. |
| Tolerance and clearance stack | **Not verified** | Measure/inspect board, cell, contacts, motor, walls, cover travel and assembly tolerances in one datum system. |

## Mandatory KiCad labels

`BATTERY_KEEP_OUT`, `BATTERY_CONTACT_ZONE`, `PCB_MAX_OUTLINE`, `MOTOR_GEARBOX_ZONE`, `SHAFT_AXIS`, `NFC_ANTENNA_ZONE`, `METAL_LOCKBODY_ZONE`, `SERVICE_ACCESS_ZONE`, `NO_COMPONENT_ZONE`.

The current zones are planning annotations, not proven clearances. No product-fit or fabrication claim is made.
