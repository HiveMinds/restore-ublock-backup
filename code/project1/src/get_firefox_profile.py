"""Gets and returns the firefox profile."""

import time
from code.project1.src.helper import open_url


def get_firefox_profile(driver):
    """Returns the extension id of Ublock Origin."""
    # Go to extension settings.
    driver = open_url(
        driver,
        "about:support",
    )
    time.sleep(1)

    # Get the extension id from the browser.
    firefox_profile = driver.find_element(
        "xpath",
        f'//*[@id="profile-dir-box"]',
    )

    print(f"firefox_profile.text={firefox_profile.text}")
    return firefox_profile.text
