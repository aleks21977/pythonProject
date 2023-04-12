from selenium.webdriver.chrome.webdriver import WebDriver


class Application:
    pass

    def __init__(self):
        self.wd = WebDriver('./webdriver/chromedriver')
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://demoqa.com/text-box")

    def find_elements_by_xpath(self, x_path):
        element = self.wd.find_element("xpath", x_path)
        return element

    def get_element_text(self, x_path):
        element_text = self.wd.find_element("xpath", x_path).text
        return element_text

    def destroy(self):
        self.wd.quit()
