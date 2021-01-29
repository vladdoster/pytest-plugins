from mock import Mock
import pytest

@pytest.fixture()
def pyramid_server():
    return Mock(uri='http://www.example.com')


def test_webdriver(pyramid_server, webdriver):
    assert webdriver.root_uri == 'http://www.example.com'
    webdriver.get('http://www.example.com')
    assert webdriver.current_url == 'http://www.example.com/'
    