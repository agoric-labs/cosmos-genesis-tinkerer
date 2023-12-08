#!/bin/bash
set -x
set +e

./scripts/run_state_sync.sh

./scripts/run_export.sh

./scripts/run_tinkerer.sh

./scripts/run_compress.sh

# ./scripts/run_upload.sh
