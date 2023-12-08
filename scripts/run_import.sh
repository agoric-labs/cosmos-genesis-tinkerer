#!/bin/bash
set -x
set +e

wait_for_bootstrap() {
  endpoint="localhost"
  while true; do
    if json=$(docker exec agoric1 curl -s --fail -m 15 "$endpoint:26657/status"); then
      if [[ "$(echo "$json" | jq -r .jsonrpc)" == "2.0" ]]; then
        if last_height=$(echo "$json" | jq -r .result.sync_info.latest_block_height); then
          if [[ "$last_height" != "1" ]]; then
            echo "$last_height"
            return
          else
            echo "$last_height"
          fi
        fi
      fi
    fi
    sleep 5
  done
  echo "done"
}

waitForBlock() (
  echo "waiting for block..."
  times=${1:-1}
  echo "$times"
  for ((i = 1; i <= times; i++)); do
    b1=$(wait_for_bootstrap)
    while true; do
      b2=$(wait_for_bootstrap)
      if [[ "$b1" != "$b2" ]]; then
        echo "block produced"
        break
      fi
      sleep 5
    done
  done
  echo "done"
)

NETWORK_NAME="forknet"
network_exists=$(docker network ls --filter name=^${NETWORK_NAME}$ --format "{{ .Name }}")
if [ -z "$network_exists" ]; then
    echo "Network '$NETWORK_NAME' does not exist. Creating it..."
    docker network create --subnet=10.99.0.0/16 $NETWORK_NAME
else
    echo "Network '$NETWORK_NAME' already exists."
fi

docker kill agoric1
docker kill agoric2

docker rm agoric1
docker rm agoric2

docker run --name agoric1 -d -v $PWD/state/mainfork:/state:rw -v --net=forknet --ip 10.99.0.2 ghcr.io/agoric/agoric-sdk:36 start --home /state/agoric1 --x-crisis-skip-assert-invariants --iavl-disable-fastnode false
docker run --name agoric2 -d -v $PWD/state/mainfork:/state:rw -v --net=forknet --ip 10.99.0.3 ghcr.io/agoric/agoric-sdk:36 start --home /state/agoric2 --x-crisis-skip-assert-invariants --iavl-disable-fastnode false

waitForBlock 5
height=$(wait_for_bootstrap)

docker kill agoric1
docker kill agoric2


# tar -czf agoric2-config-$height.tar.gz --exclude='config/genesis*' --exclude='config/swing-store' -C agoric2 config data/priv_validator_state.json
# tar -czf agoric-$height.tar.gz -C agoric1 config/genesis.json data keyring-test

# Compress things for upload
#docker run -it --entrypoint '/cosmos-genesis-tinkerer/compress.sh' \
#           -v /Users/touseefliaqat/code/state:/state:rw \
#           -v /Users/touseefliaqat/code/state/cosmos-genesis-tinkerer:/cosmos-genesis-tinkerer:rw  \
#           --net=bridge ghcr.io/agoric/agoric-sdk:36 $height