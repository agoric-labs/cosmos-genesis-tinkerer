#!/bin/bash
set -x
set +e

docker run \
    -v $PWD/state/mainfork:/state:rw \
    -v $PWD/scripts:/scripts:rw \
    --entrypoint '/scripts/compress.sh' \
    ghcr.io/agoric/agoric-sdk:38
