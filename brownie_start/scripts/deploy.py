from brownie import accounts,config,SimpleStorage,network



def deploy_simple_storage():
    #using ganache cli
    account = get_account()

    Simple_st=SimpleStorage.deploy({"from" : account})
    stored_value= Simple_st.retrieve()

    print(stored_value)

    transaction = Simple_st.store(765,{"from":account})
    transaction.wait(1)
    updated_value=Simple_st.retrieve()
    print(updated_value)

def get_account():  
    if network.show_active() == "development":
        return accounts[0] 
    else:
        return accounts.load("real")

    #using testnet
    #good choice as privatekey is not pushed anywhere
    #account = accounts.load("vedet")


    #using environment variable and brownie config
    # account=accounts.add(config["wallets"]["from_key"])
    # print(account)

def main():
    deploy_simple_storage()



# Cli-Instruction
# brownie accounts new <accout name>  {creates new account}