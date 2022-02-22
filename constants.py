# constants
# (c) Port. Prerogative Club 2022

TIME_ZERO = (2022, 2, 24, 0, 0, 0, 0, 0, 0)

# ATTRIBUTES
SKIP_ATTRIBUTES = "SKIP_ATTRIBUTES"
TO_PRINT ="TO_PRINT"

# COMMANDS

# Services
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
APOSTROPHE = "'"
AT = "@"
CARRIAGE_RETURN = "\r"
COLON = ":"
COMMA = ","
EMPTY_STRING = ""
EQUALS = "="
FWD_SLASH = "/"
HYPHEN = "-"
NEW_LINE = "\n"
QUESTION_MARK = "?"
SEMICOLON = ";"
SPACE = " "
TAB = "\t"
UNDER = "_"

BREAKS = [NEW_LINE, CARRIAGE_RETURN, TAB]

# Credentials
FILE_NAME = "credentials.json"
GUEST = "guest"
TOKEN = "token"

STANDARD_WIDTH = 18

# UUIDs
TEST_STRING = "4be0643f-1d98-573b-97cd-ca98a65347dd"

# ENCODING
UTF8 = "utf-8"

# Headers
CHARSET = "charset"
CONTENT_ENCODING="Content-Transfer-Encoding"
CONTENT_TYPE = "Content-Type"
##FIELDS = [CHARSET, CONTENT_ENCODING, CONTENT_TYPE]
