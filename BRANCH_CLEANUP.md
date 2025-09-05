# Branch Cleanup Documentation

## Overview
This repository currently has 42 branches total. The goal is to clean up all branches except the `main` branch, leaving only 1 active branch.

## Current Branch Status

### Main Branch (to keep)
- `main` - Main development branch (SHA: 1e2bb59eebfc6e632613a3702de5c1a4ef8a7272)

### Branches to Delete (41 total)

#### Codex-generated branches (36 branches)
- 4k31ja-codex/modify-is_free-to-return-true-or-false
- codex/add-and-expand-docstrings-in-scripts
- codex/add-cli-argument-for-workers-from-env
- codex/add-requirements.txt-and-installation-instructions
- codex/add-sys.path-modification-and-verify-pytest
- codex/allow-team-size-parameter-and-env-worker-count
- codex/assign-sla-in-__init__-method
- codex/clarify-cli-guidance-in-readme
- codex/clarify-data-definitions-in-data.py
- codex/convert-call-and-agent-to-dataclasses
- codex/create-department-enum-and-update-code
- codex/create-helper-to-load-numbers-and-refactor-statistics
- codex/fix-typo--ussing--to--using
- codex/implement-argparse-for-mode-selection
- codex/implement-build_worker_list-function
- codex/implement-generic-helper-functions
- codex/implement-or-simplify-next_available-logic
- codex/improve-docstrings
- codex/improve-docstrings-across-files
- codex/improve-readme,-add-model-details
- codex/improve-skills-model-details
- codex/improve-unit-tests
- codex/modify-is_free-to-return-true-or-false
- codex/perform-code-quality-review
- codex/refactor-_service_level-to-use-generator-expression
- codex/refactor-algorithm-for-flexible-worker-configuration
- codex/refactor-filter.first_level-and-filter.second_level
- codex/refactor-non-english-variables-and-methods
- codex/refactor-simulation-loop-into-run_simulation
- codex/refactor-sys.stdout-reassignment-in-main.py
- codex/remove-unused-import-and-store-sla-value
- codex/remove-unused-imports-from-files
- codex/rename-variables-and-update-comments-to-english
- codex/replace-basque-names-with-english-equivalents
- codex/specify-python-version-and-dependencies
- codex/update-.gitignore-and-readme

#### Other AI-generated branches (4 branches)
- kcucde-codex/refactor-non-english-variables-and-methods
- kvcze9-codex/add-sys.path-modification-and-verify-pytest
- p789rk-codex/improve-docstrings
- w2ab53-codex/clarify-data-definitions-in-data.py

#### Copilot branch (1 branch)
- copilot/fix-f6724fc5-7088-41e6-8a0f-a52c01659576

## Cleanup Actions

### Automated Cleanup
Use the provided script `cleanup-branches.sh` to delete all branches except main:

```bash
./cleanup-branches.sh
```

### Manual Cleanup
If preferred, branches can be deleted manually using:

```bash
git push origin --delete <branch-name>
```

### Verification
After cleanup, verify only the main branch remains:

```bash
git ls-remote --heads origin
```

Expected result:
```
1e2bb59eebfc6e632613a3702de5c1a4ef8a7272	refs/heads/main
```

## Notes
- All branches are currently unprotected and can be safely deleted
- The main branch contains a working codebase with passing tests (19 tests pass)
- No branch protection rules are currently in place
- The cleanup is irreversible - deleted branches cannot be recovered unless SHA references are preserved

## Repository State After Cleanup
- Single active branch: `main`
- Clean branch history
- Simplified development workflow
- Reduced repository complexity