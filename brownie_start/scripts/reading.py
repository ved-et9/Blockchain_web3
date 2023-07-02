from brownie import accounts,SimpleStorage,network,config

def read():
    #when  using Simplestorage[0] we access the first deployment >.. We us SimpleStorage[-1] 
    #to get the latest deployment
    simple_storage=SimpleStorage[-1]

    # to interact we need address and ABI

    print(simple_storage.retrieve())

def main():
    read()

