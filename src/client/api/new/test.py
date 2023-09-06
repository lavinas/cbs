import unittest
from .... import get_app 
from .control import NewClient

class TestClientNew(unittest.TestCase):
    def test_run_ok(self):
        self.app.app_context()
        self.control.run()
    
    def setUp(self):
        self.app = get_app()
        self.control = NewClient(Settings(), Db(), Log())


# mocks
class Settings(object):
    pass

class Db(object):
    pass

class Log(object):
    pass

if __name__ == '__main__':
    unittest.main()