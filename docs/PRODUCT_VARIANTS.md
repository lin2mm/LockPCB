# Product Variant Strategy — LockPCB

## V1 — current PCB design target

- User-directed first design: one 1S 18650 form factor beside the longitudinal PCB. This is a design target, not an exact cell MPN approval.
- The board's `BATTERY_KEEP_OUT` annotation now shows a provisional 19 × 70 mm planning envelope for an 18650-style protected/packaged cell. It is a graphical mechanical reference only: no KiCad keepout rule, SKU fit, clearance, contact, or safety validation is implied. Replace it with the selected cell's actual maximum dimensions and tolerance allowance.
- The designer factory function note says 18500, and its STEP cell-like node is about 18 × 18 × 50 mm despite the node name. The second CAD folder has matching component IDs but no assembled, dimensioned long-size enclosure in the reviewed contents. See [`CAD_VARIANT_COMPARISON.md`](CAD_VARIANT_COMPARISON.md). Do not claim either enclosure accepts V1 until checked against the physical assembled enclosure and exact CAD revision.

## Future differently-sized series

- A second product series with different dimensions is possible, but its envelope, battery format, PCB outline and interface requirements have not been supplied. It is not part of the current V1 placement.
- Aim for reusable electrical architecture where practical, but do not force one board outline, battery-contact pattern or component placement to fit incompatible mechanical variants. Create a controlled V2 mechanical/BOM variant only after its source CAD and dimensional requirements are confirmed.

## V1 validation gates

1. Select an exact 18650 model; record protected/unprotected dimensions, terminal style, chemistry, current limits and approved supply source.
2. Compare its maximum installed envelope with the selected enclosure CAD variant and physical sample, including contacts, insulation, assembly path and tolerance stack.
3. Recalculate motor-driver, regulator, protection and copper requirements from the selected cell and motor data.
4. Keep the second product series separate until its dimensions are available.

No current CAD fit, electrical safety, runtime or fabrication readiness is claimed.
