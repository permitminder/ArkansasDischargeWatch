"""
State configuration for this ArkansasDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "AR"
STATE_NAME = "Arkansas"
APP_NAME = "ArkansasDischargeWatch"
APP_TAGLINE = "Arkansas Discharge Monitoring"
DOMAIN = "arkansasdischargewatch.org"
DATA_FILE = "ar_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@arkansasdischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "CST"
EPA_REGION = 6
