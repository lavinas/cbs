import configparser
import os
import sys

class Settings(object):
    def get_parameters(self, name, group=None):
        config = configparser.ConfigParser()
        config.read(
            os.path.join(os.path.dirname(__file__), "../../settings.ini")
        )
        ret = None
        for i in sys.argv:
            if i.lower().startswith(name + "="):
                ret = i[len(name + "="):]
        if not ret:
            group = group if group is not None else "parameters"
            ret = config.get(group, name)
        return ret
