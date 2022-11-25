"""Entry point of this project, call with arguments to:

Get GitLab runner token from local GitLab server. Set GitHub ssh deploy
key. Set GitHub personal access token.
"""
import argparse

from .GitLab.restore_ublock_backup import RestoreUblockBackup
from .Hardcoded import Hardcoded
from .helper import get_browser_drivers

# get browser drivers
hardcoded = Hardcoded()
get_browser_drivers(hardcoded)

# Parse user arguments to determine what to do.
parser = argparse.ArgumentParser()
parser.add_argument(
    "--b0",
    dest="backup_zero",
    action="store_true",
    help="boolean flag, determines whether which backupfile is restored.",
)
parser.set_defaults(
    backup_zero=True,
)
args = parser.parse_args()
if args.backup_zero:
    _ = RestoreUblockBackup()


print("Done.")
