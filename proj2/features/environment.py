from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_all(context):
	try:
		context.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
	except WebException:
		context.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
    		
	context.driver.implicitly_wait(5)
	context.base_url = "http://localhost:8080/VALU3S"


def after_all(context):
	context.driver.quit()
