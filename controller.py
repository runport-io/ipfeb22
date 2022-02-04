# Controller
# part of Port. 2.0
# (c) 2022
# 
# Module manages flow of information
#

from . import observer

# launch observers
marketing = observer.GmailObserver("marketing")
# add marketing login

personal = observer.GmailObserver("personal")
# add personal login

# set up storage, one file per co?
# set up delivery interface

def do_smtg(x):
	pass
	# results = marketing.check()
	# storage.store(results)
	# results2 = personal.check()
	# storage.store(results2)
	## results should be now stored in SSOT, single timeline, by timestamp, with offset
	## 

def get_events(offset=0, batch=None):
	pass
	# returns batch of events starting at offset
	




