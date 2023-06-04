import pytest
from dash.testing.application_runners import import_app
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Define the test cases
def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app.layout)

    header = dash_duo.wait_for_element("#header")
    assert header is not None

def test_visualization_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app.layout)

    chart = dash_duo.wait_for_element("#sales-chart")
    assert chart is not None

def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app.layout)

    picker = dash_duo.wait_for_element("#region-filter")
    assert picker is not None

# Execute the test suite
if __name__ == "__main__":
    args = [
        "--no-sugar",
        "--headless",
        "--disable-gpu",
        "--disable-extensions",
        "--disable-dev-shm-usage",
        "--disable-setuid-sandbox",
        "--no-sandbox",
    ]
    webdriver.ChromeOptions.add_argument = lambda self, arg: args.append(arg)
    pytest.main(["-s", "--driver", "Chrome", "--driver-path", ChromeDriverManager().install(), __file__])
