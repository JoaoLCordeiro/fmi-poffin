
class PoffinParser():
    def __init__(self):
        pass

    def tour_req_to_tour_data(self, tour_req):
        if type(tour_req) is not list:
            raise ValueError

        aux_list = []
        for tournament in tour_req:
            parsed_tour = {}

            parsed_tour["id"] = tournament["id"]
            parsed_tour["date"] = tournament["date"]
            parsed_tour["players"] = tournament["players"]

            aux_list += [parsed_tour]

        return aux_list

    def tour_req_to_decklists_data(self, tour_req):
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

                aux_list += [parsed_decklist]

        return aux_list
