#!/bin/bash
set -x
set +e

cp -r $PWD/state/mainnet/agoric/data/priv_validator_state.json ./priv_validator_state.json
rm -rf $PWD/state/mainnet/agoric/data/*
mv ./priv_validator_state.json $PWD/state/mainnet/agoric/data/priv_validator_state.json

docker run -it \
    -v $PWD/state/mainnet/agoric:/root/agoric:rw \
    -v $PWD/scripts:/scripts:rw \
    --entrypoint '/scripts/state_sync.sh' \
    ghcr.io/agoric/agoric-sdk:38
