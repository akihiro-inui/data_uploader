"""
@author: Akihiro Inui
"""
import os
import sys
import configparser
sys.path.insert(0, os.getcwd())


class ConfigReader:
    """
    Reading configuration file data. Define module specific configuration in different functions.
    """
    def __init__(self):
        """
        Read common configuration data from configuration file
        """
        # Read deployment
        self.DEPLOYMENT = os.environ.get('DEPLOYMENT')

        self.config_folder_path = os.path.join(f'app/config/{self.DEPLOYMENT}')
        assert os.path.isdir(self.config_folder_path), f"{self.config_folder_path} is not a valid configuration folder!" \
                                                       f"Working directory is {os.getcwd()}"
        cfg = configparser.ConfigParser()
        self.cfg = cfg

        # Read config files
        self.__init_database(cfg)

    def __init_database(self, cfg):
        # Check config file exist
        config_file_path = os.path.join(self.config_folder_path, 'db_config.ini')
        cfg.read(config_file_path)
        assert os.path.isfile(config_file_path), f"{config_file_path} is not a valid configuration file!"

        # Read parameters
        self.DATABASE_HOST = cfg.get('database', 'DATABASE_HOST')
        self.DATABASE_PORT = cfg.get('database', 'DATABASE_PORT')
        self.DATABASE_NAME = cfg.get('database', 'DATABASE_NAME')
        self.DATABASE_USER = cfg.get('database', 'DATABASE_USER')
        self.DATABASE_PASSWORD = cfg.get('database', 'DATABASE_PASSWORD')

