#!/usr/bin/env bash
# Evaluation script for the KR-extended benchmark.
#
# Usage:
#   bash ./script/eval_kr.sh                                    # default: WebJudge on example
#   bash ./script/eval_kr.sh /path/to/trajectories              # custom trajectory dir
#   TRAJECTORIES_DIR=/path/to/traj MODE=WebJudge_Online_Mind2Web_eval bash ./script/eval_kr.sh

set -euo pipefail

api_key="${API_KEY:-API_KEY}"
model_name="${MODEL_NAME:-o4-mini}"

# Where the agent's trajectory output lives (one <task_id>/ subdir per task).
# Defaults to the bundled KR example; override with $1 or $TRAJECTORIES_DIR.
if [[ $# -ge 1 ]]; then
    base_dir="$1"
else
    base_dir="${TRAJECTORIES_DIR:-./data/kr/example_kr}"
fi

mode="${MODE:-WebJudge_Online_Mind2Web_eval}"
output_path="${base_dir}_result"

python ./src/run.py \
    --mode "$mode" \
    --model "$model_name" \
    --trajectories_dir "$base_dir" \
    --api_key "$api_key" \
    --output_path "$output_path" \
    --num_worker 1 \
    --score_threshold 3