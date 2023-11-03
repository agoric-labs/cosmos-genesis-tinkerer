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
UBLD_LIQUID_TOKEN_INCREASE = 10 * UBLD_STAKE_INCREASE

# The original validator will be replaced
# Ollinet validator 1
# validator1 = Validator()
# validator1.self_delegation_address = "agoric1ezruw34rsll795vrsmpujml5rtkchjzs28z8fa"
# validator1.self_delegation_public_key = "Am1XLi0vgfWkjvGHsbGGb7h7GkiZFCStkxr8s5TA4suN"
# validator1.operator_address = "agoricvaloper1ezruw34rsll795vrsmpujml5rtkchjzs6l3w4u"
# validator1.public_key = "G/0sp340CeN/cPtCQeWEOnsagqTiAdX+Zo8fosILobM="
# validator1.address = "E200822E3F6FC203BD7D36AA747A5118ADD2EA93"
# validator1.consensus_address = "agoricvalcons1ugqgyt3ldlpq80tax648g7j3rzka965nw7zlky"
# validator1.name = "agoric0"


# Mainnet validator 1
validator1 = Validator()
validator1.self_delegation_address = "agoric1qr7k4hr3qw2xvjhl8925gsw57ef8llv4e4ykpl"
validator1.self_delegation_public_key = "A4XT6Kul/1VMbWuj1BPDYVyD9xrGY+WvACCsKhzMFkaH"
validator1.operator_address = "agoricvaloper14lultfckehtszvzw4ehu0apvsr77afvy4d3pzq"
validator1.public_key = "2kzaCesVCMiNN5IoHZHYrJdMRFP605/pFsRYNIaqFd4="
validator1.address = "E29E617AD137136F27BF347591AE2E8417EDDC5B"
validator1.consensus_address = "agoricvalcons1u20xz7k3xufk7falx36ert3wsst7mhzmqgdqn0"
validator1.name = "DokiaCapital"


alt_validator1 = Validator()
alt_validator1.self_delegation_address = validator1.self_delegation_address
alt_validator1.self_delegation_public_key = validator1.self_delegation_public_key
alt_validator1.operator_address = validator1.operator_address
alt_validator1.public_key = "kHOI3Ao3R+W7yuHak8bUyXCDqWQ+F56cr+McN5HLPu4="
alt_validator1.address = "6392DE61F82BF84F17ABCB837EB5444E755BC3B4"
alt_validator1.consensus_address = "agoricvalcons1vwfduc0c90uy79atewphad2yfe64hsa593vf2w"
alt_validator1.name = validator1.name

# Ollinet validator 2
# validator2 = Validator()
# validator2.self_delegation_address = "agoric1gl2e3reqgmpjawaexl7qlcq3y6mtnkpxq68qf4"
# validator2.self_delegation_public_key = "C1WrGjVh0lvCutz0rgztx5w81sYfC7BeFxYH7wELyWo="
# validator2.operator_address = "agoricvaloper1gl2e3reqgmpjawaexl7qlcq3y6mtnkpxsz5f45"
# validator2.public_key = "C1WrGjVh0lvCutz0rgztx5w81sYfC7BeFxYH7wELyWo="
# validator2.address = "D8A07604A7F388D50E7DE7E29E0F3CC2A9A99EB2"
# validator2.consensus_address = "agoricvalcons1mzs8vp987wyd2rnaul3fureuc256n84j55wegt"
# validator2.name = "validator-1"

# Mainnet validator 2
validator2 = Validator()
validator2.self_delegation_address = "agoric1lhxs063m3qwdjrc9svmfzcf4mvv0vlhxrhqgka"
validator2.self_delegation_public_key = "A6oBneiw0Kosp5USeIrguPIJMezqLk/wDFEVvt8tNpBo"
validator2.operator_address = "agoricvaloper108p8an08ztyxp8yhd2ca5zn456e3myqksy22pa"
validator2.public_key = "JQdQwEFBmQhyu1YMYG4BKGBfZSB542BZbbo8Beqng1I="
validator2.address = "BB5E2C3807AE56E46129196128607662D3643EE5"
validator2.consensus_address = "agoricvalcons1hd0zcwq84etwgcffr9sjscrkvtfkg0h9ljus68"
validator2.name = "polkachu.com"


alt_validator2 = Validator()
alt_validator2.self_delegation_address = validator2.self_delegation_address
alt_validator2.self_delegation_public_key = validator2.self_delegation_public_key
alt_validator2.operator_address = validator2.operator_address
alt_validator2.public_key = "Tasmq5v3wUwjJCNSkCKLM6FPorqC/m+08cbHLmD4pUM="
alt_validator2.address = "C6D8B0E84F89742885CEF24ADA2A26E59F085120"
alt_validator2.consensus_address = "agoricvalcons1cmvtp6z0396z3pww7f9d523xuk0ss5fqs6fs6v"
alt_validator2.name = validator2.name

delegator1 = Delegator()
delegator1.address = validator1.self_delegation_address
delegator1.public_key = validator1.self_delegation_public_key
