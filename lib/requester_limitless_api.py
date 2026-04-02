import requests


class Requester():
    def __init__(self,
                 endpoint_base="https://play.limitlesstcg.com/api"):
        self.endpoint_base = endpoint_base

    def get_req(self, sufix_endpoint):
        endpoint = self.endpoint_base + sufix_endpoint
        response = requests.get(endpoint)

        print(endpoint)

        return response.text


class LimitlessPTCGRequester(Requester):
    def __init__(self,
                 endpoint_base="https://play.limitlesstcg.com/api"):
        super().__init__(endpoint_base=endpoint_base)

    def _get_tornaments(self, game="PTCG", format="STANDARD"):
        sufix_endpoint = \
            "/tournaments?game={}&format={}".format(
                game, format
            )

        return self.get_req(sufix_endpoint)

    def update_database(self, force_full_update=False):
        # connect to database (create if don't exist)

        # if (force_full_update == False) read database
        # metadata to check when was the last update

        # get tournaments that weren't saved
        # for each tournament:
        #   save these info:
        #     - date
        #     - player quantity
        #   get all deckslists and save these info for each:
        #     - tournament id
        #     - decklist
        #     - standing
        #     - wins
        #     - losses
        #     - ties

        # the decklists are saved in other collection

        pass
