import pynsive

from glob import glob

import re
import sys


class Engine(object):

    def __init__(self, checks_location, total_rounds=None, current_round=None):
        self.checks = []
        self.current_round = current_round
        self.total_rounds = total_rounds
        self.checks_location = checks_location

    def add_check(self, check_obj):
        self.checks.append(check_obj)

    def load_checks(self):
        sys.path.append(self.checks_location)
        print("Loading checks from " + self.checks_location)
        self.plugin_manager = pynsive.PluginManager()
        self.plugin_manager.plug_into(self.checks_location)
        checks_path = self.checks_location.split('/')[-1]

        for protocol in glob(self.checks_location + "/*"):
            protocol_name = protocol.replace(self.checks_location + '/', '')
            print("\tProtocol: " + protocol_name)
            for filename in glob(protocol + "/*"):
                check_filename = filename.replace(self.checks_location + '/' + protocol_name + '/', '')
                print("\t\tCheck Filename: " + check_filename)

                check_source_str = open(filename, 'r').read()
                check_classname = re.search('\nclass (\w+)', check_source_str).group(1)
                check_file_module = __import__(protocol_name + '.' + check_filename.replace('.py', ''), fromlist=[check_classname])
                check_class_attr = getattr(check_file_module, check_classname)
                print("\t\t\tCheck Classname: " + check_class_attr.name)
                self.add_check(check_class_attr)

        return self.checks

    def run(self, num_checks=None):
        if num_checks is None:
            print("Running until process is killed")
        else:
            print("Running " + num_checks + " times")

    def stop(self):
        print("Stopping Engine")