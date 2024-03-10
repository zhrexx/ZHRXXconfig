import configparser

class Config:
    @staticmethod
    def get_config(*args):
        config = configparser.ConfigParser()
        config.read('config.ini')
        if len(args) >= 2:
            value = config.get(args[0], args[1])
            return value
        else:
            return None  # Or handle this case as per your requirement

# Usage:
# Assuming 'config.ini' exists and contains appropriate configuration
# Access the config value by passing section and key

