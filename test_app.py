import pytest
from dash.testing.application_runners import import_app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Import your Dash app (Replace "task_4" with your actual filename without .py)
app = import_app("task_4")

# Custom fixture to set up WebDriver using webdriver-manager
@pytest.fixture(scope="session")
def chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Automatically install ChromeDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()

# Test 1: Verify the header is present
def test_header_present(dash_duo, chrome_driver):
    dash_duo.start_server(app)
    header = dash_duo.wait_for_element("h1")
    assert header.text == "Pink Morsel Sales DashBoard", "Header is missing or incorrect"

# Test 2: Verify the visualization (chart) is present
def test_visualization_present(dash_duo, chrome_driver):
    dash_duo.start_server(app)
    chart = dash_duo.wait_for_element("#Sales-line-chart")
    assert chart.is_displayed(), "Sales chart is missing"

# Test 3: Verify the region picker (Radio Items) is present
def test_region_picker_present(dash_duo, chrome_driver):
    dash_duo.start_server(app)
    region_picker = dash_duo.wait_for_element("#region-radio")
    assert region_picker.is_displayed(), "Region picker is missing"

# Run the tests
if __name__ == "__main__":
    pytest.main()
