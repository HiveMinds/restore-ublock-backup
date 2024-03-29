"""Gets a website controller and opens it."""
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from .Hardcoded import Hardcoded


# pylint: disable=R0903
class Website_controller:
    """Controls/commands website using selenium."""

    def __init__(self):
        """Constructs object that controlls a firefox browser.

        TODO: Allow user to switch between running browser
        in background or foreground.
        """
        self.hardcoded = Hardcoded()

        # Kill firefox
        close_firefox()

        # To run Firefox browser in foreground
        print("Loading geckodriver")
        try:
            options = Options()

            options.add_argument("-profile")
            options.add_argument(self.hardcoded.firefox_profile)
            # options.add_argument("window-size=400,600")
            options.set_preference("dom.webdriver.enabled", False)
            options.set_preference("useAutomationExtension", False)

            self.driver = webdriver.Firefox(
                options=options,
                executable_path=r"firefox_driver/geckodriver",
            )
        # pylint: disable=W0707
        except:
            # pylint: disable=W0707
            raise Exception(
                "Error, you have the snap Firefox browser installed"
                + ". Please use the apt one instead. This switching is automated"
                + " in a bash script of the Self-host GitLab."
            )

        # To run Firefox browser in background
        # os.environ["MOZ_HEADLESS"] = "1"
        # self.driver = webdriver.Firefox(executable_path=r"firefox_driver/geckodriver")

        # To run Chrome browser in background
        # options = webdriver.ChromeOptions();
        # options.add_argument('headless');
        # options.add_argument('window-size=1200x600'); // optional

def close_firefox() -> None:
    """Closes firefox if it is open."""
    if subprocess.call( [ "pkill", "firefox" ] ) > 0:
        raise SystemError("Firefox not closed.")
    