from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('chromedriver_path_here')

driver.get('https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&fromSignIn=true&trk=uno-reg-join-sign-in')

# sleep(1)
email = driver.find_element_by_name('session_key')
password = driver.find_element_by_name('session_password')
singInButton = driver.find_element_by_name('signin')

email.send_keys('email_here')
sleep(1)
password.send_keys('password_here')
sleep(1)
singInButton.click()
sleep(1)

driver.get('https://www.linkedin.com/mynetwork/')
while True:
    sleep(1)
    conn = driver.find_elements_by_class_name('button-secondary-small')
    # for ddt in conn:
    if len(conn)>3:
        conn[0].click()
    elif len(conn) <= 3:
        driver.get('https://www.linkedin.com/mynetwork/')
        sleep(2)
