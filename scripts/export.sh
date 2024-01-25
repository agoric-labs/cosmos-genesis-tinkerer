#!/bin/bash
set -x
set +e

AGORIC_HOME=$HOME/agoric

mkdir -p $AGORIC_HOME/export
rm -rf $AGORIC_HOME/export/*

agd export --export-dir $AGORIC_HOME/export --home $AGORIC_HOME
