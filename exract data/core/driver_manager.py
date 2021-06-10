from interface import implements, Interface
from selenium import webdriver
from appium import webdriver as m_webdriver

def driver_manager_factory(d_type):
    d_type = d_type.lower()
    if d_type in ['chrome','chromedriver']:
        return ChromeDriverManager()
    elif d_type in ['firefox','geckodriver']:
        return FirefoxDriverManager()
    elif d_type in ['edge']:
        return EdgeDriverManager()
    elif d_type in ['ie']:
        return InternetExplorerDriverManager()
    elif d_type in ['safari','safaridriver']:
        return SafariDriverManager()
    elif d_type in ['m_safari','safari_mobile']:
        return SafariMobileDriverManager()
    elif d_type in ['m_chrome','chrome_mobile']:
        return ChromeMobileDriverManager()
    else:
        return FirefoxDriverManager()


# ! Driver executable are need to be added in PATH variable
# ! Path/URL of the Appium Server should come from a config [Start on desired url and port] TODO
# ! Desired Capabilities of mobile can also come from a config
class DriverManager(Interface):

    def __init__(self):
        '''
        Initiate the WebDriver Executable Path and Desired Capabilities
        '''
        pass

    def create_driver(self):
        '''
        Create Web Driver
        '''
        pass


# Note: Add 'geckodriver' executable as PATH variable
class FirefoxDriverManager(implements(DriverManager)):

    def __init__(self):
        self.driver = None

    def create_driver(self):
        self.driver = webdriver.Firefox(executable_path='./drivers/geckodriver.exe')
        self.driver.maximize_window()
        return self.driver


# Note: Add 'chromedriver' executable as PATH variable
class ChromeDriverManager(implements(DriverManager)):

    def __init__(self):
        self.driver = None

    def create_driver(self):
        self.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        self.driver.maximize_window()
        return self.driver


class SafariDriverManager(implements(DriverManager)):

    def __init__(self):
        self.driver = None

    def create_driver(self):
        self.driver = webdriver.Safari()
        self.driver.maximize_window()
        return self.driver


# Note: Add 'msedgedriver' executable as PATH variable
class EdgeDriverManager(implements(DriverManager)):

    def __init__(self):
        self.driver = None

    def create_driver(self):
        cap = webdriver.DesiredCapabilities().EDGE
        cap["platform"] = "ANY"
        self.driver = webdriver.Edge("msedgedriver",capabilities=cap)
        self.driver.maximize_window()
        return self.driver


# Note: Add 'ie' executable as PATH variable
class InternetExplorerDriverManager(implements(DriverManager)):

    def __init__(self):
        self.driver = None

    def create_driver(self):
        raise NotImplementedError


# Note: iOS Simulator or Real Device need to be connected and available
class SafariMobileDriverManager(implements(DriverManager)):

    def __init__(self,capabilities = None):
        self.dc = capabilities
        self.driver = None
        # Todo Launch Appium Server if not running
        # ! Desired capabilities should come from config.ini [Framework specific config]

    def create_driver(self):
        dc = {
            "platformName": "iOS",
            "platformVersion": "13.6",
            "deviceName": "iPad Pro",
            "automationName": "XCUITest",
            "browserName": "Safari",
            "udid":'CC853F55-AB84-48E8-AEB5-39FE56E721DB'
        }   
        self.driver = m_webdriver.Remote('http://localhost:4723/wd/hub',dc)
        return self.driver


# Note: Android Emulator or Real Device need to be connected and available
class ChromeMobileDriverManager(implements(DriverManager)):

    def __init__(self,capabilities = None):
        self.dc = capabilities
        self.driver = None

    def create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('androidPackage', 'com.android.chrome')
        self.driver = webdriver.Chrome('chromedriver', options=options)
        return self.driver

    
