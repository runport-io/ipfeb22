# Manager

import email_observer
import observ2

marketing_inbox = email_observer.EmailObserver()
credentials = observ2.load_credentials()
guest, token = credentials
market_inbox.activate(token)

# now ready to get events


