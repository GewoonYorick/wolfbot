PASS = ""
CHANNEL = ""
HOST = "irc.freenode.net"
PORT = 6667
NICK = "wolfbot"
OWNERS = ("unaffiliated/wolfbot_admin1",)  # the comma is required at the end if there is one owner
ADMINS = ("unaffiliated/wolfbot_admin2", "unaffiliated/wolfbot_admin3")
CMD_CHAR = "!"
CHANGING_HOST_QUIT_MESSAGE = "Changing host"
JOIN_AFTER_CLOAKED = True # Set to false if the bot does not have a cloak
DISABLE_DEBUG_MODE = False  # Entirely disable debug mode

# Argument --debug means start in debug mode
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')

args = parser.parse_args()
DEBUG_MODE = args.debug if not DISABLE_DEBUG_MODE else False