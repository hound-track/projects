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