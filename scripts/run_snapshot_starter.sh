#!/bin/bash
set -x
set +e

source $PWD/scripts/constants.sh

docker run \
    -v $PWD/state/mainnet/agoric:/root/agoric:rw \
    -v $PWD/scripts:/scripts:rw \
    --entrypoint '/scripts/snapshot_starter.sh' \
    $AGORIC_DOCKER_IMAGE
