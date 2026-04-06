import database
import requester_limitless_api


class PoffinManager():
    def __init__(self):
        self.oc_requester = requester_limitless_api.LimitlessPTCGRequester()
        self.database = database.PoffinDatabase()
