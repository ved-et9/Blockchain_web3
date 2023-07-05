from brownie import accounts,FundMe,network
from scripts.helping_script import get_account

def deploy_fund():
    account=get_account()
    #need to pass address as constructor is called
    # by default
    fund_me=FundMe.deploy("0x5629a048466054Cd121494370eD26562e6ABFeBF",{"from":account},publish_source=True)
    print("Contract deployed to {fund_me.address}")


def main():
    deploy_fund()