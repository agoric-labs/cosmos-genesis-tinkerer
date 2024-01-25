#!/bin/bash
set -x
set +e

source $PWD/scripts/constants.sh

docker run --entrypoint '/tinkerer/scripts/tinkerer.sh' \
           -v $PWD/state/mainfork:/state:rw \
           -v $PWD/state/mainnet/agoric/export:/export:rw \
           -v $PWD:/tinkerer:rw  \
           $AGORIC_DOCKER_IMAGE
