"""Object to run code based on incoming arguments."""
import os
import time
from code.project1.src.get_ext_id import get_ext_id
from code.project1.src.Hardcoded import Hardcoded
from code.project1.src.helper import get_browser_drivers, open_url
from code.project1.src.Website_controller import Website_controller


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
        ext_id = get_ext_id(website_controller.driver)
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

        # time.sleep(10)
        # website_controller.driver.navigate().back()
        time.sleep(3)
        website_controller.driver = open_url(
            website_controller.driver,
            f"moz-extension://{ext_id}/settings.html",
        )
        time.sleep(2)
        website_controller.driver = open_url(
            website_controller.driver,
            f"moz-extension://{ext_id}/dashboard.html",
            # moz-extension://260d3cd9-bfbf-4869-a842-ef17f9fbed23/dashboard.html#1p-filters.html
            # moz-extension://260d3cd9-bfbf-4869-a842-ef17f9fbed23/dashboard.html#settings.html
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
    time.sleep(10)
    # driver.close()
    # print(f'driver.switch_to={driver.switch_to.__dict__}')
    # driver.switch_to.driver

    new_window = driver.window_handles[0]
    driver.switch_to.window(new_window)

    # driver.switch_to.default_content()
    # driver.switch_to.frame('iframe1')
