from brownie import FundMe, MockV3Aggregator, network, config
import scripts.helpful_scrips
from web3 import Web3

def deploy_fund_me():
    account = scripts.helpful_scrips.account
    # pass the price feed to contract
    # if we on persistent network use associated address
    # otherwise, deploy mocks
    if network.show_active() not in scripts.helpful_scrips.LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        scripts.helpful_scrips.deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fundMe = FundMe.deploy(
        price_feed_address,
        {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fundMe.address}")

def main():
    deploy_fund_me()