# observer 2
# (c) Port. Prerogative Club 2

import imaplib
import email
import json

import parser2

GMAIL = "imap.gmail.com"
USER = "put@runport.io"

# IMAP commands and strings
INBOX = "INBOX"
UID = "UID"
FETCH = "FETCH"
SUBJECT = "BODY[HEADER.FIELDS (SUBJECT)]"
RFC822 = "(RFC822)"

# Email fields
EMAIL_LIB_FROM = "From"
EMAIL_LIB_DATE = "Date"
EMAIL_LIB_SUBJECT = "Subject"
PLAIN_TEXT = "text/plain"

# Ops
BATCH_SIZE = 10

# Parsing
SPACE = " "
NEW_LINE = "\n"

# Credentials
file_name = "credentials.json"
GUEST = "guest"
TOKEN = "token"


def load_credentials():
    """
    Reads credentials from file

    """
    # should expand this to non-managed dir
    # step up one level in folder, then make credentials
    file = open(file_name, "r")
    creds = json.load(file)
    guest = creds[GUEST]
    token = creds[TOKEN]
    
    return guest, token

def establish_session(service=GMAIL):
    session = imaplib.IMAP4_SSL(service)
    return session

def authenticate(session, guest, token=None):
    if not token:
        token = input("Token: ")
    session.login(guest, token)
    return session

def check_mail(session, folder=INBOX):
    resp_code, mail_count = session.select(folder, readonly=True)
    print(resp_code, mail_count)
    return (resp_code, mail_count)

def get_ids(session, length=None):
    """
    returns list
    """
    result = None
    resp_code, mails = session.search(None, "ALL")
    # mails comes back as len-1 list [<bytes>], where <bytes> consists of 
    # integers separated by spaces.
    
    result = mails[0].split()
    # truncate if necessary
    if length:
        result = result[:(length - 1)]

    print(result)
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
       content = parser2.parse_parens(content)
       # processes content into a dictionary      
       result.append(content[UID])

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

def get_message_by_UID(session, uid):
    msg = None
    code, data = session.uid(FETCH, uid, RFC822)
    response = data[0]
    command = response[0]
    content = response[1]
    msg = email.message_from_bytes(content)
    return msg

def get_subjects(session, uids):
    """

    returns dictionary 
    """
    result = dict()
    for uid in uids:
        subject = get_subject_by_UID(session, uid)
        result[uid] = subject

    return result

#
def unpack_response(response):
    pass
    # deliver the content

def get_subject2(session, uid):
    subject = ""
    msg = get_message_by_UID(session, uid)
    # msg is in email format
    subject = msg.get(EMAIL_LIB_SUBJECT)
    return subject

def get_first(session, number=BATCH_SIZE):
    result = list()
    ids = get_ids(session)
    ids = ids[:BATCH_SIZE]
    uids = get_UIDs(session, ids)
    for uid in uids:
        msg = get_message_by_UID(session, uid)
        result.append(msg)

    return result

def get_last(session, number=BATCH_SIZE):
    """
    returns email objects
    """
    # should really run on slice syntax
    result = list()
    ids = get_ids(session)
    ids = ids[-BATCH_SIZE:]
    uids = get_UIDs(session, ids)
    for uid in uids:
        msg = get_message_by_UID(session, uid)
        result.append(msg)

    return result

def print_timestamp_and_subject(messages, clean=True):
    for message in messages:

        timestamp = message.get(EMAIL_LIB_DATE)
        print("Date:         ", timestamp)

        sender = message.get(EMAIL_LIB_FROM)
        print("From:         ", sender)
        
        subject = message.get(EMAIL_LIB_SUBJECT)
        print("Subject (R):  ", subject)

        if clean:
            cleaned = parser2.clean_string(subject)
            print("Subject (C):  ", cleaned)

# what about capitalization of titles?
# what happens if I pass in wrong uid?

def get_body_lines(msg, limit=None, trace=False):
    """

    
    As described at https://coderzcolumn.com/tutorials/python/imaplib-simple-guide-to-manage-mailboxes-using-python
    """
    result = list()
    wip = list()
    for part in msg.walk():
        if trace:
            print("Part:          \n")
            print(part)
        content_type = part.get_content_type()
        if trace:
            print("Content type:  \n")
            print(content_type)
        if content_type == PLAIN_TEXT:
            body_lines = part.as_string().split(NEW_LINE)
            wip.append(body_lines)

    #truncate
    if limit:
        wip = wip[:limit]

    result = wip
    return result

def get_body(msg, glue=NEW_LINE, trace=false):
    """

    get_body(msg, glue, trace) -> string

    Returns a string connected by glue that represents the body of a message.
    """
    result = ""
    body_lines = get_body_lines(msg, trace=trace)

session = establish_session()
guest, token = load_credentials()
authed = authenticate(session, guest, token)
results = check_mail(authed)
ids = get_ids(authed)
first_four = ids[:4]
print(first_four)

last_four = ids[-4:]
print(last_four)
uniques = get_UIDs(session, last_four)
print(uniques)

headlines = get_subjects(session, uniques)
for item in headlines.items(): print(item)

messages = list()
for uid in uniques:
    msg = get_message_by_UID(session, uid)
    messages.append(msg)

cleaned_subjects = list()
for msg in messages:
    subject = msg.get(EMAIL_LIB_SUBJECT)
    print("Raw:     ", subject)
    cleaned = parser2.clean_string(subject)
    print("Cleaned: ", cleaned)
    cleaned_subjects.append(cleaned)

first_msgs = get_first(session, number=5)
print("******first******")
print_timestamp_and_subject(first_msgs)

last_msgs = get_last(session, number=5)
print("******last******")
print_timestamp_and_subject(last_msgs)

body1 = get_body(last_msgs[0])
print("Body of first most-recent email:  \n")
print(body1)

body2 = get_body(last_msgs[1])
print("Body of second most-recent email:  \n")
print(body2)


# figure out what "=20" means, how to get rid of the unicode thingamajig.
# flow: keep the first 100 messages, and dim x watchlist?
## works only for each pull

# write the full email method
# wrap this in a class
# move auth somewhere like a file
# get last emails instead of first?
# figure out speed
# figure out storage: any? discard messages not in watchlist? or in top 100

## on class: store creds.

# need to parse out the html and links somehow.
# put the strings through cleaner.
