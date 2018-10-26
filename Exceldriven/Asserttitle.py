import time,xlrd,unittest,os,pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from ddt import ddt,data,unpack


@ddt
class test_hero1(unittest.TestCase):

    def setUp(self):
        driverlocation = "D:\\Pythondriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        self.driver = webdriver.Chrome(driverlocation)
    @pytest.mark.run(order=1)
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
