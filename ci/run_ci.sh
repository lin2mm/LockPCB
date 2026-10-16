#!/usr/bin/env bash
# Run every check, retain each actual exit code, and fail the job if any check fails.
set -u
mkdir -p reports/render
status=0
run() {
  local name="$1"; shift
  echo "===== ${name}: $* ====="
  "$@" >"reports/${name}.log" 2>&1
  local rc=$?
  cat "reports/${name}.log"
  echo "${name}_exit_code=${rc}" | tee -a reports/summary.txt
  if [ "$rc" -ne 0 ]; then status=1; fi
}
: > reports/summary.txt

run version kicad-cli version
python3 ci/check_kicad_major.py reports/version.log 8 > reports/version-gate.log 2>&1
rc=$?
cat reports/version-gate.log
echo "version_gate_exit_code=${rc}" | tee -a reports/summary.txt
if [ "$rc" -ne 0 ]; then status=1; fi

run erc kicad-cli sch erc --exit-code-violations --output reports/erc.rpt pcb/LockPCB.kicad_sch
run drc kicad-cli pcb drc --exit-code-violations --output reports/drc.rpt pcb/LockPCB.kicad_pcb
run netlist_export kicad-cli sch export netlist --output reports/LockPCB.net pcb/LockPCB.kicad_sch
run schematic_svg kicad-cli sch export svg --output reports/render/schematic pcb/LockPCB.kicad_sch
run pcb_svg kicad-cli pcb export svg --layers "F.Cu,In1.Cu,In2.Cu,B.Cu,Edge.Cuts,User.1,User.2,User.3,User.4,User.5,User.6,User.7,User.8,User.9,User.Comments,Eco1.User,Eco2.User" --output reports/render/pcb pcb/LockPCB.kicad_pcb
run pcb_structure python3 ci/check_pcb_structure.py pcb/LockPCB.kicad_pcb reports/pcb-structure.txt
run schematic_intent_and_unconnected python3 ci/check_design_intent.py --schematic pcb/LockPCB.kicad_sch --bom docs/BOM_DRAFT.csv --nets docs/NETLIST_DRAFT.csv --netlist reports/LockPCB.net --report reports/design-intent.txt

if [ "$status" -ne 0 ]; then
  echo "overall=FAIL (one or more checks failed; see per-check reports)" | tee -a reports/summary.txt
  exit 1
fi
echo "overall=PASS (PRE-CAD limitations are explicitly reported)" | tee -a reports/summary.txt
