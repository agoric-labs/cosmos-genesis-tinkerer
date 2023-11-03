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

# Key:  name:peppa, address:agoric1sx3jrcs6q3dn49x07qhkf7qfcltq6xqw4ntlx5, pubkey:AnycX+c6so98e9/3yUU4gmDiWFqxq8K6HOmiM3BPPQxW, byte_address:81A321E21A045B3A94CFF02F64F809C7D60D180E, mnemonic:auto erupt whisper push chase tunnel enjoy normal baby tobacco delay minor fee balance initial radar cereal plug infant hood pizza pyramid bulb voice, agoric1sx3jrcs6q3dn49x07qhkf7qfcltq6xqw4ntlx5
#
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
print(accounts)

bonded_account = tinkerer.get_bonded_pool_address()

# Important: The following work is split into multiple loops to make replace_account_address, replace_validator, and replace_delegator tasks to be executed before other tasks.
# for account in accounts:
#     new_key = Key(account['address'])
#     new_accounts[account["address"]] = new_key
#     print(new_key)

# for account in accounts:
#     if account["address"] == bonded_account:
#         continue
#     tinkerer.add_task(tinkerer.replace_account_address,
#                      old_account=account,
#                      new_account=new_accounts[account["address"]])



tinkerer.add_task(tinkerer.replace_validator,
            old_validator=validator1,
            new_validator=alt_validator1)

tinkerer.add_task(tinkerer.replace_validator,
            old_validator=validator2,
            new_validator=alt_validator2)

tinkerer.add_task(tinkerer.replace_delegator,
            old_delegator=delegator1,
            new_delegator=alt_delegator1)

# for account in accounts:
#     if account["address"] == bonded_account:
#         continue
#     tinkerer.add_task(tinkerer.replace_auth_account,
#                      address=new_accounts[account["address"]].address,
#                      new_account=new_accounts[account["address"]].address,
#                      new_pub_obj=new_accounts[account["address"]].public_key_object)



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


# tinkerer.add_task(tinkerer.delete_transcripts)

# tinkerer.add_task(tinkerer.increase_balance,
#                  address=alt_validator2.self_delegation_address,
#                  amount=UBLD_LIQUID_TOKEN_INCREASE)

# tinkerer.add_task(tinkerer.increase_delegator_stake_to_validator,
#                  delegator=delegator1,
#                  validator=alt_validator2,
#                  increase={'amount': UBLD_STAKE_INCREASE,
#                            'denom': 'ubld'})

# tinkerer.add_task(tinkerer.increase_balance,
#                  address=alt_validator1.address,
#                  amount=UBLD_LIQUID_TOKEN_INCREASE)

#tinkerer.add_task(tinkerer.increase_validator_stake,
            #operator_address=alt_validator1.operator_address,
            #increase=1000)

# Set new governance parameters for convenience
tinkerer.add_task(tinkerer.set_voting_period,
                 voting_period='60s')

tinkerer.run_tasks()

print(new_key)