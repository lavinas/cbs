from typing import Any

class Model(object):
    def __init__(self, conn: Any):
        self.conn = conn
              
    def post(self, args: dict):
        self.conn.begin()
        self.conn.exec(sql_post, args)
        self.conn.commit()
        
    def nick_count(self, nick) -> int:
        p = {'nick': nick}
        r = self.conn.query(sql_nick_count, p)
        return r[0].count
             
sql_post = '''
    insert into client (
        name, nickname, document, phone, email
    ) values (
        %(name)s, %(nickname)s, %(document)s, %(phone)s, %(email)s
    );
'''

sql_nick_count = '''
    select count(1) count
      from client
    where nickname = %(nick)s;
'''