# Gmail Observer
# part of Port. 2.0
# (c) 2022
#
# Module observes an account in Gmail via IMAP. 
# 

import imaplib
import email

GMAIL = "imap.gmail.com"
USER = "put@runport.io"

class GmailObserver:
	def __init__(self):
		self.service = None
		self.ACCT = None
		self.PASS = None

	def establish_session(self, service=None):
                if not service:
                        service = self.service
		self.session = imaplib.IMAP4_SSL(service)
		self.session.select()
		# defaults to inbox
		
##        def authenticate(self, acct=None, password=None):
##                if not acct:
##                        acct = self.ACCT
##                if not password:
##                        password = self.PASS
##                self.session.login(acct, password)

        def check_inbox(self):
                resp_code, mail_count = self.session.select("INBOX", readonly=True)
                print(resp_code, mail_count)

        def retrieve_mail_ids(self):
                resp_code, mails = self.session.search(None, "ALL")
                first_10 = mails[:9]
                return first_10
        
	def retrieve_emails(self, num=None):

		# gets num most recent emails		
		if not num:
			num = 10
			# make this a class var
		results = list()
		x = 0
		while x <= num:
			rv, msg = self.session.fetch(x, '(RFC822)')
			results.append(msg)
			x += 1
		return results
	
	def exit(self):	
		self.session.close()
		self.session.logout()

# get ids of first 10 emails
# get their bodies







