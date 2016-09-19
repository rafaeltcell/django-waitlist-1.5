from waitlist.models import WaitlistEntry
from waitlist.models import Notification

class LoadEntriesMiddleware(object):

    def process_request(self, request):
        waitlist_entries = WaitlistEntry.objects.all()
        print(waitlist_entries)
        print(Notification)
        # allowed_ips = ['192.168.1.1', '123.123.123.123', etc...] # Authorized ip's
        # ip = request.META.get('REMOTE_ADDR') # Get client IP
        # if ip not in allowed_ips:
            # raise Http403 # If user is not allowed raise Error

        # If IP is allowed we don't do anything
        return None
