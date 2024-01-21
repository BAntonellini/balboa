import os
import dlt

def set_config_value(key, config_key, env_var_prefix = 'DATACOVES__MAIN__'):

    env_var = env_var_prefix + key.upper()

    value = os.getenv(env_var, dlt.config[config_key])

    return value

config_keys = ["account", "database", "warehouse", "role", "username", "password"]

db_config = {}
for key in config_keys:
    config_key = "destination.snowflake.credentials." + key

    try:
        dlt.config[config_key]
    except dlt.common.configuration.exceptions.ConfigFieldMissingException:
        dlt.config[config_key] = ''

    db_config[key] = set_config_value(key, config_key)

# This is needed because by default dlt calls the snowflake account host
db_config['host'] = db_config['account']
