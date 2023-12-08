#!/bin/bash
set -x
set +e

docker run \
    -v $PWD/state/mainnet/agoric:/root/agoric:rw \
    -v $PWD/scripts:/scripts:rw \
    --entrypoint '/scripts/export.sh' \
    ghcr.io/agoric/agoric-sdk:38
