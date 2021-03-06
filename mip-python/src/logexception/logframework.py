'''
Create a logging framework to collect all the logs into a single file .Please follow all the tasks below.

 - Make the logger customisable, with settings being retrieved from a configuration file
 - Create the logging framework; every time the logger is invoked, it should log into a single file
 - The logging format has to be generic with the module_name, function_name, line_no : message
'''

import yaml
import logging
import logging.config

def setup_logging(default_level=logging.INFO):
    with open("logging.yaml", 'rt') as f:
        configdata = yaml.safe_load(f.read())
    logging.config.dictConfig(configdata)
