import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver(): #launching the browser using driver as a function
    paths = r"E:\Automation testing\chromedriver.exe"
    os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

# tests
from imdb_search import IMDBSearch # parent directory added

def imdb_test(driver):
    driver.get("https://www.imdb.com/search/name/")
    imdb_search = IMDBSearch(driver)
    imdb_search.open()
    imdb_search.scroll_down()
    imdb_search.fill_search_form(name="bhavani",gender="Female",birth_month="march",birth_year_min="1990",birth_year_max="2000",death_year_min="2010",death_year_max="2023",acting_credits_min="5",sort_by="Popularity Ascending")
    imdb_search.click_search()
