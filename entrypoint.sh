#!/bin/bash
set -x
set +e

wget http://archive.ubuntu.com/ubuntu/pool/main/s/sed/sed_4.8.orig.tar.xz
tar -xf sed_4.8.orig.tar.xz
cd sed-4.8/
./configure
make
make install

rm -rf /state/agoric1/keyring-test
rm /state/agoric1/config/genesis.json
cat /state/agoric1/config/genesis-org.json | jq . > /state/agoric1/config/genesis.json

cd /cosmos-genesis-tinkerer
apt install -y python3-venv
python3 -m venv .env
source .env/bin/activate
python3 agoric_genesis.py

cp /state/agoric1/config/genesis.json /state/agoric2/config/genesis.json 

sed -i "s/127\.0\.0\.1/0\.0\.0\.0/g" /state/agoric1/config/config.toml
sed -i "s/127\.0\.0\.1/0\.0\.0\.0/g" /state/agoric1/config/app.toml

sed -i "s/127\.0\.0\.1/0\.0\.0\.0/g" /state/agoric2/config/config.toml
sed -i "s/127\.0\.0\.1/0\.0\.0\.0/g" /state/agoric2/config/app.toml

agd --home=/state/agoric1 tendermint unsafe-reset-all
agd --home=/state/agoric2 tendermint unsafe-reset-all
