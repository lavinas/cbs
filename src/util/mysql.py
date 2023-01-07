from sqlalchemy import create_engine
from typing import Any

user_set = 'user'
pass_set = 'pass'
host_set = 'host'
db_set = 'db'
pool_set = 'pool_size'
overflow_set = 'max_overflow'

class MySql(object):
    def __init__(self, sett: Any):
        self.engine = get_engine(sett)
        self.conn = self.engine.connect()
 
    def close(self):
        self.conn.close()
        self.engine.dispose()
        
    def begin(self):
        self.trans = self.conn.begin_nested()
        
    def commit(self):
        self.trans.commit()
        
    def rollback(self):
        self.trans.rollback()
        
    def query(self, sql: str, params: dict) -> list:
        return list(self.conn.execute(sql, params))

    def exec(self, sql: str, params: dict) -> list:
        self.conn.execute(sql, params)

def get_engine(sett: Any) -> Any:
    url = 'mysql+pymysql://{u}:{p}@{h}/{d}'.format(
        u = sett.get(user_set),
        p = sett.get(pass_set),
        h = sett.get(host_set),
        d = sett.get(db_set)
    )
    p = int(sett.get(pool_set))
    m = int(sett.get(overflow_set))
    return create_engine(url, convert_unicode=True, echo=False, 
                        pool_size=p, max_overflow=m)
