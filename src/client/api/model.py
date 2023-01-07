from typing import Any

class Model(object):
    def __init__(self, conn: Any):
        self.conn = conn
        
    def close(self):
        self.conn.close()        
    
    def post(self, args: dict):
        self.conn.begin()
        self.conn.exec(sql_post, args)
        self.conn.commit()

        
sql_post = '''
    insert into client (
        name, surname, document, phone, email
    ) values (
        %(name)s, %(surname)s, %(document)s, %(phone)s, %(email)s
    );
'''