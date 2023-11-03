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
import subprocess

GENESIS_PEER = "/Users/touseefliaqat/code/state/agoric1/config/genesis.json"

# Tokens configuration
UBLD_STAKE_INCREASE = 5500000000 * 1000000
UBLD_LIQUID_TOKEN_INCREASE = 3 * UBLD_STAKE_INCREASE

# The original validator will be replaced
# Ollinet validator 1
org_val1 = Validator()
org_val1.self_delegation_address = "agoric1ezruw34rsll795vrsmpujml5rtkchjzs28z8fa"
org_val1.self_delegation_public_key = "Am1XLi0vgfWkjvGHsbGGb7h7GkiZFCStkxr8s5TA4suN"
org_val1.operator_address = "agoricvaloper1ezruw34rsll795vrsmpujml5rtkchjzs6l3w4u"
org_val1.public_key = "G/0sp340CeN/cPtCQeWEOnsagqTiAdX+Zo8fosILobM="
org_val1.address = "E200822E3F6FC203BD7D36AA747A5118ADD2EA93"
org_val1.consensus_address = "agoricvalcons1ugqgyt3ldlpq80tax648g7j3rzka965nw7zlky"
org_val1.name = "agoric0"


# Mainnet validator 1
# org_val1 = Validator()
# org_val1.self_delegation_address = "agoric1qr7k4hr3qw2xvjhl8925gsw57ef8llv4e4ykpl"
# org_val1.self_delegation_public_key = "A4XT6Kul/1VMbWuj1BPDYVyD9xrGY+WvACCsKhzMFkaH"
# org_val1.operator_address = "agoricvaloper14lultfckehtszvzw4ehu0apvsr77afvy4d3pzq"
# org_val1.public_key = "2kzaCesVCMiNN5IoHZHYrJdMRFP605/pFsRYNIaqFd4="
# org_val1.address = "E29E617AD137136F27BF347591AE2E8417EDDC5B"
# org_val1.consensus_address = "agoricvalcons1u20xz7k3xufk7falx36ert3wsst7mhzmqgdqn0"
# org_val1.name = "DokiaCapital"


new_val1 = Validator()
# new_val1.self_delegation_address = "agoric1vwfduc0c90uy79atewphad2yfe64hsa5p6vu6w"
new_val1.self_delegation_address = org_val1.self_delegation_address
# test_val.self_delegation_reward_address = "cosmos1r5v5srda7xfth3hn2s26txvrcrntldjumt8mhl"
# new_val1.self_delegation_public_key = "kHOI3Ao3R+W7yuHak8bUyXCDqWQ+F56cr+McN5HLPu4="
new_val1.self_delegation_public_key = org_val1.self_delegation_public_key

# new_val1.operator_address = "agoricvaloper1vwfduc0c90uy79atewphad2yfe64hsa53zl4x0"
new_val1.operator_address = org_val1.operator_address

new_val1.public_key = "kHOI3Ao3R+W7yuHak8bUyXCDqWQ+F56cr+McN5HLPu4="
new_val1.address = "6392DE61F82BF84F17ABCB837EB5444E755BC3B4"
new_val1.consensus_address = "agoricvalcons1vwfduc0c90uy79atewphad2yfe64hsa593vf2w"
# node id: 0663e8221928c923d516ea1e8972927f54da9edb
new_val1.name = "peer1"

# Ollinet validator 2
org_val2 = Validator()
org_val2.self_delegation_address = "agoric1gl2e3reqgmpjawaexl7qlcq3y6mtnkpxq68qf4"
org_val2.self_delegation_public_key = "C1WrGjVh0lvCutz0rgztx5w81sYfC7BeFxYH7wELyWo="
org_val2.operator_address = "agoricvaloper1gl2e3reqgmpjawaexl7qlcq3y6mtnkpxsz5f45"
org_val2.public_key = "C1WrGjVh0lvCutz0rgztx5w81sYfC7BeFxYH7wELyWo="
org_val2.address = "D8A07604A7F388D50E7DE7E29E0F3CC2A9A99EB2"
org_val2.consensus_address = "agoricvalcons1mzs8vp987wyd2rnaul3fureuc256n84j55wegt"
org_val2.name = "validator-1"

# Mainnet validator 2
# org_val2 = Validator()
# org_val2.self_delegation_address = "agoric1lhxs063m3qwdjrc9svmfzcf4mvv0vlhxrhqgka"
# org_val2.self_delegation_public_key = "A6oBneiw0Kosp5USeIrguPIJMezqLk/wDFEVvt8tNpBo"
# org_val2.operator_address = "agoricvaloper108p8an08ztyxp8yhd2ca5zn456e3myqksy22pa"
# org_val2.public_key = "JQdQwEFBmQhyu1YMYG4BKGBfZSB542BZbbo8Beqng1I="
# org_val2.address = "BB5E2C3807AE56E46129196128607662D3643EE5"
# org_val2.consensus_address = "agoricvalcons1hd0zcwq84etwgcffr9sjscrkvtfkg0h9ljus68"
# org_val2.name = "polkachu.com"


new_val2 = Validator()
new_val2.self_delegation_address = "agoric1cmvtp6z0396z3pww7f9d523xuk0ss5fq53f92v"
new_val2.self_delegation_public_key = "Tasmq5v3wUwjJCNSkCKLM6FPorqC/m+08cbHLmD4pUM="
new_val2.operator_address = "agoricvaloper1cmvtp6z0396z3pww7f9d523xuk0ss5fqyf6vkd"
new_val2.public_key = "Tasmq5v3wUwjJCNSkCKLM6FPorqC/m+08cbHLmD4pUM="
new_val2.address = "C6D8B0E84F89742885CEF24ADA2A26E59F085120"
new_val2.consensus_address = "agoricvalcons1cmvtp6z0396z3pww7f9d523xuk0ss5fqs6fs6v"
# node id: e234dc7fffdea593c5338a9dd8b5c22ba00731eb
new_val2.name = "peer2"

org_del = Delegator()
org_del.address = new_val1.self_delegation_address
org_del.public_key = new_val1.self_delegation_public_key

new_del = Delegator()
new_del.address = "agoric15t2ua083ekhd86n978l3xv9g8989qa04mzzd0k"
new_del.public_key = "AlnpuxCnM1T9Ne2iQMJPMGSauhKoO7tApn50Gt2hZo5P"
