# Gmail Observer
# part of Port. 2.0
# (c) 2022
#
# Module observes an account in Gmail via IMAP. 
# 

import imaplib
import email

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
		
	def authenticate(self, acct=None, password=None):
		if not acct:
			acct = self.ACCT
		if not password:
			password = self.PASS
		self.session.login(acct, password)

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


	

