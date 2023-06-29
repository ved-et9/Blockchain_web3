from solcx import compile_standard,install_solc
import json
from web3 import Web3

with open("F:\Web3\simple_storage.sol","r") as file :
    simple_storage_file = file.read()
    print(simple_storage_file)


   #complile solidity
install_solc('0.8.20')
compiles_sol = compile_standard({
    "language":"Solidity",
    "sources":{"simple_storage.sol": {"content":simple_storage_file}},
    "settings": {
        "outputSelection":{
            "*":{"*" : ["abi","metadata","evm.bytecode","evm.sourceMap"]}
            }
        },
    },

    solc_version="0.8.20",
)

with open("compiled_code.json","w") as file:
    json.dump(compiles_sol,file)



#get bytecode

bytecode = compiles_sol["contracts"]["simple_storage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]
print(bytecode)
#get abi

abi=compiles_sol["contracts"]["simple_storage.sol"]["SimpleStorage"]["abi"]



#Ganache = Ganache is a simulated or a fake blockchain that we 
# can use to deploy contract 
# just like javascript vm in remix

#connecting ganache
w3=Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

chain_id = 1337

my_address="0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"

#Never hardcode your private key  definr as environment varianle
private_key = "0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d"


#create contract in python

# 1.Build a contract
# 2.Deploy Transaction
# 3.Sign the transcation
# 4.Send the Transcation

simple_storage = w3.eth.contract(abi=abi,bytecode=bytecode)

#get latest transaction
nonce = w3.eth.get_transaction_count(my_address)
print(nonce)

# .Build a transaction
# .Sign a transaction
#.Send a transaction
transaction = simple_storage.constructor().build_transaction(
    {"chainId":chain_id,"from":my_address,"nonce":nonce}
)


signed_transaction= w3.eth.account.sign_transaction(transaction,private_key=private_key)

#send transaction to blockchain
transaction_hash= w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

#Working with the contract
#contract address
#contract ABI
simple_storage=w3.eth.contract(address=transaction_receipt.contractAddress,abi=abi)
# print(simple_storage.functions.retrieve().call())
# print(simple_storage.functions.store(15).call())

#Call -> Simulate making call
#Transact -> when it actually make state change


#create transaction
store_transactio=simple_storage.functons.store(15).buildTransaction(

    {"chainId":chain_id,"from":my_address,"nonce":nonce+1}
)

#signed transaction
signed_store_transaction=w3.eth.account.sign_transaction(
    store_transactio,private_key=private_key
)

#send the transaction

send_store_transaction=w3.eth.send_raw_transaction(signed_store_transaction.rawTransaction)

#Wait for confirmation

transaction_reciept=w3.eth.wait_for_transaction_receipt(send_store_transaction)















#calling view function