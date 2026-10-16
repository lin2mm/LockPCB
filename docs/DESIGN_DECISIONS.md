# Design Decisions — Current Baseline

This file contains only the active project baseline and open decisions. Superseded Agent CAD narratives are not carried forward here. See `docs/MECHANICAL_SOURCE_BASELINE.md` for the source/evidence record.

## Confirmed constraints

- Compact indoor retrofit lock; no drilling or new wiring.
- One 1S cell beside a long PCB; motor/gearing/coupler near the top.
- Current activity is PCB engineering only; no firmware flashing, purchasing, fabrication, or real hardware test.
- Designer-confirmed package contains the submitted prototype drawing/CAD inputs; the designer enclosure parts have been sampled and assembled.
- PCB plan outline is 14 × 50 mm with a notched/stepped contour, based on the confirmed DWG/JPG/STEP; DWG calls out 1.20 mm board thickness and two Ø3.10 mm end holes.

## Active engineering decisions

- Keep KiCad source in the GitHub session branch as the editable PCB source.
- Keep `Edge.Cuts` aligned to the source-derived DWG contour. Do not turn the two hole/ring graphics into actual drill/pad features until polarity, plating, contact hardware and electrical ratings are approved.
- Maintain all nine required mechanical labels as editable KiCad annotations. They communicate intended regions only; they are not verified keepouts or clearance results.
- Keep the 4-layer approach as an evaluation preference, not a frozen stackup. MPNs, footprints and actual electrical connectivity remain open.
- Treat the sampled/assembled enclosure as the mechanical anchor, and identify the exact CAD variant/revision matching it before claiming any fit result.

## Open decisions

- **V1 cell target:** user selected 1S 18650 as the first PCB design basis. Exact SKU and installed envelope remain TBD. Factory TXT says 18500; STEP node `DC-18650-SX` measures about 18 × 18 × 50 mm, so fit to the current factory/sample enclosure is not established. A second size series is deferred.
- **Contacts:** polarity, terminal material/plating, preload, current, screw/washer stack, insulation and protection are TBD.
- **Motor/drive:** motor MPN, operating range, startup/stall current, torque, duty, gearbox and shaft/coupler geometry are TBD.
- **RF/service/metal:** boundaries and antenna keepout require the selected enclosure assembly and module/antenna data.
- **Mechanical validation:** native-mm source/datum cross-check, actual fit and tolerance stack remain open.

No manufacturing release, fit, electrical safety or hardware validation is claimed.
