from pymongo import MongoClient


class PoffinDatabase():
    def __init__(self, host="mongodb://localhost:27017/",
                 db_name="poffindb"):
        self.client = MongoClient(host)
        self.db = self.client[db_name]

        self.oc_tournaments_cname = "oc_tournaments"
        self.oc_decklists_cname = "oc_decklists"
        self.or_tournaments_cname = "or_tournaments"
        self.or_decklists_cname = "or_decklists"
        self.cards_cname = "cards"

        self._init_collections()

    def _init_collections(self):
        collections_name = [
            self.oc_tournaments_cname,
            self.oc_decklists_cname,
            self.or_tournaments_cname,
            self.or_decklists_cname,
            self.cards_cname
        ]

        existing_c = self.db.list_collection_names()

        for c_name in collections_name:
            if c_name in existing_c:
                self.db.create_collection(c_name)

        self.oc_tournaments = \
            self.db[self.oc_tournaments_cname]
        self.oc_decklists = \
            self.db[self.oc_decklists_cname]
        self.or_tournaments = \
            self.db[self.or_tournaments_cname]
        self.or_decklists = \
            self.db[self.or_decklists_cname]
        self.cards = \
            self.db[self.cards_cname]

    def _store_tournaments(self, oc_or, tournament_data):
        if oc_or == "oc":
            curr_db = self.oc_decklists
        elif oc_or == "or":
            curr_db = self.or_decklists
        else:
            raise ValueError

        # TODO: parse requester data to then use it here
        pass
