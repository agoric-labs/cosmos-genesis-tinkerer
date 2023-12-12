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
rm /state/agoric2/config/genesis.json
rm -rf /state/agoric1/config/swing-store
rm -rf /state/agoric2/config/swing-store

cp /export/genesis.json /state/agoric1/config/genesis.json

cp -r /export/swing-store /state/agoric1/config/ &
cp -r /export/swing-store /state/agoric2/config/ &

cd /tinkerer
apt install -y python3-venv
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python3 agoric_genesis.py

# sed -i "s/\/usr\/src\/agoric-sdk\/packages\/vats\/modified-bootstrap.json/@agoric\/vats\/decentral-main-vaults-config.json/g" /state/agoric1/config/genesis.json

cp /state/agoric1/config/genesis.json /state/agoric2/config/genesis.json

wait

agd --home=/state/agoric1 tendermint unsafe-reset-all
agd --home=/state/agoric2 tendermint unsafe-reset-all
