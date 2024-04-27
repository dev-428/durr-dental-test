from selenium import webdriver


def before_all(context):
    print("Open chrome")
    context.driver = webdriver.Chrome()


def after_all(context):
    print("Close Chrome")
    context.driver.quit()
