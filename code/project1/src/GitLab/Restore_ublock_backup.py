"""Object to run code based on incoming arguments."""
import time
from code.project1.src.Hardcoded import Hardcoded
from code.project1.src.helper import get_browser_drivers, open_url
from code.project1.src.Website_controller import Website_controller


# pylint: disable=R0903
class Restore_ublock_backup:
    """Gets the GitLab runner from the GitLab server."""

    def __init__(self):
        """Initialises object that gets the browser controller, then it gets
        the issues from the source repo, and copies them to the target repo.

        :param login: [Boolean] True if the website_controller object should be
        created and should login to GitHub.
        """

        # Store the hardcoded values used within this project
        self.hc = Hardcoded()

        # get browser drivers
        get_browser_drivers(self.hc)
        website_controller = Website_controller()

        website_controller.driver.implicitly_wait(3)
        # TODO: get the settings link automatically.
        website_controller.driver = open_url(
            website_controller.driver,
            "moz-extension://260d3cd9-bfbf-4869-a842-ef17f9fbed23/settings.html",
        )
        filepath = "/home/name/git/configure_ublock/ublock_backup.txt"
        # Upload backup file to Ublock:

        self.upload_file(website_controller.driver, filepath)

        # close website controller
        website_controller.driver.close()

        print("Applied the backed-up settings to Ublock Origin.")

    def upload_file(self, driver, filepath):
        """Uploads a Ublock Origin backup (template) .txt file into the Ublock
        Origin extension."""
        driver.find_element("id", "restoreFilePicker").send_keys(filepath)
        time.sleep(1)
        driver.switch_to.alert.accept()
