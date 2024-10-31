import os

admin_address = "" # set your address
admin_private_key = "" # set your private key

networks = {
    "Crab": {
        "token_decimals": 9,
        "ETH_RPC": "http://g1.crab2.darwinia.network",
        "NETWORK_ID": 44,
        "LAND_API": "https://backend.evolution.land/api/lands?district=4",
        "RESOURCE_FILE": "./conf/example_land_resource.json",
        "Land_ADDRESS": "",
        "GENESIS_HOLDER": "",
        "Gen0_ADDRESS": "",
        "RingTokenAddress": "",  # Ring token contract
        "ObjectOwnership": "",  # ObjectOwnership proxy contract
        "USER_ADDRESS": admin_address,  # Owner
        "CREATE_PRI_KEY": admin_private_key,  # Owner pri key
        "RANGE": [-22, 22, 23, 67],
        "PREFIX": "2a030001030001020000000000000003"
    },
}

current = networks[os.getenv("CHAIN", "Heco")]
