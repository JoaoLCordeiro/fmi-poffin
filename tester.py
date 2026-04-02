#!/usr/bin/env python3

import sys
from lib.requester_limitless_api import LimitlessPTCGRequester


def main():
    requester = LimitlessPTCGRequester()
    response = requester.get_tornaments()

    print("response:")
    print(response)


if __name__ == "__main__":
    sys.exit(main())
