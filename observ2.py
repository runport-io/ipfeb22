# observer 2
# (c) Port. Prerogative Club 2

import imaplib
import email

GMAIL = "imap.gmail.com"
USER = "put@runport.io"
INBOX = "INBOX"
UID = "UID"
FETCH = "FETCH"
SUBJECT = "BODY[HEADER.FIELDS (SUBJECT)]"

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

    Returns list of strings
    """
    
    # serial ids takes a list of bytestrings in UTF, returns same
    result = list()
    for serial_id in serial_ids:
       resp_code, data = session.fetch(serial_id, '(UID)')
       print(resp_code, data)
       # data is a list of one bytestring
       content = data[0].decode()
       # turns bytestring into regular string
       content = parse_parens(content)
       # processes content into a dictionary      
       result.append(content[UID])

    return result

def parse_parens(string, trace=False):
    """

    function expects string in format (x y)
    """
    result = dict()
    wip = ""
    start = False
    end = False
    for char in string:
        if trace:
            print(char)
            print("Start: ", start)
            print("End:   ", end)
        
        if char == "(":
            start = True
            if trace:
                print("Starting transcription")
                
            continue
        elif char == ")":
            end = True
            break
        if start and not end:
            wip = wip + char
            if trace:
                print("WIP:  ", wip)
            
    tokens = wip.split()
    result[tokens[0]] = tokens[1]
    
    return result

def get_subject_by_UID(session, uid):
    """

    returns string
    """
    result = ""
    # uid command requires UID to be passed in as string, not integer?
    status, data = session.uid(FETCH, uid, SUBJECT)
    # imap returns tuple of (code, content)

    response = data[0]
    # data comes back in the format of a list; the first item in the list is a
    # tuple of (command, response)
    command = response[0]
    subject = response[1]
    result = subject.decode()
    
    return result
    
def get_subjects(session, uids):
    """

    returns dictionary 
    """
    result = dict()
    for uid in uids:
        subject = get_subject_by_UID(session, uid)
        result[uid] = subject

    return result


session = establish_session()
authed = authenticate(session)
results = check_mail(authed)
ids = get_ids(authed, length=4)
print(ids)

uniques = get_UIDs(session, ids)
print(uniques)

headlines = get_subjects(session, uniques)
for item in headlines.items(): print(item)

# figure out what "=20" means, how to get rid of the unicode thingamajig.

# write the full email method
# wrap this in a class
# move auth somewhere like a file
# get last emails instead of first?
# figure out speed
# figure out storage: any? discard messages not in watchlist? or in top 100
