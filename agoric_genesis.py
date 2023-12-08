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
from cosmos_genesis_tinker import Delegator, Validator, GenesisTinker
from agoric_constants import validator1, validator2, alt_validator1, alt_validator2, delegator1
from agd_key import Key
import subprocess
import json

GENESIS_PEER = "/state/agoric1/config/genesis.json"

# Tokens configuration
UBLD_STAKE_INCREASE = 500000000 * 10000000
UBLD_LIQUID_TOKEN_INCREASE = 3 * UBLD_STAKE_INCREASE

filter_address = [validator1.self_delegation_address, validator2.self_delegation_address, delegator1.address]

print("Tinkering... ")

new_key = Key('whale')
new_key.add_genesis_account()

alt_delegator1 = Delegator()
alt_delegator1.address = new_key.address
alt_delegator1.public_key = new_key.public_key
print(alt_delegator1)

filter_address.append(alt_delegator1.address)

tinkerer = GenesisTinker(input_file=GENESIS_PEER, output_file=GENESIS_PEER)
tinkerer.auto_load()
accounts = tinkerer.get_accounts()
accounts = tinkerer.filter_accounts(filter_address)
new_accounts = {}

bonded_account = tinkerer.get_bonded_pool_address()

tinkerer.add_task(tinkerer.replace_validator,
            old_validator=validator1,
            new_validator=alt_validator1)

tinkerer.add_task(tinkerer.replace_validator,
            old_validator=validator2,
            new_validator=alt_validator2)

tinkerer.add_task(tinkerer.replace_delegator,
            old_delegator=delegator1,
            new_delegator=alt_delegator1)

tinkerer.add_task(tinkerer.increase_balance,
                 address=alt_delegator1.address,
                 amount=UBLD_LIQUID_TOKEN_INCREASE)

tinkerer.add_task(tinkerer.increase_delegator_stake_to_validator,
                 delegator=alt_delegator1,
                 validator=alt_validator1,
                 increase={'amount': UBLD_STAKE_INCREASE,
                           'denom': 'ubld'})

tinkerer.add_task(tinkerer.increase_delegator_stake_to_validator,
                 delegator=alt_delegator1,
                 validator=alt_validator2,
                 increase={'amount': UBLD_STAKE_INCREASE,
                           'denom': 'ubld'})

# Set new governance parameters for convenience
tinkerer.add_task(tinkerer.set_voting_period,
                 voting_period='60s')

tinkerer.run_tasks()

print(new_key)