#!/bin/bash
set -x
set +e

source $PWD/scripts/constants.sh

docker run \
    -v $PWD/state/mainnet/agoric:/root/agoric:rw \
    -v $PWD/scripts:/scripts:rw \
    --entrypoint '/scripts/state_sync.sh' \
    $AGORIC_DOCKER_IMAGE
