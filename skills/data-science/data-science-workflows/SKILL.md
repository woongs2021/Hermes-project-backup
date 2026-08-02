---
name: data-science-workflows
description: "Use when doing iterative Python/data exploration, notebook-style analysis, live kernels, DataFrame inspection, statistical exploration, or reproducible data-science scratch work."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [data-science, python, jupyter, notebooks, repl, exploration, analysis]
---

# Data Science Workflows

## Overview

This is the class-level umbrella for interactive data-science and exploratory Python work. Use it when the user needs notebook-like iteration, stateful variables, data inspection, plotting, statistical exploration, or a clean reproducible analysis artifact.

The shared pattern is: identify the data/source and question, choose the execution mode, run small checks before full analysis, preserve useful artifacts, and report results with paths, assumptions, and caveats.

## When to Use

- The user asks to explore data, inspect a DataFrame, test analysis code interactively, or build up state over multiple steps.
- The task would normally be done in a Jupyter notebook or REPL rather than a one-shot script.
- The user asks for statistical summaries, plots, model prototyping, notebook cleanup, or reproducible exploratory analysis.
- You need a live kernel because variables, imports, loaded data, or expensive setup should persist across executions.

## Execution Mode Decision

| Mode | Use When |
| --- | --- |
| Live Jupyter kernel | Iterative exploration, persistent variables, notebook editing, DataFrames/plots, repeated API probing |
| `execute_code` | One-shot stateless scripts that need Hermes tool access such as web/file helpers |
| `terminal` | Installing packages, shell commands, long-running scripts, git/build/process management |

If you would open a notebook for the task, prefer the live-kernel lane. If the task needs Hermes tool calls inside the code, prefer `execute_code` unless you explicitly bridge the data into the notebook.

## Live Jupyter Kernel Lane (hamelnb)

Prerequisites and setup:

1. Check `uv` is available.
2. Install JupyterLab if needed: `uv tool install jupyterlab`.
3. Use the hamelnb helper script at `$HOME/.agent-skills/hamelnb/skills/jupyter-live-kernel/scripts/jupyter_live_kernel.py`; clone `https://github.com/hamelsmu/hamelnb.git` to `~/.agent-skills/hamelnb` if it is missing.
4. Start a local headless Jupyter server when none is running:
   ```bash
   jupyter-lab --no-browser --port=8888 --notebook-dir=$HOME/notebooks \
     --IdentityProvider.token='' --ServerApp.password='' > /tmp/jupyter.log 2>&1 &
   ```

Core commands, always with `--compact` to save context:

```bash
SCRIPT="$HOME/.agent-skills/hamelnb/skills/jupyter-live-kernel/scripts/jupyter_live_kernel.py"
uv run "$SCRIPT" servers --compact
uv run "$SCRIPT" notebooks --compact
uv run "$SCRIPT" execute --path scratch.ipynb --code $'import pandas as pd\nprint(pd.__version__)' --compact
uv run "$SCRIPT" variables --path scratch.ipynb list --compact
uv run "$SCRIPT" variables --path scratch.ipynb preview --name df --compact
uv run "$SCRIPT" contents --path scratch.ipynb --compact
uv run "$SCRIPT" restart-run-all --path scratch.ipynb --save-outputs --compact
```

For pure REPL use, create `~/notebooks/scratch.ipynb`, start a session via the Jupyter REST API, then execute code repeatedly against that notebook.

## Analysis Workflow

1. **Frame the question.** Capture the dataset/source, target metric, required output, and whether the result is exploratory or production-grade.
2. **Load and sanity-check data.** Verify row counts, schema, missing values, date ranges, duplicates, and units before modeling or plotting.
3. **Iterate in small cells.** Keep expensive loads cached in kernel state; inspect intermediate variables rather than rerunning from scratch.
4. **Make outputs durable.** Save cleaned data, figures, notebooks, or scripts to explicit paths when the user needs a deliverable.
5. **Verify from a clean run when needed.** Use restart/run-all or a standalone script before claiming a notebook/report is reproducible.

## Practical Tips

- First execution after a Jupyter server starts may timeout while the kernel initializes; retry once before escalating.
- The kernel Python is JupyterLab's Python, so packages must be installed into that environment, not necessarily the Hermes runtime.
- Subcommand argument order matters: use `variables --path nb.ipynb list`, not `variables list --path nb.ipynb`.
- Errors are returned as JSON with `ename` and `evalue`; inspect those before changing code.
- For long-running cells, pass a larger timeout such as `--timeout 120`.

## Common Pitfalls

1. **Using a stateless one-shot script for iterative analysis.** You lose expensive setup and intermediate variables.
2. **Forgetting clean verification.** A notebook that works only because of hidden kernel state is not reproducible.
3. **Wrong Python environment.** Installing packages into Hermes does not necessarily install them into the Jupyter tool environment.
4. **Verbose notebook output.** Always use compact output and preview large variables instead of dumping them.

## Verification Checklist

- [ ] Dataset/source and analysis question are explicit.
- [ ] Execution mode chosen deliberately.
- [ ] Data sanity checks run before conclusions.
- [ ] Outputs saved to paths when deliverables are requested.
- [ ] Clean restart/run-all or equivalent reproducibility check performed when appropriate.
