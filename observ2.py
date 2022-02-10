# observer 2
# (c) Port. Prerogative Club 2

import imaplib
import email

GMAIL = "imap.gmail.com"
USER = "put@runport.io"
INBOX = "INBOX"

def establish_session(service=GMAIL):
    session = imaplib.IMAP4_SSL(service)
    return session

def authenticate(session, user=USER):
    password = input("Password: ")
    session.login(user, password)
    return session

def check_mail(session, folder=INBOX):
    resp_code, mail_count = session.select(folder, readonly=True)
    print(resp_code, mail_count)
    return (resp_code, mail_count)

def get_ids(session, length=10):
    resp_code, mails = session.search(None, "ALL")
    print(resp_code, mails)
    # mails comes back as len-1 list [<bytes>], where <bytes> consists of 
    # integers separated by spaces.
    ids = mails[0].split()
    result = ids[:(length - 1)]
    return result

def get_UIDs(session, serial_ids):
    """
    Returns list of bytestrings
    """
    
    # serial ids takes a list of bytes
    result = list()
    for serial_id in serial_ids:
       resp_code, data = session.fetch(serial_id, '(UID)')
       print(resp_code, data)
       # data is a list of one bytestring
       result.append(data[0])
    return result

session = establish_session()
authed = authenticate(session)
results = check_mail(authed)
ids = get_ids(authed)
print(ids)

uniques = get_UIDs(session, ids)
print(uniques)

