#!/usr/bin/env bash 

export AGORIC_DOCKER_IMAGE="ghcr.io/agoric/agoric-sdk:39"
export AGORIC_HOME="$HOME/agoric"
export SNAPHSOT_BASE="https://snapshots.polkachu.com/snapshots/agoric"
export HEIGHT=13103773
export HALT_HEIGHT=$(($HEIGHT + 5))
export SNAPHSOT_FILE="agoric_$HEIGHT.tar.lz4"
