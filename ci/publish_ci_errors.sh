#!/usr/bin/env bash
# Surface concise failure details as GitHub check annotations (also retained in artifacts).
set -u
if [ ! -f reports/summary.txt ]; then
  echo '::error title=KiCad CI::summary.txt was not produced; inspect runner logs/artifacts.'
  exit 0
fi
while IFS= read -r entry; do
  case "$entry" in
    *_exit_code=*)
      value="${entry##*=}"
      [ "$value" = "0" ] && continue
      name="${entry%%_exit_code=*}"
      echo "::error title=KiCad ${name}::command exited with code ${value}"
      file="reports/${name}.log"
      [ "$name" = "version_gate" ] && file="reports/version-gate.log"
      if [ -f "$file" ]; then
        tail -n 18 "$file" | while IFS= read -r line; do
          line=${line//'%'/'%25'}
          line=${line//$'\r'/'%0D'}
          line=${line//$'\n'/'%0A'}
          echo "::error title=${name} detail::${line}"
        done
      fi
      ;;
  esac
done < reports/summary.txt
