#!/bin/bash
set -x
set +e

source $PWD/scripts/constants.sh

docker run \
    -v $PWD/state/mainfork:/state:rw \
    -v $PWD/scripts:/scripts:rw \
    --entrypoint '/scripts/compress.sh' \
    $AGORIC_DOCKER_IMAGE
