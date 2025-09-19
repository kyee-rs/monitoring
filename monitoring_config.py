from common import ValidatorConfig

config = ValidatorConfig(
    validator_name="Northgroup-Testnet",
    secrets_path="/home/firedancer",
    local_rpc_address="http://localhost:8899",
    remote_rpc_address="https://api.testnet.solana.com/",
    cluster_environment="testnet",
    debug_mode=False
)