"""Object to run code based on incoming arguments."""
import os
import time

from src.restore_ublock_backup.get_ext_id import get_ext_id
from src.restore_ublock_backup.Hardcoded import Hardcoded
from src.restore_ublock_backup.helper import get_browser_drivers, open_url
from src.restore_ublock_backup.Website_controller import Website_controller


# pylint: disable=R0903
class RestoreUblockBackup:
    """Gets the GitLab runner from the GitLab server."""

    def __init__(self):
        """Initialises object that gets the browser controller, then it gets
        the issues from the source repo, and copies them to the target repo.

        :param login: [Boolean] True if the website_controller object should be
        created and should login to GitHub.
        """

        # Store the hardcoded values used within this project
        self.h_c = Hardcoded()

        # get browser drivers
        get_browser_drivers(self.h_c)
        website_controller = Website_controller()
        time.sleep(1)

        # Get the settings link.
        ext_id = get_ext_id(driver=website_controller.driver)
        print(f"ext_id={ext_id}")

        # Go to extension settings.
        website_controller.driver = open_url(
            website_controller.driver,
            f"moz-extension://{ext_id}/settings.html",
        )
        time.sleep(2)

        # Upload backup file to Ublock:
        filepath = os.getcwd() + "/ublock_backup.txt"
        upload_file(website_controller.driver, filepath)

        time.sleep(3)
        website_controller.driver = open_url(
            website_controller.driver,
            f"moz-extension://{ext_id}/settings.html",
        )
        time.sleep(2)
        website_controller.driver = open_url(
            website_controller.driver,
            f"moz-extension://{ext_id}/dashboard.html",
        )
        time.sleep(2)

        # Close website controller.
        website_controller.driver.close()
        print("Applied the backed-up settings to Ublock Origin.")


def upload_file(driver, filepath):
    """Uploads a Ublock Origin backup (template) .txt file into the Ublock
    Origin extension."""
    driver.find_element("id", "restoreFilePicker").send_keys(filepath)
    time.sleep(3)
    alert = driver.switch_to.alert
    print(f"alert.text={alert.text}")
    alert.accept()
    time.sleep(3)

    new_window = driver.window_handles[0]
    driver.switch_to.window(new_window)
