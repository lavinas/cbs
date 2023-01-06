from datetime import datetime, timedelta
from os.path import join, isfile
from os import listdir, remove
import gzip
import shutil

filePat = '{date}-{domain}.log'
messPat = '[{tag}] {datetime} | {status} | {message}\n'
dpattern = '%Y-%m-%d'
dtpattern = '%Y-%m-%d - %H:%M:%S'

class Log (object):
    def __init__(self, path: str, domain: str):
        self.path = path
        self.domain = domain
        self.file, self.now =  create(path, domain)
    
    def close(self):
        if self.file is not None:
            self.file.close()
            
    def rotate(self):
        now = datetime.now().strftime(dpattern)
        if self.now != now:
            self.close()
            self.file, self.now = create(self.path, self.domain)
    
    def info(self, tag: str, message: str, code: str = 'INFO'):
        if self.file is not None:
            self.rotate()
            write(self.file, tag, message, code)

    def error(self, tag: str, message: str, code: str = 'ERROR'):
        if self.file is not None:
            self.rotate()
            write(self.file, tag, message, code)
    
    def zip(self):
        pass

def create(path: str, domain: str):
    try:
        now = datetime.now().strftime(dpattern)
        name = filePat.format(date=now, domain=domain)
        log_file = join(path, name)
        file = open(log_file, 'a', encoding='utf-8')
        return file, now
    except Exception as e:
        return None, None    
    
def write(file: any, tag: str, message: str, code: str):
    d = datetime.now().strftime(dtpattern)
    m = messPat.format(tag=tag, datetime=d, status=code, message=message)
    file.write(m)
    file.flush()

def info(path, domain, tag, message, code = "INFO"):
    l = Log(path, domain)
    l.info(tag, message, code)
    l.close()
    
def error(path, domain, tag, message, code = "ERROR"):
    l = Log(path, domain)
    l.error(tag, message, code)
    l.close()
    
def zip_files(path: str):
    today = datetime.now().strftime(dpattern)
    yesterday = (datetime.now() - timedelta(days=1)).strftime(dpattern)
    for f in listdir(path):
        s = f.split(('.'))
        p = join(path, f)
        o = join(path, f.replace('.log', '') + '.gz')
        if not isfile(p) or s[len(s) -1] != 'log' or \
            today in f or yesterday in f:
            continue
        with open(p, 'rb') as f_in:
            with gzip.open(o, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        remove(p)