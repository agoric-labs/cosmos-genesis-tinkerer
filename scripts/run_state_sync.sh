#!/bin/bash
set -x
set +e

docker run \
    -v $PWD/state/mainnet/agoric:/root/agoric:rw \
    -v $PWD/scripts:/scripts:rw \
    --entrypoint '/scripts/state_sync.sh' \
    ghcr.io/agoric/agoric-sdk:38
