import configparser
import os

class Settings(object):
    def __init__(self, domain: str = None, path: str = None):
        d = os.path.join(os.path.dirname(__file__),  "../../settings.ini")
        self.path = d if path is None else path
        self.dmn = domain if domain is not None else 'default'
        self.config = configparser.ConfigParser()
        self.config.read(self.path) 
    
    def get(self, name: str, domain: str =None) -> str:
        domain = self.dmn if domain is None else domain
        return self.config.get(domain, name)

    def domain(self) -> str:
        return self.dmn