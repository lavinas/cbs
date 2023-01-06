from sqlalchemy import create_engine
from typing import Any

class MySql(object):
    def __init__(self, settings: Any):
        self.sett = settings
        
    def begin(self):
        self.engine = get_engine(self.sett)
        self.conn = self.engine.connect()
        self.trans = self.conn.begin_nested()

    def close(self):
        self.conn.close()
        self.engine.dispose()
        
    def restart(self):
        self.conn.begin_nested()
        
    def commit(self):
        self.trans.commit()
        
    def rollback(self):
        self.trans.rollback()
        
    def execute(self, sql: str, params: dict) -> list:
        return list(self.conn.execute(sql, params))
    
def get_engine(setting: Any, domain: str) -> Any:
    host = setting.get_parameters('host', domain)
    user = setting.get_parameters('user', domain)
    passw = setting.get_parameters('pass', domain)
    db = setting.get_parameters('db', domain)
    pool = int(setting.get_parameters('pool_size', domain))
    max = int(setting.get_parameters('max_overflow', domain))
    url = "mysql+pymysql://" + user + ":" + passw + "@" + host
    if db is not None:
        url += "/" + db
    return create_engine(url, convert_unicode=True, echo=False, 
                        pool_size=pool, max_overflow=max)
