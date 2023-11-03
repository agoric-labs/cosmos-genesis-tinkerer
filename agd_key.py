#!/usr/bin/env python
"""
This example will turn a genesis file exported from mainnet
into a genesis file that has a single validator.
Usage:
$ ./example_mainnet_genesis.py
To recover the validator key, use the following mnemonic:
abandon abandon abandon abandon abandon abandon abandon abandon
abandon abandon abandon abandon abandon abandon abandon abandon
abandon abandon abandon abandon abandon abandon abandon art
"""
import subprocess
import json

agd = ["agd", "--home", "/state/agoric1"]

class Key:
    def __init__(self, name):
        self.name = name
        output = subprocess.run(agd + ["keys",
                            "--keyring-backend=test", "add", name,
                            "--output", "json"],
                            check=True, capture_output=True, text=True)
        new_key = json.loads(output.stdout)
        self.address = new_key['address']
        self.public_key = json.loads(new_key['pubkey'])['key']
        self.mnemonic = new_key['mnemonic']

        self.public_key_object = {
            "@type": "/cosmos.crypto.secp256k1.PubKey",
            "key": self.public_key
        }

        output = subprocess.run(agd + ["keys", "parse", self.address,
                "--output", "json"],
                check=True, capture_output=True, text=True)
        self.byte_address = json.loads(output.stdout)["bytes"]

        output = subprocess.run(agd + ["keys", "parse", self.byte_address,
                                "--output", "json"],
                                check=True, capture_output=True, text=True)
        self.formats = json.loads(output.stdout)["formats"]

    def __str__(self):
        return f"Key:  name:{self.name}, address:{self.address}, pubkey:{self.public_key}, byte_address:{self.byte_address}, mnemonic:{self.mnemonic}, {self.formats[0]}"
    
    def get_address(self, format):
        for address in self.formats:
            if address.startswith(format):
                return address
        return None       

    def add_genesis_account(self):
        subprocess.run(agd + ["add-genesis-account", self.address, "5000000000000000ubld"],
                                check=True, capture_output=True, text=True)
