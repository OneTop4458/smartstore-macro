# -*- coding: utf-8 -*-

# config library
# example
# import config
# config.Config().set_config(config)
# config_file = config.Config().get_config()

import json
import os

import unittest

class Config:

    def __init__(self, config=None):
        self.config = config

    def get_config(self):
        try:
            with open('./config.json', 'r', encoding='utf-8') as json_file:
                json_data = json.load(json_file)
        except Exception as e:
            raise('Error in reading config file, {}'.format(e))
            return None
        else:
            return json_data

    def set_config(self, config):
        try:
            with open('./config.json', 'w', encoding='utf-8') as json_file:
                json.dump(config, json_file)
        except Exception as e:
            raise('Error in writing config file, {}'.format(e))


class Tests(unittest.TestCase):
    def test_save_config(self):
        if os.path.isfile("../config.json"):
            os.renames("../config.json", "config.json.bk")

        config = {'Test': 'config', 'AAA': "False"}
        Config().set_config(config)

        if not os.path.isfile("../config.json"):
            raise Exception("config file create Failed")
        else:
            print("Config File Create Success")

        if os.path.isfile("config.json.bk"):
            os.remove("../config.json")
            os.renames("config.json.bk", "../config.json")

    def test_load_config(self):
        if not os.path.isfile("../config.json"):
            raise Exception("Config File is not Found")

        config = Config().get_config()

        if config is None:
            raise Exception("Config File is null")
        else:
            print("Config File Load Success : {}".format(config))
