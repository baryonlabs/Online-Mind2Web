#!/usr/bin/env bash
# KR benchmark environment setup for macOS.
#
# Usage:
#   bash script/setup_macos.sh
#
# This script:
#   1. Creates a Python venv
#   2. Installs requirements + websockets
#   3. Copies config template
#   4. Verifies KR tasks are generated
#   5. Prints next steps

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  KR Benchmark — macOS Setup                                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"

# 1. Python venv
VENV=".venv-kr"
if [ ! -d "$VENV" ]; then
    echo "→ Creating Python venv ($VENV)..."
    python3 -m venv "$VENV"
fi
source "$VENV/bin/activate"
echo "→ Upgrading pip..."
pip install --quiet --upgrade pip

# 2. Install dependencies
echo "→ Installing requirements..."
pip install --quiet -r requirements.txt
pip install --quiet websockets

# 3. Config
if [ ! -f "config.local.json" ]; then
    echo "→ Copying config template..."
    cp config.json.example config.local.json
    echo "  ⚠ Edit config.local.json with your bus/token/brain/openai key"
else
    echo "→ config.local.json already exists (skipping)"
fi

# 4. Generate KR task IDs if needed
TASK_COUNT=$(ls -1 data/kr/tasks/*.json 2>/dev/null | wc -l | tr -d ' ')
if [ "$TASK_COUNT" -eq 0 ]; then
    echo "→ Generating KR task IDs..."
    python3 script/gen_kr_task_ids.py --write
    TASK_COUNT=$(ls -1 data/kr/tasks/*.json | wc -l | tr -d ' ')
fi
echo "→ KR tasks: $TASK_COUNT"

# 5. Verify adapter
echo "→ Verifying WebClaw adapter..."
python3 -c "
import sys; sys.path.insert(0, 'src')
from kr.webclaw_adapter import WebclawFrame, frames_to_v2
doc = frames_to_v2('test', 'abc', 5, [], 'done')
assert doc['schema_version'] == 'online-mind2web-v2'
print('  ✓ Adapter OK')
"

# 6. Stats
echo ""
echo "→ KR benchmark stats:"
python3 script/kr_stats.py

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  Setup complete!                                             ║"
echo "║                                                              ║"
echo "║  Next steps:                                                 ║"
echo "║  1. Edit config.local.json with your credentials             ║"
echo "║  2. Load WebClaw Chrome extension + patches                  ║"
echo "║  3. Start DureClaw bus + brain LLM                           ║"
echo "║  4. Run benchmark:                                           ║"
echo "║     source .venv-kr/bin/activate                             ║"
echo "║     python3 script/run_benchmark.py                          ║"
echo "║                                                              ║"
echo "║  Or run a subset:                                            ║"
echo "║     python3 script/run_benchmark.py --bundle legal           ║"
echo "║     python3 script/run_benchmark.py --difficulty easy --limit 5  ║"
echo "║     python3 script/run_benchmark.py --skip-exec              ║"
echo "╚══════════════════════════════════════════════════════════════╝"