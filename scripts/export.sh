#!/bin/bash
set -x
set +e

AGORIC_HOME=$HOME/agoric

apt update
apt install sqlite3

#sqlite3 $AGORIC_HOME/data/agoric/swingstore.sqlite 'delete from transcriptItems; delete from transcriptSpans; VACUUM;'

mkdir -p $AGORIC_HOME/export
rm -rf $AGORIC_HOME/export/*

agd export --export-dir $AGORIC_HOME/export --home $AGORIC_HOME
