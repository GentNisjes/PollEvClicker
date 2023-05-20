import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

def my_script():


    number_of_inputs = 3

    for x in range(0, number_of_inputs):
        # SET UP

        s = Service('\webdrivers\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("https://pollev.com/hansrediers735")

        time.sleep(1)

        # DISMISS: ACCEPTING THE POLICY OF POLLEV
        driver.find_element(by=By.XPATH, value="/html/body/aside/div[2]/div[2]/pe-button[1]/button/span").click()
        time.sleep(1)

        # driver.find_element(by=By.XPATH, value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/advisory-message/div/div/button[2]").click()
        # time.sleep(1)
        driver.find_element(by=By.XPATH,
                            value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-screen-name").click()
        time.sleep(1)

        # SKIP BUTTON
        driver.find_element(by=By.XPATH,
                            value="//html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-screen-name/div[2]/div[2]/pe-button[2]/button/span").click()

        time.sleep(1)

        # START QUIZ AND CHOOSING RESPONSE 1
        # driver.find_element(by=By.XPATH,value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-activity/div/div/div/button").click()
        driver.find_element(by=By.XPATH,
                            value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-activity/div/div/div[2]/div[2]/div/div[1]/button[1]/div[2]").click()
        # time.sleep(1)

        # # FINISHING THE QUIZ
        # driver.find_element(by=By.XPATH,value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-activity/div/div/div/div[2]/nav/button[2]").click()
        # time.sleep(1)
        # driver.find_element(by=By.XPATH,value="/html/body/pe-application/notification-manager/pe-notification/aside/div[2]/div[2]/pe-button/button/span").click()
        # time.sleep(1)
        # driver.find_element(by=By.XPATH,value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-activity/div/div/div/div[2]/nav/button[2]").click()

        # FORMAT FOR FINDING ELEMENT
        # driver.find_element(by=By.XPATH,value="").click()

        print(driver.title, 'ANS', x + 1, "/", number_of_inputs, "POLL2")
        time.sleep(0.1)
        driver.quit()


if __name__ == '__main__':
    threads = []


    for x in range(0,10):  # Specify the number of threads you want to run
        t = threading.Thread(target=my_script)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  # Wait for all threads to finish
