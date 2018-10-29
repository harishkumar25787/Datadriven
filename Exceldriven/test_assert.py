import time,xlrd,unittest,os,pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class test_hero1(unittest.TestCase):

    def setUp(self):
        driverlocation = "D:\\Pythondriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        self.driver = webdriver.Chrome(driverlocation)
    @pytest.fixture()
    def test_forasserrt(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("http://the-internet.herokuapp.com/")
        print(driver.title)
        parentGUID = driver.current_window_handle
        driver.find_element_by_link_text("Multiple Windows").click()
        driver.find_element_by_link_text("Click Here").click()
        allguid = driver.window_handles
        count = len(allguid)
        print(count)
        title = driver.title
        if "The Internet" in title:
            print("Title of  page matches : ")
            return True

        else :
            print("Title mismatch")


    def tearDown(self):
        self.driver.quit()
