import time
import random
import smtplib
import sys
import os
import datetime
import holidays
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class TestInit():

  def setup(self, mail_user, mail_pass, edu_user, edu_pass, edu_school):
    #self.send_mail("Startup service")
    self.mail_user = mail_user
    self.mail_pass = mail_pass
    self.edu_user = edu_user
    self.edu_pass = edu_pass
    self.edu_school = edu_school

    options = Options()
    options.headless = False

    gecko_path = './geckodriver'
    if 'GECKODRIVER_PATH' in os.environ: 
      gecko_path = os.environ['GECKODRIVER_PATH']
    if 'FIREFOX_BIN' in os.environ: 
      binary = FirefoxBinary(os.environ['FIREFOX_BIN'])
      self.driver = webdriver.Firefox(firefox_binary=binary, options=options, executable_path=gecko_path)
    else:
      self.driver = webdriver.Firefox(options=options, executable_path=gecko_path)
  
  def teardown(self):
    self.driver.quit()
  
  def test(self):
    try:
      print("1 Initializing")
      wait = WebDriverWait(self.driver, 30)
      # Test name: init
      # Step # | name | target | value

      # 2 | open | / | 
      print("2 Opening browser... Waiting till fully loaded")
      time.sleep(random.uniform(5, 9)) 
      self.driver.get("https://web.mashov.info/msite/login.aspx")

      # 3 | wait until the initial login selection screen somes and click to switch
      wait.until(presence_of_element_located((By.LINK_TEXT, "משו\"ב להורים ותלמידים")))
      print("3 Login page loaded... Waiting 2-4 sec before click")
      time.sleep(random.uniform(2, 4)) 
      self.driver.find_element(By.LINK_TEXT, "משו\"ב להורים ותלמידים").click()

      # 4 | wait until the login page comes up and click the school box
      wait.until(presence_of_element_located((By.ID, "mat-input-3")))
      print("4 Login page loaded... Waiting 1-3 sec before click school")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.ID, "mat-input-3").click()

      # 5 | type username
      print("5 Clicked... Waiting 2-4 sec before entering school")
      time.sleep(random.uniform(2, 4)) 
      self.driver.find_element(By.ID, "mat-input-3").send_keys(self.edu_school)

      # 6 | wait until the MOE login page comes up and click the username box
      print("6 Entered schoole code... Waiting 1-3 sec before selecting school")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.CSS_SELECTOR, ".mat-option-text").click()

      # 7 | click username
      print("7 Clicked... Waiting 2-4 sec before clicking username")
      time.sleep(random.uniform(2, 4)) 
      self.driver.find_element(By.ID, "mat-input-0").click()

      # 8 | type username
      print("8 Clicked... Waiting 2-4 sec before entering username")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.ID, "mat-input-0").send_keys(self.edu_user)

      # 9 | click the password
      wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mat-button-wrapper > .ng-star-inserted")))
      print("9 Entered username ... Waiting 1-3 sec before click password")
      time.sleep(random.uniform(1, 3)) 
      element = self.driver.find_element(By.CSS_SELECTOR, ".mat-button-wrapper > .ng-star-inserted")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()

      # 10 | Entered password
      wait.until(presence_of_element_located((By.ID, "mat-input-4")))
      print("10 Clicked ... Waiting 1-3 sec before enter password")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.ID, "mat-input-4").send_keys(self.edu_pass)

      # 11 | Click login
      wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mat-button-wrapper > .ng-star-inserted")))
      print("11 Entered password ... Waiting 1-3 sec before clicking login")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.CSS_SELECTOR, ".mat-button-wrapper > .ng-star-inserted").click()

      # # 12 | mouseOver | css=.ng-tns-c401-10:nth-child(3) > .mat-focus-indicator > .mat-button-wrapper > .mshv-menu-item | 
      # wait.until(presence_of_element_located((By.CSS_SELECTOR, ".ng-tns-c401-10:nth-child(3) > .mat-focus-indicator > .mat-button-wrapper > .mshv-menu-item")))
      # print("12 Post login ... Waiting 1-3 sec before moving to health statement")
      # time.sleep(random.uniform(1, 3)) 
      # element = self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c401-10:nth-child(3) > .mat-focus-indicator > .mat-button-wrapper > .mshv-menu-item")
      # actions = ActionChains(self.driver)
      # actions.move_to_element(element).perform()

      # 13 | click | css=.splash-purple > .splash-header-text-large | 
      wait.until(presence_of_element_located((By.CSS_SELECTOR, ".splash-purple > .splash-header-text-large")))
      print("13 Post login ... Waiting 1-3 sec before clicking health statement")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.CSS_SELECTOR, ".splash-purple > .splash-header-text-large").click()

      # 14 | click | css=.mat-primary > .mat-button-wrapper | 
      wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mat-primary > .mat-button-wrapper")))
      print("13 Inside statement ... Waiting 1-3 sec before clicking confirm")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.CSS_SELECTOR, ".mat-primary > .mat-button-wrapper").click()

      # 15 | runScript | window.scrollTo(0,0) | 
      print("14 Inside statement ... Waiting 1-3 sec before scroll")
      time.sleep(random.uniform(1, 3)) 
      self.driver.execute_script("window.scrollTo(0,0)")

      # 16 | mouseOver | css=.mat-icon-button:nth-child(1) | 
      element = self.driver.find_element(By.CSS_SELECTOR, ".mat-icon-button:nth-child(1)")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()

      # 17 | mouseOut | css=.mat-icon-button:nth-child(1) | 
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()

      # 21 | click | css=.mshv-student-dropdown-icon:nth-child(1) > svg | 
      wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mshv-student-dropdown-icon:nth-child(1) > svg")))
      print("21 Inside statement ... Waiting 1-3 sec before click")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.CSS_SELECTOR, ".mshv-student-dropdown-icon:nth-child(1) > svg").click()

      # 22 | click | css=.mshv-child-item:nth-child(1) | 
      wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mshv-child-item:nth-child(1)")))
      print("22 Inside statement ... Waiting 1-3 sec before click")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.CSS_SELECTOR, ".mshv-child-item:nth-child(1)").click()

      # 23 | mouseOver | css=.mat-focus-indicator:nth-child(3) .ng-star-inserted | 
      element = self.driver.find_element(By.CSS_SELECTOR, ".mat-focus-indicator:nth-child(3) .ng-star-inserted")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()

      # 24 | click | css=.splash-purple > .splash-header-text-large | 
      wait.until(presence_of_element_located((By.CSS_SELECTOR, ".splash-purple > .splash-header-text-large")))
      print("24 Inside statement ... Waiting 1-3 sec before click")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.CSS_SELECTOR, ".splash-purple > .splash-header-text-large").click()

      # 25 | click | css=.mat-primary > .mat-button-wrapper | 
      wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mat-primary > .mat-button-wrapper")))
      print("25 Inside statement ... Waiting 1-3 sec before click")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.CSS_SELECTOR, ".mat-primary > .mat-button-wrapper").click()

      # 26 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")

      # 27 | mouseOver | css=.mat-focus-indicator:nth-child(16) | 
      element = self.driver.find_element(By.CSS_SELECTOR, ".mat-focus-indicator:nth-child(16)")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()

      # 28 | mouseOut | css=.mat-focus-indicator:nth-child(16) | 
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()

      # 29 | click | css=.mat-focus-indicator:nth-child(16) svg | 
      wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mat-focus-indicator:nth-child(16) svg")))
      print("29 Inside statement ... Waiting 1-3 sec before click")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.CSS_SELECTOR, ".mat-focus-indicator:nth-child(16) svg").click()

      # 30 | mouseOver | css=.mat-button:nth-child(3) > .mat-button-wrapper | 
      element = self.driver.find_element(By.CSS_SELECTOR, ".mat-button:nth-child(3) > .mat-button-wrapper")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()

      # 31 | click | css=.mat-button:nth-child(3) > .mat-button-wrapper | 
      wait.until(presence_of_element_located((By.CSS_SELECTOR, ".mat-button:nth-child(3) > .mat-button-wrapper")))
      print("29 Inside statement ... Waiting 1-3 sec before Logoug")
      time.sleep(random.uniform(1, 3)) 
      self.driver.find_element(By.CSS_SELECTOR, ".mat-button:nth-child(3) > .mat-button-wrapper").click()

      return "Ended Successfully!!"
    except Exception as e: 
      print("Error: ", type(e), " ", e.msg)
      return "Failed with error: " + type(e) + " " + e.msg
        

  def send_mail(self, msg):
    fromaddr = self.mail_user
    toaddrs  = self.mail_user
    subj = 'Message from Mashov Bot'
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (fromaddr, toaddrs, subj, msg)

    username = self.mail_user
    password = self.mail_pass
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()


# 
# password = ''
# for line in sys.stdin():
#     password = line.rstrip()

args = []
if len(sys.argv) == 1:
  cred_file = Path("creds")
  if cred_file.is_file():
    import fileinput
    args.append("_")
    for line in fileinput.input(files=('creds')):
        args.append(line.rstrip())
  else:
    args.append("_")
    args.append(os.environ['MAIL_USER'])
    args.append(os.environ['MAIL_PASS'])
    args.append(os.environ['MOE_USER'])
    args.append(os.environ['MOE_PASS'])
    args.append(os.environ['MOE_SCHOOL'])

else:
  args = sys.argv

il_holidays = holidays.Israel()
day = datetime.datetime.today() 
# Don't run on friday, saturday and il-holidays
if day.weekday() != 5 and day.weekday() != 4 and day not in il_holidays:
  test = TestInit()
  result = 'Test not run'
  test.setup(args[1], args[2], args[3], args[4], args[5]) #password)
  result = test.test()
  test.teardown()
  test.send_mail("Finished with message:\n" + result)  
else:
  print("Skipping day on no school: ", day)

sys.exit()