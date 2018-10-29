import time,unittest,os,pytest
from pytest import skip
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class test_multi(unittest.TestCase):


    def setUp(self):
        driverlocation = "D:\\Pythondriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverlocation
        self.driver = webdriver.Chrome(driverlocation)

    @pytest.fixture()
    def test_multipl_ewindow(self):
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
        print("Page title before switching : " + title)
        print("Total windows : ", len(allguid))
        time.sleep(4)
        for guid in allguid:

            if (guid != parentGUID):
                driver.switch_to.window(guid)
                break

        time.sleep(4)
        text1 = driver.find_element_by_xpath("//*[@class = 'example']")
        print(text1.text)
        print("Page title after switching to new window : ", driver.title)
        time.sleep(4)
        driver.close()
        driver.switch_to.window(parentGUID)
        time.sleep(4)
        driver.back()
        time.sleep(4)
        driver.forward()
        parentile = driver.title
        print("Page title after swithcing back to parent : ", parentile)
    def tearDown(self):
            self.driver.quit()


