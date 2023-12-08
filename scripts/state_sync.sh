#!/bin/bash
set -x
set +e

wget http://archive.ubuntu.com/ubuntu/pool/main/s/sed/sed_4.8.orig.tar.xz
tar -xf sed_4.8.orig.tar.xz
cd sed-4.8/
./configure
make
make install
sed --version

AGORIC_HOME=$HOME/agoric
SNAP_RPC="https://agoric-rpc.polkachu.com:443"

LATEST_HEIGHT=$(curl -s $SNAP_RPC/block | jq -r .result.block.header.height); \
BLOCK_HEIGHT=$((LATEST_HEIGHT - 25000)); \
TRUST_HASH=$(curl -s "$SNAP_RPC/block?height=$BLOCK_HEIGHT" | jq -r .result.block_id.hash)

echo "Latest height"
echo "$LATEST_HEIGHT" > $AGORIC_HOME/height.txt
cat $AGORIC_HOME/height.txt

sed -i.bak -E "s|^(enable[[:space:]]+=[[:space:]]+).*$|\1true| ; \
s|^(rpc_servers[[:space:]]+=[[:space:]]+).*$|\1\"$SNAP_RPC,$SNAP_RPC\"| ; \
s|^(trust_height[[:space:]]+=[[:space:]]+).*$|\1$BLOCK_HEIGHT| ; \
s|^(trust_hash[[:space:]]+=[[:space:]]+).*$|\1\"$TRUST_HASH\"|" $AGORIC_HOME/config/config.toml

cat $AGORIC_HOME/config/config.toml

agd tendermint unsafe-reset-all --home $AGORIC_HOME

wget -O addrbook.json https://snapshots.polkachu.com/addrbook/agoric/addrbook.json --inet4-only
mv addrbook.json $AGORIC_HOME/config/

wget -O genesis.json https://snapshots.polkachu.com/genesis/agoric/genesis.json --inet4-only
mv genesis.json $AGORIC_HOME/config/

agd start --home $AGORIC_HOME
