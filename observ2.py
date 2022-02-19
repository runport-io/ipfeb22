# Observer 2
# (c) Port. Prerogative Club 2022

"""

Module includes logic for monitoring a source of events.
------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:
GMAIL               URL for gmail's IMAP gateway
USER                id for the marketing inbox

FUNCTIONS:

CLASSES:
N/a
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins
import imaplib
import email
import json

# 2) Port. objects
import parser2

from constants import *

# 3) Constants
GMAIL = "imap.gmail.com"
USER = "put@runport.io"

# 4) Functions
def authenticate(session, guest, token=None):
    """

    authenticate() -> session

    Function authenticates session using the credentials you provide in the
    signature. If you don't specify a password, function will prompt you for it.
    """
    if not token:
        token = input("Token: ")
    session.login(guest, token)
    return session

def check_mail(session, folder=INBOX):
    """

    check_mail() -> tuple

    Function checks mail, returns (response code, mail count) in the folder you
    specify. You should provide a session that you have authenticated.
    """
    resp_code, mail_count = session.select(folder, readonly=True)
    print(resp_code, mail_count)
    return (resp_code, mail_count)

def establish_session(service=GMAIL):
    """

    establish_session() -> session

    Returns istance of IMAP4_SSL object. This function does not perform
    authentication.
    """
    session = imaplib.IMAP4_SSL(service)
    return session

def get_body(msg, glue=NEW_LINE, trace=False):
    """

    get_body(msg, glue, trace) -> string

    Returns a string connected by glue that represents the body of a message.
    """
    result = ""
    body_lines = get_body_lines(msg, trace=trace)
    result = glue.join(body_lines)
    return result

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
            wip.extend(body_lines)

    #truncate
    if limit:
        wip = wip[:limit]

    result = wip
    return result

    # only works when body is in plain text

def get_first(session, number=BATCH_SIZE):
    """

    get_first() -> list

    Function returns a list of "email" objects of size "number", or BATCH_SIZE
    by default. The emails will be the oldest in the mailbox.
    """
    result = list()
    ids = get_ids(session)
    ids = ids[:BATCH_SIZE]
    uids = get_UIDs(session, ids)
    for uid in uids:
        msg = get_message_by_UID(session, uid)
        result.append(msg)

    return result

def get_ids(session, length=None, trace=False):
    """

    get_ids() -> list()

    Function returns list of strings of ids. Function retrieves serial ids that
    change over time. If you specify "length", function truncates the list of
    ids. Function prints the result if "trace" is True.  
    """
    result = None
    resp_code, mails = session.search(None, "ALL")
    # mails comes back as len-1 list [<bytes>], where <bytes> consists of 
    # integers separated by spaces.
    
    result = mails[0].split()
    # truncate if necessary
    if length:
        result = result[:(length - 1)]

    if trace:
        print(result)
    
    return result

def get_last(session, number=BATCH_SIZE):
    """

    get_first() -> list

    Function returns a list of "email" objects of size "number", or BATCH_SIZE
    by default. The emails will be the newest in the mailbox.
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

def get_message_by_UID(session, uid):
    """

    get_message_by_UID() -> email

    Function expects a string for UID. Function returns an "email" object from
    the built-in library. 
    """
    msg = None
    code, data = session.uid(FETCH, uid, RFC822)
    response = data[0]
    command = response[0]
    content = response[1]
    msg = email.message_from_bytes(content)
    return msg


def get_subject_by_UID(session, uid):
    """

    get_subject_by_UID() -> string

    Function expects the UID to be a string. Function collects the subject
    through IMAP.
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

def get_subject2(session, uid):
    """

    get_subject() -> string

    Function retrieves the message and uses the "email" object to extract the
    subject. You should use a string for UID.  
    """
    subject = ""
    
    msg = get_message_by_UID(session, uid)
    # msg is in email format
    subject = msg.get(EMAIL_LIB_SUBJECT)

    return subject

def get_subjects(session, uids):
    """

    get_subjects() -> dict

    Function expects a list of strings of UIDs. Function returns a dictionary
    keyed by UID, with raw strings as values. 
    """
    result = dict()
    for uid in uids:
        subject = get_subject_by_UID(session, uid)
        result[uid] = subject

    return result

def get_UIDs(session, serial_ids):
    """

    get_UIDs() -> list()

    Function expects an authenticated session and a list of bytestrings.
    Function returns a list of bytestrings.
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
    # <-----------------------------------------------------review routine

def load_credentials():
    """

    load_credentials() -> tuple
    
    Reads credentials from file. Returns a (guest, token).
    """
    # should expand this to non-managed dir
    # step up one level in folder, then make credentials
    file = open(file_name, "r")
    creds = json.load(file)
    guest = creds[GUEST]
    token = creds[TOKEN]
    
    return guest, token

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

def unpack_response(response):
    pass
    # deliver the content

# Testing
def run_tests():
    
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

if __name__ == "__main__":
    run_tests()

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

## operation:
# construct event
# return events
# move offset
# clear memory

