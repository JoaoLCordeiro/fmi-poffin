from . import database
from . import requester_limitless_api
from . import parser

from datetime import date

LAST_UPDATE_STR = "last_update"
FORCE_FULL_UPDATE_STR = "force_full_update"

STD_METADATA_PATH = "./config/poffin.metadata"
STD_CONFIG_PATH = "./config/poffin.conf"


class PoffinManager():
    def __init__(self):
        self.oc_requester = requester_limitless_api.LimitlessPTCGRequester()
        self.database = database.PoffinDatabase()
        self.parser = parser.PoffinParser()

    def get_last_update(self):
        """Get the last update date stored in the metadata file.
        Format: "YYYY-MM-DD"
        """

        config_fd = open(STD_METADATA_PATH, 'r')

        for line in config_fd:
            if LAST_UPDATE_STR in line:
                ignore_chars = len(LAST_UPDATE_STR) + 1

                value = line[ignore_chars:]
                break

        config_fd.close()

        return value

    def set_last_update(self, last_updt_date):
        """Set the last update date stored in the metadata file.
        Format: "YYYY-MM-DD"
        """

        config_fd = open(STD_METADATA_PATH, 'r')
        lines = config_fd.readlines()
        config_fd.close()

        for i in range(0, len(lines)):
            if LAST_UPDATE_STR in lines[i]:
                last_updt_str = \
                    LAST_UPDATE_STR + "=" + last_updt_date
                lines[i] = last_updt_str
                break

        config_fd = open(STD_METADATA_PATH, 'w')
        config_fd.writelines(lines)
        config_fd.close()

    def get_force_full_update(self):
        """Get the force full update setting stored in the config file.
        Format: true or false (boolean)
        """

        config_fd = open(STD_CONFIG_PATH, 'r')

        for line in config_fd:
            if FORCE_FULL_UPDATE_STR in line:
                ignore_chars = len(FORCE_FULL_UPDATE_STR) + 1

                value = line[ignore_chars:]
                bool_value = bool(value)
                break

        config_fd.close()

        return bool_value

    def update_database(self):
        # get info about the last update made
        # and if the user wants to force a full update
        force_full_update = self.get_force_full_update()
        if not force_full_update:
            last_update = self.get_last_update()
        else:
            last_update = None

        # get limitless data
        limitless_data = self.oc_requester.get_data(
            force_full_update=force_full_update,
            last_update=last_update
        )

        # parse obteined data
        tour_data = self.parser.tour_req_to_tour_data(limitless_data)
        deck_data = self.parser.tour_req_to_decklists_data(limitless_data)

        # storing limitless data
        self.database.store_tournaments("oc", tour_data)
        self.database.store_decklists("oc", deck_data)

        # updates last update metadata
        today = str(date.today())
        self.set_last_update(today)
