from brownie import FundMe
from scripts import helpful_scrips

def fund():
    fundMe = FundMe[-1]
    account = helpful_scrips.account
    entranceFee = fundMe.getEntranceFee()
    print(entranceFee)
    print(f"The current entry fee is {entranceFee}")
    print("Funding")
    fundMe.fund({"from": account, "value": entranceFee})

def withdraw():
    fundMe = FundMe[-1]
    account = helpful_scrips.account
    fundMe.withdraw({"from": account})

def main():
    fund()
    withdraw()