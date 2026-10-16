# Decision 0004 — Agent Recommendations for the Six Blockers

- Date: 2026-10-16
- Status: Agent-proposed working defaults, **not user-confirmed product facts**. Continue placeholder work; replace as soon as sourced data arrives.

## 1. 18650 cell

**Recommend electrical candidate: Molicel INR-18650-P28A**, with Samsung INR18650-30Q as a second-source/capacity alternative after motor-current validation. The high-drain P28A is the safer first electrical evaluation candidate for motor pulses/voltage sag; trade-off is lower capacity than some energy-oriented 18650s and potential distributor/authenticity/supply risk. This is a datasheet/procurement candidate only, not a purchase instruction. Confirm current datasheet, cell authenticity, protection/temperature requirements and second-source compatibility before selection.

For mechanical exploration, use an approximate bare-cell envelope near **18.6 mm diameter × 65.2 mm length**, then add sleeve, tolerances, contacts, retention and insertion/removal clearance. The bare-cell figure is not the holder envelope. Prefer a documented flat-top cell format only if the selected contact/holder and polarity protection require it; protected cell variants can be longer and may trip under motor pulses.

## 2. PCB length, width and thickness

**Recommend keep 17.5 × 60 mm as the nominal first-layout target** (same as current `Edge.Cuts`) and use **20 × 65 mm only as a provisional maximum review envelope**, taken from the upper edge of the original evaluation range. The `PCB_MAX_OUTLINE` user-layer rectangle now denotes that review envelope; it is not a frozen maximum or a fit claim. The enclosure measurement must replace both before any placement freeze.

**Recommend 1.2 mm nominal FR-4 thickness for first stackup discussion**, because it balances a narrow 4-layer board's stiffness/connector support against available internal clearance. Compare 1.0 mm only if the measured enclosure forces it and board support/strain are acceptable; 1.6 mm is a stiffness fallback if the shell permits. Actual core/prepreg, dielectric, copper weight, fab availability and thickness tolerance remain TBD.

## 3. Motor voltage and current

**Recommend a 3 V-class brushed DC geared motor intended for direct use from a single-cell rail**, with an explicitly verified operating range spanning the selected cell's charged and discharged limits. This preserves the simple 1S power tree and avoids a motor boost stage. Do not pick an exact motor or claim DRV8213 compatibility before the motor datasheet is matched.

Measure/obtain winding resistance and startup/stall current at maximum cell voltage, plus peak duration, duty cycle, torque and jam condition. Size the H-bridge, connector, cell and copper from the worst-case pulse and thermal model; as an initial engineering screening rule, select a driver peak rating with at least 1.5× margin over the verified pulse current, then validate its datasheet thermal/current-limit behavior. If no direct-1S motor meets torque/size, compare a higher-voltage motor + boost against a gear-ratio/mechanical change before adopting boost.

## 4. Axis and top gearbox

Do not assign gear teeth/module/center distances until torque, ratio and envelope are defined. Recommend establish a 3D datum scheme now: PCB plane as datum A, a shell/mounting face as datum B, and motor/lock output axis as datum C; dimension the coupling centerline from these datums. Evaluate a **3 mm D-flat output shaft** as a compact, commonly coupled candidate only if selected gearbox torque and shaft strength support it. Compare with the actual lock spindle/coupler; do not cut a shaft or gear from this recommendation.

Request a gearbox outline drawing, reduction ratio, output speed/torque, shaft type/diameter, allowable radial load and mounting face. Keep the top `MOTOR_GEARBOX_ZONE` not-to-scale until then.

## 5. USB-C charging

**Recommend no on-board USB-C charger in the first design iteration by default**, assuming the 18650 remains service-replaceable. Reasons: keeps the narrow board simpler, avoids charger/power-path and thermal/safety complexity, and frees connector/access volume. Preserve optional service pads and an uncommitted charging interface decision in the docs only. Reverse this recommendation if in-situ charging is a product requirement or the cell is not readily replaceable; then evaluate USB-C protection, charge current, thermals, enclosure access and battery protection as a complete subsystem.

## 6. Metal enclosure

**Until measured otherwise, treat nearby lock body/gear hardware as conductive metal for RF/NFC planning.** Keep the BLE antenna at the farthest available edge and plan a non-metallic RF window/antenna cap if the enclosure is metal. Follow the chosen certified module's full keepout and antenna reference layout; numeric separation cannot be set yet. Assume NFC may need a dedicated plastic-faced region and/or ferrite only after coil and shell geometry are known. This is a conservative planning assumption, not a claim the enclosure is actually metal.

## Additional recommendations

- Keep the single-board baseline, but keep the motor/power daughterboard option available if the measured top-end motor envelope or current loop makes the narrow board unrouteable.
- Add cell reverse-polarity/overcurrent/undervoltage and temperature strategy to the architecture before choosing contacts or charger. Do not rely on an unprotected cell without a complete system protection review.
- Ensure motor-control has a hardware-safe disabled/reset state; budget for motor-start brownout and transient recovery so BLE remains stable.
- Use a certified BLE module for Rev-A feasibility; compare its module width and antenna keepout against a bare SoC only if the board envelope makes the module impossible.
- Keep Wi-Fi off the core board by default because its peak power and RF coexistence cost do not serve the BLE-first baseline; use a separate optional module only if later required.
- Keep DNP optional peripherals out of the base power budget. Add accessible VBAT, GND, 3V3 and debug test points; current TP1–TP5 draft already captures these points.
- Revisit all recommendations after the six blockers arrive. No recommendation here authorizes ordering, fabrication or hardware testing.
