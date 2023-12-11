#!/bin/bash
set -x
set +e

docker run --entrypoint '/tinkerer/scripts/tinkerer.sh' \
           -v $PWD/state/mainfork:/state:rw \
           -v $PWD/state/mainnet/agoric/export:/export:rw \
           -v $PWD:/tinkerer:rw  \
           ghcr.io/agoric/agoric-sdk:38
