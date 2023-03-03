from ofxparse import OfxParser
from codecs import open

with open('/home/paulo/Downloads/2023-02.ofx', encoding='latin-1') as fofx:
    ofx = OfxParser.parse(fofx)

print(ofx.account.institution.organization)

for transaction in ofx.account.statement.transactions:
    print('----------------------------------')
    print('Payee', transaction.payee)
    print('Type', transaction.type)
    print('Date', transaction.date)
    print('User date', transaction.user_date)
    print('Amount', transaction.amount)
    print('Id', transaction.id)
    print('Memo', transaction.memo)
    print('Sic', transaction.sic)
    print('Mcc', transaction.mcc)
    print('Checksum', transaction.checknum)   
    print('----------------------------------')
    
    