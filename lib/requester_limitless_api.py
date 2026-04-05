import requests
import json


class Requester():
    def __init__(self,
                 endpoint_base="https://play.limitlesstcg.com/api"):
        self.endpoint_base = endpoint_base

    def get_req(self, sufix_endpoint):
        endpoint = self.endpoint_base + sufix_endpoint
        response = requests.get(endpoint)

        return response.text


class LimitlessPTCGRequester(Requester):
    def __init__(self,
                 endpoint_base="https://play.limitlesstcg.com/api"):
        super().__init__(endpoint_base=endpoint_base)

    def _get_tornaments(self, game="PTCG", format="STANDARD", page=1):
        """Sends a request to get tournament data.
        """

        sufix_endpoint = \
            "/tournaments?game={}&format={}&page={}".format(
                game, format, str(page)
            )

        return self.get_req(sufix_endpoint)

    def _check_if_last_page(self, resp_list, last_update):
        """Check if the page have tournaments from before last update
        """

        last_updt_year = int(last_update[0:4])
        last_updt_month = int(last_update[5:7])
        last_updt_day = int(last_update[8:10])

        for tournament in resp_list:
            tournament_date = tournament["date"]

            curr_updt_year = int(tournament_date[0:4])
            curr_updt_month = int(tournament_date[5:7])
            curr_updt_day = int(tournament_date[8:10])

            if curr_updt_year < last_updt_year:
                return True
            elif (curr_updt_year == last_updt_year) &\
                 (curr_updt_month < last_updt_month):
                return True
            elif (curr_updt_year == last_updt_year) &\
                 (curr_updt_month == last_updt_month) &\
                 (curr_updt_day < last_updt_day):
                return True

        return False

    def _filter_tournament_date(self, resp_list, last_update):
        """Filters tournaments from before last update from a list
        """

        last_updt_year = int(last_update[0:4])
        last_updt_month = int(last_update[5:7])
        last_updt_day = int(last_update[8:10])

        aux_list = []

        for tournament in resp_list:
            tournament_date = tournament["date"]

            curr_updt_year = int(tournament_date[0:4])
            curr_updt_month = int(tournament_date[5:7])
            curr_updt_day = int(tournament_date[8:10])

            if curr_updt_year < last_updt_year:
                continue
            elif (curr_updt_year == last_updt_year) &\
                 (curr_updt_month < last_updt_month):
                continue
            elif (curr_updt_year == last_updt_year) &\
                 (curr_updt_month == last_updt_month) &\
                 (curr_updt_day < last_updt_day):
                continue

            aux_list += [tournament]

        return aux_list

    def _filter_tournament_opendecklists(self, tour_list):
        """Returns only the open descklist tournaments from a list
        """

        aux_list = []

        for tournament in tour_list:
            tour_id = tournament["id"]
            sufix_endpoint = "/tournaments/{}/details".format(
                tour_id)

            details_str = self.get_req(sufix_endpoint)
            details_dict = json.loads(details_str)

            is_opendecklist = details_dict["decklists"]

            if is_opendecklist:
                aux_list += [tournament]

        return aux_list

    def get_data(self, force_full_update=True, last_update=None):
        """Get tournament data, including standings.
        If force_full_update=True, gets data from all tournaments in
        the format. Otherwise, gets data from tournaments that occured
        on the last_update date and after.
        """

        if not force_full_update:
            if last_update is None:
                raise ValueError
        else:
            # first tournament legal post G-rotation
            last_update = "2026-03-27"

        last_update_reached = False
        curr_page = 1
        all_tournaments_list = []
        while not last_update_reached:
            resp_json = self._get_tornaments(page=curr_page)
            resp_list = json.loads(resp_json)

            if self._check_if_last_page(resp_list, last_update):
                filtered_list = self._filter_tournament_date(resp_list,
                                                             last_update)
                all_tournaments_list += filtered_list
                last_update_reached = True
            else:
                all_tournaments_list += resp_list
                curr_page += 1

        filtered_list = self._filter_tournament_opendecklists(
            all_tournaments_list)

        for tournament in filtered_list:
            tournament_id = tournament["id"]
            sufix_endpoint = "/tournaments/{}/standings".format(
                tournament_id
            )

            standings = self.get_req(sufix_endpoint)

            tournament["standings"] = standings

        return filtered_list
