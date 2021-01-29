from mock import Mock, sentinel
import pytest

import pytest_webdriver


def test_browser_to_use():
    caps = Mock(CHROME=sentinel.chrome, UNKNOWN=None)
    wd = Mock(DesiredCapabilities = Mock(return_value = caps))
    assert pytest_webdriver.browser_to_use(wd, 'chrome') == sentinel.chrome
    with pytest.raises(ValueError):
        pytest_webdriver.browser_to_use(wd, 'unknown')