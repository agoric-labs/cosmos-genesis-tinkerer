#!/bin/bash
set -x
set +e

source /scripts/constants.sh

apt update
apt install -y axel
apt install lz4

wget http://archive.ubuntu.com/ubuntu/pool/main/s/sed/sed_4.8.orig.tar.xz
tar -xf sed_4.8.orig.tar.xz
cd sed-4.8/
./configure
make
make install
sed --version

cp $AGORIC_HOME/data/priv_validator_state.json  $AGORIC_HOME/priv_validator_state.json
rm -rf $AGORIC_HOME/data/*
cd $AGORIC_HOME
agd tendermint unsafe-reset-all --home $AGORIC_HOME

axel --quiet -n 10 -o "$SNAPHSOT_FILE" "$SNAPHSOT_BASE/$SNAPHSOT_FILE"
lz4 -c -d "$SNAPHSOT_FILE"  | tar -x -C $AGORIC_HOME

cp $AGORIC_HOME/priv_validator_state.json  $AGORIC_HOME/data/priv_validator_state.json

wget -O addrbook.json https://snapshots.polkachu.com/addrbook/agoric/addrbook.json --inet4-only
mv addrbook.json $AGORIC_HOME/config/

wget -O genesis.json https://snapshots.polkachu.com/genesis/agoric/genesis.json --inet4-only
mv genesis.json $AGORIC_HOME/config/

sed -i "s/^halt-height = .*/halt-height = $HALT_HEIGHT/" $AGORIC_HOME/config/app.toml

agd start --home $AGORIC_HOME

exit 0
