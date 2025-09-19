from common import ValidatorConfig
import requests
from common import debug


def sfdp_rpc_call(config: ValidatorConfig, identity_account_pubkey: str):

    address = "https://api.solana.org/api/validators/" + identity_account_pubkey

    try:
        debug(config, address)
        json_response = requests.get(address, timeout=5).json()
        if 'kycStatus' not in json_response:
            result = {}
        else:
            result = json_response
    except:
        result = {}

    debug(config, result)

    return result