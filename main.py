# from web3 import Web3

# rpc_server_address = 'https://rpc.sepolia.org'
# web3 = Web3(Web3.HTTPProvider(rpc_server_address))

# tx_hash = '0x666765589154fce6d50a0f19bf8903c516bee2235d87d83bf0a6b8eee24d0987'
# tx = web3.eth.get_transaction(tx_hash)

# print(tx)



# from web3 import Web3

# rpc_server_address = 'https://rpc.sepolia.org'

# web3 = Web3(Web3.HTTPProvider(rpc_server_address))

# address = '0x45A616Fe04b73fD9B8d3D3172578981C1ea7D1eE'

# # Get the latest block number
# latest_block = web3.eth.block_number

# print(latest_block)
# # Loop through all blocks and transactions to find transactions involving the address
# for block_number in range(latest_block + 1):
#     block = web3.eth.get_block(block_number)

#     for tx_hash in block['transactions']:
#         tx = web3.eth.get_transaction(tx_hash)

#         if tx['from'] == address or tx['to'] == address:
#             print(tx)


# 3842845



# from web3 import Web3

# rpc_server_address = 'https://rpc.sepolia.org'

# web3 = Web3(Web3.HTTPProvider(rpc_server_address))

# address = '0x45A616Fe04b73fD9B8d3D3172578981C1ea7D1eE'
# filter = web3.eth.filter({"to": address})

# def handle_transaction(event, receipt):
#     print("New transaction detected:")
#     print("  Hash: ", event["transactionHash"].hex())
#     tx_hash = event["transactionHash"].hex()
#     tx = web3.eth.get_transaction(tx_hash)
#     print(tx)

# while True:
#     events = filter.get_new_entries()
#     for event in events:
#         receipt = web3.eth.get_transaction_receipt(event["transactionHash"])
#         handle_transaction(event, receipt)

# from web3 import Web3

# # Connect to the Ethereum network using an RPC server
# rpc_server_address = 'https://rpc.sepolia.org'

# web3 = Web3(Web3.HTTPProvider(rpc_server_address))

# # Define the address we want to filter transactions for
# address = '0x45A616Fe04b73fD9B8d3D3172578981C1ea7D1eE'

# # Create a filter that matches transactions where the 'from' or 'to' address is equal to our address
# filter = web3.eth.filter({'address': address})

# # Get the current block number
# block_number = web3.eth.block_number

# # Start listening for new transactions
# while True:
#     # Get the latest block number
#     latest_block_number = web3.eth.block_number
    
#     # If a new block has been mined, check for new transactions
#     if latest_block_number > block_number:
#         block_number = latest_block_number
        
#         # Get all new transactions that match our filter
#         new_transactions = filter.get_all_entries()
        
#         # Print each transaction
#         for transaction_hash in new_transactions:
#             transaction = web3.eth.getTransaction(transaction_hash)
#             print('Transaction from {} to {}: {} wei'.format(transaction['from'], transaction['to'], transaction['value']))


import requests
import asyncio
from web3 import Web3
from trans_bot import send_test_message

from dotenv import load_dotenv
import os
load_dotenv()

# rpc_server_address = 'https://rpc.sepolia.org'
# rpc_server_address = 'https://arbitrum-goerli.public.blastapi.io'
# rpc_server_address = 'https://testnet.era.zksync.dev'
rpc_server_address = os.environ.get('RPC_SERVER_ADDRESS')
address = os.environ.get('USER_ADDRESS')
web3 = Web3(Web3.HTTPProvider(rpc_server_address))

# get block
latest_block = web3.eth.block_number
curr_block = 0
# handle transaction
while True:
    i = latest_block if not curr_block else curr_block + 1
    while i <= web3.eth.block_number:
        block = web3.eth.get_block(i, True)
        for tx in block.transactions:
            if tx['from'] == address:
                # update current block number
                curr_block = i

                tx_hash = tx.hash.hex()
                print(f"Block: {i}, TxHash: {tx_hash}")
                tx = web3.eth.get_transaction(tx_hash)
                tx_from = tx['from']
                tx_to = tx['to']
                tx_value = tx['value']
                message = f"from: {tx_from}, to: {tx_to}, value: {tx_value}"
                print(message)
                asyncio.run(send_test_message(message=message))
        i += 1
