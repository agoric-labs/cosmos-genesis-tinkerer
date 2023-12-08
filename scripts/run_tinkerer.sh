#!/bin/bash
set -x
set +e

docker run -it --entrypoint '/tinkerer/scripts/tinkerer.sh' \
           -v $PWD/state/mainfork:/state:rw \
           -v $PWD/state/mainnet/agoric/export:/export:rw \
           -v $PWD:/tinkerer:rw  \
           --net=bridge ghcr.io/agoric/agoric-sdk:38
