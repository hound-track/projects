import json
import os

valid_chains = [1, 10, 56, 137, 250, 42161, 42220, 43114]


def test_project_index_size():
    """ test index == projects in directory """
    assert sorted([x.split('.')[0] for x in os.listdir("projects")]) == sorted(open("projects.txt", "r").read().split('\n'))


def test_project_formatting():
    for project in os.listdir("projects"):
        project_details = json.loads(open(f'projects/{project}', "r").read())
        assert project_details['name'] != ''
        assert project_details['description'] != ''
        assert project_details['url'] != ''
        assert project_details['image'] != ''
        assert len(project_details['contracts']) != 0

        for chain_id in project_details['contracts'].keys():
            assert int(chain_id) in valid_chains
            contracts = project_details['contracts'][chain_id]
            assert len(contracts) > 0
            for contract in contracts:
                assert contract['name'] != ''
                assert contract['address'] != ''
                assert len(contract['abi']) > 0
