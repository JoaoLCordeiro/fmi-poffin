from pymongo import MongoClient
from pymongo.collection import Collection as MongoCollection


class PoffinDatabase():
    def __init__(self, host="mongodb://localhost:27017/",
                 db_name="poffindb"):
        self.client = MongoClient(host)
        self.db = self.client[db_name]

        self._oc_tournaments_cname = "oc_tournaments"
        self._oc_decklists_cname = "oc_decklists"
        self._or_tournaments_cname = "or_tournaments"
        self._or_decklists_cname = "or_decklists"
        self._cards_cname = "cards"

        self._init_collections()

    def _init_collections(self):
        collections_name = [
            self._oc_tournaments_cname,
            self._oc_decklists_cname,
            self._or_tournaments_cname,
            self._or_decklists_cname,
            self._cards_cname
        ]

        existing_c = self.db.list_collection_names()

        for c_name in collections_name:
            if c_name not in existing_c:
                self.db.create_collection(c_name)

        self._oc_tournaments: MongoCollection = \
            self.db[self._oc_tournaments_cname]
        self._oc_decklists: MongoCollection = \
            self.db[self._oc_decklists_cname]
        self._or_tournaments: MongoCollection = \
            self.db[self._or_tournaments_cname]
        self._or_decklists: MongoCollection = \
            self.db[self._or_decklists_cname]
        self._cards: MongoCollection = \
            self.db[self._cards_cname]

    def store_tournaments(self, oc_or, tournament_data):
        if oc_or == "oc":
            curr_db = self._oc_tournaments
        elif oc_or == "or":
            curr_db = self._or_tournaments
        else:
            raise ValueError

        for tournament in tournament_data:
            id = tournament["_id"]
            updt_filter = {"_id": id}
            updt = {"$set": tournament}

            result = curr_db.update_one(
                filter=updt_filter,
                update=updt,
                upsert=True
            )

            if result.acknowledged is False:
                raise RuntimeError

    def store_decklists(self, oc_or, decklists_data):
        if oc_or == "oc":
            curr_db = self._oc_decklists
        elif oc_or == "or":
            curr_db = self._or_decklists
        else:
            raise ValueError

        for decklist in decklists_data:
            id = decklist["_id"]
            updt_filter = {"_id": id}
            updt = {"$set": decklist}

            result = curr_db.update_one(
                filter=updt_filter,
                update=updt,
                upsert=True
            )

            if result.acknowledged is False:
                raise RuntimeError

    def read_all_tournaments(self, oc_or):
        if oc_or == "oc":
            collection = self._oc_tournaments
        elif oc_or == "or":
            collection = self._or_tournaments
        else:
            raise ValueError

        doc_list_aux = []

        cursor = collection.find({})
        for doc in cursor:
            doc_list_aux += [doc]

        return doc_list_aux

    def read_all_decklists(self, oc_or):
        if oc_or == "oc":
            collection = self._oc_decklists
        elif oc_or == "or":
            collection = self._or_decklists
        else:
            raise ValueError

        doc_list_aux = []

        cursor = collection.find({})
        for doc in cursor:
            doc_list_aux += [doc]

        return doc_list_aux
