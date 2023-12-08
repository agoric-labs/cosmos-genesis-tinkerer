#!/bin/bash
set -x
set +e

height=$(cat /scripts/height.txt)

if [ -z "$height" ]; then
    echo "Please provide height"
    exit 1
fi

cd /state
rm "agoric1-config-$height.tar.gz"
rm "agoric2-config-$height.tar.gz"
rm "agoric-$height.tar.gz"

tar -czf "agoric1-config-$height.tar.gz" --exclude="config/genesis*" --exclude="config/swing-store" -C agoric1 config data/priv_validator_state.json
tar -czf "agoric2-config-$height.tar.gz" --exclude="config/genesis*" --exclude="config/swing-store" -C agoric2 config 
tar -czf "agoric-$height.tar.gz" -C agoric1 config/genesis.json config/swing-store data keyring-test
