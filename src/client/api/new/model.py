from typing import Any
from decimal import Decimal

class Model(object):
    def __init__(self, conn: Any):
        self.conn = conn
              
    def insert(self, args: dict):
        self.conn.begin()
        self.conn.exec(sql_insert, args)
        self.conn.commit()
        
    def nick_count(self, nick) -> int:
        p = {'nick': nick}
        r = self.conn.query(sql_nick_count, p)
        return r[0].count
    
    def document_count(self, document: Decimal) -> int:
        p = {'document': document}
        r = self.conn.query(sql_document_count, p)
        return r[0].count
    
             
sql_insert = '''
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

sql_document_count = '''
    select count(1) count
      from client
    where document = %(document)s;
'''
