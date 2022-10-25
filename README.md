# Add New Project

To add a new project, create a new json file `<your_project>.json` under `projects` directory named after your project.

The json file should contain the following fields:

```json
{
  "name": "<Project Name>",
  "description": "<Project Description>",
  "url": "<Project url>",
  "image": "<Project image url>",
  "contracts": {
    "chainId": [
      {
        "name": "<Contract Name>",
        "address": "<Contract Address>",
        "abi": "<Contract ABI>"
      },
      ...
    ]
  }
}
```

## Project Creator

```bash
$ python project-creator.py contracts_input.txt
```

`contracts_input.txt` in this format chain_id,contract_name,address

```text
1,LendingPoolAddressesProvider,0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5
1,LendingPoolAddressesProviderRegistry,0x52D306e36E3B6B02c153d0266ff0f85d18BCD413
1,LendingPool,0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9
```