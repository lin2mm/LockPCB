# Decision 0001 — Architecture and Functional Zoning

- Date: 2026-10-16
- Status: provisional default for first CAD iteration; revisable on measurement/data
- Current product constraints: one 1S cell beside the long PCB; motor/gearbox at top; BLE core. The prior brief says 18650, factory TXT says 18500, and the STEP cell-like geometry is 18 × 50 mm; exact cell remains TBD pending sampled-cell/BOM confirmation. Unknown dimensions stay TBD; no manufacturing claim.

## Options compared

### A. Single 4-layer longitudinal main PCB — recommended first layout target

- **Size:** four layers can carry a continuous RF reference plane and separate motor/power distribution, potentially reducing routing congestion or board elongation. It does not guarantee minimum board width; actual module and keepout dimensions decide.
- **Power:** supports a clearer motor-current region and logic/RF return strategy. Motor pulses still couple through cell impedance and ground; topology must be measured/calculated from data.
- **Reliability:** fewer board-to-board connectors and fewer assembly interfaces.
- **Supply/manufacturing:** more PCB cost than 2-layer, but a common four-layer process is widely available; actual fab and impedance rules TBD.
- **Risk:** if the available width is extremely small, plane/via/connector and antenna requirements may still make the placement impossible.

### B. Single 2-layer board

- **Size/cost:** lowest layer cost, but routing and return paths may force extra width or longer routing.
- **Power/RF:** harder to preserve uninterrupted RF reference and isolate motor current.
- **Reliability/supply:** simpler supply and fewer stackup specifications.
- **Decision:** fallback if actual placement and return-path review demonstrates adequate margin; not the first choice because user's soft preference is 4-layer.

### C. Split top motor/power board + control/RF board

- **Size:** frees the control board area but adds connector/cable and may increase total package volume.
- **Power/reliability:** separates switching currents physically; connector/contact resistance and motor transient current become new failure risks.
- **Manufacturing/supply:** two boards and extra assembly operations.
- **Decision:** escalation option only if the single-board mechanical envelope fails. No split is committed.

## Provisional functional placement

1. Top end: motor connector, driver, local decoupling, short switched-current loop.
2. Transition region: battery entry, protection/measurement TBD and 3.3-V buck-boost.
3. Far end/outer edge: certified BLE module and its vendor-defined antenna clearance; secure element nearby if approved.
4. Service end/edge: debug/test points and optional expansion connector subject to access constraints.
5. NFC/optional peripherals: optional board/connector only after feature, metal-clearance and I/O requirements are known.

The `.kicad_pcb` contains a four-copper-layer starting stack and illustrative `MOTOR_CURRENT_ZONE`/`RF_SENSITIVE_ZONE` sketches on user layers. These do not establish component placement or RF clearance.

## Motor and logic rail recommendation

Default candidate: low-voltage brushed geared motor on the 1S battery rail through a DRV8213-class H-bridge, and a separate 3.3-V buck-boost for BLE/logic. This avoids boosting the high motor power, but depends on the motor's full voltage range and startup/stall current. If the motor requires a regulated higher voltage, compare a boost rail against a motor with a true 1S range; do not add boost by assumption.
