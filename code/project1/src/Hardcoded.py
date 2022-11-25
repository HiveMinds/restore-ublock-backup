"""Contains the hardcoded data for this project."""


# pylint: disable=C0301
# pylint: disable=R0902
# pylint: disable=R0903
class Hardcoded:
    """Runs jupyter notebooks, converts them to pdf, exports the notebook pdfs
    to latex and compiles the latex report of the incoming project nr."""

    # pylint: disable=R0915
    def __init__(self):
        """Constructs an object that contains all the hardcoded values that are
        used in this script.

        TODO: adjust browser drivers based on the detected device type.
        """

        self.firefox_driver_folder = "firefox_driver"
        self.firefox_driver_tarname = "firefox_driver.tar.gz"
        self.firefox_driver_filename = "geckodriver"
        # self.firefox_driver_link = "https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz"
        self.firefox_driver_link = "https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz"

        self.chromium_driver_folder = "chrome_driver"
        self.chromium_driver_tarname = "chrome_driver.zip"
        self.chromium_driver_link = "https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip"
        self.chromium_driver_unmodified_filename = "chromedriver"
        self.chromium_driver_filename = "chromedriver90"

        # TODO: automate getting default profile key/path.
        self.firefox_profile = (
            "/home/name/.mozilla/firefox/1k7nmeyz.default-release"
        )
