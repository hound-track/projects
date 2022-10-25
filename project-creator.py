from collections import defaultdict
from time import sleep

import requests
import json
import sys

PROJECT_INDEX = 'projects.txt'


def get_contract_data(url: str, name: str, address: str):
    abi = requests.get(url).json()
    if 'status' not in abi:
        print(f'Added Contract {chain_id}-{name}-{address}')
        return {
            "name": name,
            "address": address,
            "abi": abi
        }
    else:
        print(abi)
        print('Contract add failed, retry')
        sleep(1)
        return get_contract_data(url, name, address)


if __name__ == '__main__':
    contracts_file_path = sys.argv[1]
    project_index = open(PROJECT_INDEX, "r").read().split('\n')
    project_id = input("Enter project id: ")
    assert project_id not in project_index

    project_name = input("Enter project name: ")
    project_description = input("Enter project description: ")
    project_url = input("Enter project URL: ")
    project_image = input("Enter project image: ")

    contracts = defaultdict(list)

    contract_list = open(contracts_file_path, "r").read().split('\n')
    for contract in contract_list:
        try:
            [chain_id, name, address] = contract.split(",")
            if chain_id == "1":
                contracts[chain_id].append(get_contract_data(
                    f"https://api.etherscan.io/api?module=contract&action=getabi&address={address}&format=raw",
                    name,
                    address))
            elif chain_id == "10":  # Optimism
                contracts[chain_id].append(get_contract_data(
                    f"https://api-optimistic.etherscan.io/api?module=contract&action=getabi&address={address}&format=raw",
                    name,
                    address))
            elif chain_id == "56":  # bsc
                contracts[chain_id].append(get_contract_data(
                    f"https://api.bscscan.com/api?module=contract&action=getabi&address={address}&format=raw",
                    name,
                    address))
            elif chain_id == "137":  # matic
                contracts[chain_id].append(get_contract_data(
                    f"https://api.polygonscan.com/api?module=contract&action=getabi&address={address}&format=raw",
                    name,
                    address))
            elif chain_id == "42161":  # arbitrum
                contracts[chain_id].append(get_contract_data(
                    f"https://api.arbiscan.io/api?module=contract&action=getabi&address={address}&format=raw",
                    name,
                    address))
            elif chain_id == "42220":  # celo
                contracts[chain_id].append(get_contract_data(
                    f"https://explorer.celo.org/mainnet/api?module=contract&action=getabi&address={address}",
                    name,
                    address))
            elif chain_id == "43114":  # avax
                contracts[chain_id].append(get_contract_data(
                    f"https://api.snowtrace.io/api?module=contract&action=getabi&address={address}&format=raw",
                    name,
                    address))
        except Exception as e:
            print(e)

    project = {
        "name": project_name,
        "description": project_description,
        "url": project_url,
        "image": project_image,
        "contracts": contracts
    }

    with open(PROJECT_INDEX, "a") as f:
        f.write('\n')
        f.write(project_id)

    with open(f'projects/{project_id}.json', 'w') as f:
        json_object = json.dumps(project, indent=2)
        f.write(json_object)

    print("Project created successfully")
