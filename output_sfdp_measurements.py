from monitoring_config import config
from measurement_sfdp_info import calculate_output_data
from common import print_json

print_json(calculate_output_data(config))
