# ---------------------------------------------------------------------------- #
#                                                                              #
# Arg Parse                                                                    #
#                                                                              #
# ---------------------------------------------------------------------------- #

import argparse

parser = argparse.ArgumentParser(__file__, description="GaPpi")
parser.add_argument("--development", "-dev", help="Dev Mode.", action="store_true")
parser.add_argument("--production", "-prod", help="Prod Mode.", action="store_true")

args = parser.parse_args()


# ---------------------------------------------------------------------------- #
#                                                                              #
#                               Launch                                         #
#                                                                              #
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    # if args.development:
    from config.configuration import WEB_IP, WEB_PORT_DEV
    from app import app

    app.run(host=WEB_IP, port=WEB_PORT_DEV, debug=True, threaded=True)
