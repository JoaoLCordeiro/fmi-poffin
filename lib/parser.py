
class PoffinParser():
    def __init__(self):
        pass

    def tour_req_to_tour_data(self, tour_req):
        """ Get tournament request response and returns it
        parsed to get stored in database.

        Returned format:
            _id: tournament id
            date: date of the tournament
            players: number of pplayers in tournament
        """

        if type(tour_req) is not list:
            raise ValueError

        aux_list = []
        for tournament in tour_req:
            parsed_tour = {}

            parsed_tour["_id"] = str(tournament["id"])
            parsed_tour["date"] = tournament["date"]
            parsed_tour["players"] = tournament["players"]

            aux_list += [parsed_tour]

        return aux_list

    def tour_req_to_decklists_data(self, tour_req):
        """ Get standings request response and returns it
        parsed to get stored in database.

        Returned format:
            _id: tournament id + '_' + placing in tournament
            id: tournament id
            placing: decklist placing in tournament
            record: wins, losses and ties
            decklist: all cards in decklist
        """

        if type(tour_req) is not list:
            raise ValueError

        aux_list = []
        for tournament in tour_req:
            standings = tournament["standings"]
            for player in standings:
                parsed_decklist = {}

                parsed_decklist["id"] = tournament["id"]
                parsed_decklist["placing"] = player["placing"]
                parsed_decklist["record"] = player["record"]
                parsed_decklist["decklist"] = player["decklist"]

                id = parsed_decklist["id"]
                placing = parsed_decklist["placing"]

                parsed_decklist["_id"] = str(id) + "_" + str(placing)

                aux_list += [parsed_decklist]

        return aux_list
