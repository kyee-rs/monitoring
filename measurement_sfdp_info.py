import time
import solana_rpc as rpc
from common import debug
from common import ValidatorConfig
import statistics
import numpy as np
import sfdp_info as sfdp
from common import measurement_from_fields

def load_data(config: ValidatorConfig):
    identity_account_pubkey = rpc.load_identity_account_pubkey(config)
    default = []
    sfdp_data = default
    sfdp_data = sfdp.sfdp_rpc_call(config, identity_account_pubkey)

    result = {
        'identity_account_pubkey': identity_account_pubkey,
        'sfdp_data': sfdp_data
    }

    debug(config, str(result))

    return result

def calculate_influx_fields(data):
    if data is None:
        result = {"sfdp_data": 0}
    else:
        identity_account_pubkey = data['identity_account_pubkey']
        result = data['sfdp_data']
    return result

def calculate_output_data(config: ValidatorConfig):
    data = load_data(config)

    measurement = measurement_from_fields(
        "sfdp_data",
        calculate_influx_fields(data),
        config
    )

    return measurement