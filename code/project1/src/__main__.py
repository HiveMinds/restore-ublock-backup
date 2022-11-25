"""Entry point of this project, call with arguments to:

Get GitLab runner token from local GitLab server. Set GitHub ssh deploy
key. Set GitHub personal access token.
"""
import argparse

from .Hardcoded import Hardcoded
from .helper import get_browser_drivers
from .restore_ublock_backup import RestoreUblockBackup

def mwe3():
    from selenium.webdriver.firefox.options import Options
    #from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium import webdriver
    options = Options()

    #help(options)

    options.add_argument('-profile')
    options.add_argument('/home/name/.mozilla/firefox/1k7nmeyz.default-release')

    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('useAutomationExtension', False)

    driver = webdriver.Firefox(options=options,executable_path=r"firefox_driver/geckodriver",)
    driver.get("about:support")

def mwe2():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options

    options=Options()

    ppath = '/home/name/.mozilla/firefox/1k7nmeyz.default-release'
    options.set_preference('profile', ppath)
    driver = webdriver.Firefox(options=options,executable_path=r"firefox_driver/geckodriver",)
    driver.get("about:support")


def mwe():
    from selenium import webdriver
    fp = webdriver.FirefoxProfile("/home/somename/.mozilla/firefox/1k7nmeyz.default-release")
    driver = webdriver.Firefox(
        executable_path=r"firefox_driver/geckodriver",
        firefox_profile=fp,    
    )
    driver.get("about:support")
#mwe3()
#mwe2()
#mwe()
#exit()

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
