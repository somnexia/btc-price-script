#!/bin/sh
set -eu

python - <<'PY'
import os
import shlex

with open("/tmp/container-env.sh", "w", encoding="utf-8") as env_file:
    for key, value in sorted(os.environ.items()):
        if key.replace("_", "").isalnum():
            env_file.write(f"export {key}={shlex.quote(value)}\n")
PY

cron
tail -f /var/log/cron.log
