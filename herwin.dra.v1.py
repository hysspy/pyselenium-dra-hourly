import os
import psutil
import time
import logging
import ssl
import smtplib
import pandas as pd
import ipgx
import ipgy
import ipocs
from ipgx import gx
from ipgy import gy
from ipocs import ocs
from dotenv import load_dotenv
from datetime import datetime
from PIL import Image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox, FirefoxOptions, FirefoxProfile
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from Screenshot import Screenshot

# record current timestamp
start = datetime.now() 

#Start DEBUG Logging
#LOG_FNAME = datetime.now().strftime('D:/Path to/Python/Log/debuglog-%H_%M_%S_%d_%m_%Y.log')
#for handler in logging.root.handlers[:]:
#    logging.root.removeHandler(handler)
#logging.basicConfig(filename=LOG_FNAME,level=logging.DEBUG)
#logging.basicConfig(filename=LOG_FNAME,level=logging.INFO)  
#logging.info('Forecasting Job Started...')
#logging.debug('abc method started...')

#Print SHELL LOG to file
LOG_FILENAME = datetime.now().strftime('C:/Path/To/Python/Log/dralog-%H_%M_%S_%d_%m_%Y.log')
log = open(LOG_FILENAME, 'w')

def oprint(message):
    print(message)
    global log
    log.write(message + "\n")
    return()

oprint("=======START LOG=======")

# Setup Firefox driver
profile_path = "C:\\Users\\((name))\\Profiles\\kzecrscn.default"
options = Options()
options.add_argument('--private')
options.add_argument('--headless')
options.add_argument('--hide-scrollbars')
options.add_argument('--disable-gpu')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.set_capability("acceptInsecureCerts", True)
options.set_preference('profile', profile_path)
service = Service("C:\\Path\\To\\Python\\geckodriver.exe")
driver = Firefox(service=service, options=options)

ob = Screenshot.Screenshot()

epoch = int((round(time.time() * 1000)) + 5254000)
idx = epoch
oprint(f'id = {idx}')

# Fetching the First Url
url = "Dra-overview-link"

# Second Url
sec_url = "Dra-session-link"

# Second Url
urlconfig = "config-firefox-link"

# Third Url
thir_url = "Dra-link"

# Fourth Url
four_url = "Dra-dashboard-link"

fifth_url = f'test-link'

gxtotal = f'Gx-total-link'

gxfail = f'Gx-fail-link'

gytotal = f'Gy-total-link'

gyfail = f'Gy-fail-link'

ocstotal = f'Ocs-total-link'

ocsrec = f'Ocs-rec-link'

ocstran = f'Ocs-tran-link'

oracle = "Oracle-dashboard"

history = "Oracle-history-link"

# Opening first url
try:
    driver.get(url)
    driver.fullscreen_window()
except Exception as e:
    logging.exception("Oops:")
oprint("DRA Link OK")
oprint("Wait 2s")
time.sleep(2)

# Take a screenshot
driver.save_screenshot("zscr-1.png")
oprint("Open Web OK")

#input creds
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login_inp']"))).send_keys("secret")
driver.find_element(By.XPATH, "//input[@id='password2_inp']").send_keys("secret")
oprint("Login OK")

# Take a screenshot after entering a value
driver.save_screenshot("zscr-2.png")
oprint("Save OK")

#press signin
button = driver.find_element(By.XPATH, "//input[@value='Sign In']")
button.click()

oprint("Wait 2s")
time.sleep(2)

# Take full screenshot
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),1263) # May need manual adjustment                                                                                                                
element = driver.find_element(By.TAG_NAME, 'body')
img_url = ob.get_element(driver, element, save_path=r'C:/Path/To/Python/', image_name='zDRA0.png')
oprint(img_url)
oprint("GET FINAL DRA OK")

# Open a new window
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[1])
    driver.fullscreen_window()
    driver.get(sec_url)
except Exception as e:
    logging.exception("Oops:")
oprint("Bucket Link OK")
oprint("Wait 2s")
time.sleep(2)

# Take full screenshot
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),1263) # May need manual adjustment                                                                                                                
element = driver.find_element(By.TAG_NAME, 'body')
img_url = ob.get_element(driver, element, save_path=r'C:/Path/To/Python/', image_name='zBucket.png')
oprint(img_url)
oprint("GET FINAL BUCKET OK")

################################################### CONFIG START ####################################################
#Author : Herwin Yudha Setyawan#
#Timestamp : 07-November-2023#
#Linkedin : Herwin Yudha Setyawan#

try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[2])
    driver.fullscreen_window()
    driver.get(urlconfig)
except Exception as e:
    logging.exception("Oops:")
oprint("CONFIG Link OK")
oprint("Wait 1s")
time.sleep(1)

#press enter
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
oprint("Press ENTER")

#input tls
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='about-config-search']"))).send_keys("security.tls.version.min")

#press enter
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
oprint("Press ENTER")

#CLICK EDIT
oprint("Press Edit")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@title='Edit']"))).click()
oprint("Wait 1s")
time.sleep(1)
#INPUT 1
oprint("Input 1")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='number']"))).send_keys("1")

#press enter
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
oprint("Press ENTER")

oprint("Wait 2s")
time.sleep(2)
############################################### CONFIG END ################################################################

# Open a new window DRA LOGIN
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[3])
    driver.fullscreen_window()
    driver.get(thir_url)
except Exception as e:
    logging.exception("Oops:")
oprint("BroadForward Link OK")
oprint("Wait 2s")
time.sleep(2)

# Take a screenshot
driver.save_screenshot("zscr-bfx1.png")
oprint("Open Web OK")
oprint("Wait 1s")
time.sleep(1)

#input creds
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='uinp_l01']"))).send_keys("secret")
driver.find_element(By.XPATH, "//input[@id='uinp_l02']").send_keys("secret")
oprint("Login OK")

# Take a screenshot
driver.save_screenshot("zscr-bfx2.png")
oprint("Save OK")

#press enter
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
oprint("Press ENTER")

oprint("Wait 1s")
time.sleep(1)

# Take full screenshot
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),1263) # May need manual adjustment                                                                                                                
element = driver.find_element(By.TAG_NAME, 'body')
img_url = ob.get_element(driver, element, save_path=r'C:/Path/To/Python/', image_name='zBFX.png')
oprint(img_url)
oprint("GET LOGIN BFX OK")
driver.refresh()
driver.refresh()
driver.refresh()
oprint("sleep 1s")
time.sleep(1)

# Open a new window DASHBOARD FLOW
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[4])
    driver.fullscreen_window()
    driver.get(four_url)
    driver.get(fifth_url)
    driver.get(gxtotal)
    driver.get(gxtotal)
    driver.get(gxfail)
    driver.get(gxfail)
    driver.get(gytotal)
    driver.get(gyfail)
    driver.get(ocstotal)
    driver.get(ocsrec)
    driver.get(ocstran)
except Exception as e:
    logging.exception("Oops:")
oprint("Dashboard Link OK")
oprint("Wait 1s")
time.sleep(1)
driver.refresh()
driver.refresh()
driver.refresh()

oprint("GET DASHBOARD DRA OK")
oprint("sleep 5s")
time.sleep(5)
driver.refresh()
driver.refresh()
driver.refresh()
driver.refresh()
driver.refresh()

# Open a new window GX Total
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[5])
    driver.fullscreen_window()
    driver.get(fifth_url)
    driver.get(gxtotal)
except Exception as e:
    logging.exception("Oops:")
oprint("Gx Link OK")

driver.refresh()
oprint("Wait 10s")
time.sleep(10)
driver.get(gxtotal)
driver.refresh()
driver.refresh()
driver.refresh()
driver.save_screenshot("zGxTotal.png")
oprint("Open Web OK")

# Open a new window GX Fail
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[6])
    driver.fullscreen_window()
    driver.get(fifth_url)
    driver.get(gxfail)
except Exception as e:
    logging.exception("Oops:")
oprint("Gx Link OK")

driver.refresh()
oprint("Wait 10s")
time.sleep(10)
driver.get(gxfail)
driver.refresh()
driver.refresh()
driver.refresh()
driver.save_screenshot("zGxFail.png")
oprint("Open Web OK")

# Open a new window GY Total
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[7])
    driver.fullscreen_window()
    driver.get(gytotal)
    driver.get(gytotal)
except Exception as e:
    logging.exception("Oops:")
oprint("Gy Link OK")
driver.refresh()
oprint("Wait 10s")
time.sleep(10)
driver.refresh()
driver.save_screenshot("zGyTotal.png")
oprint("Open Web OK")

# Open a new window GY Fail
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[8])
    driver.fullscreen_window()
    driver.get(gyfail)
    driver.get(gyfail)
except Exception as e:
    logging.exception("Oops:")
oprint("Gy Link OK")
driver.refresh()
oprint("Wait 10s")
time.sleep(10)
driver.refresh()
driver.refresh()
driver.refresh()
driver.save_screenshot("zGyFail.png")
oprint("Open Web OK")

# Open a new window OCS TOTAL
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[9])
    driver.fullscreen_window()
    driver.get(ocstotal)
    driver.get(ocstotal)
except Exception as e:
    logging.exception("Oops:")
oprint("OCST Link OK")
driver.refresh()
oprint("Wait 10s")
time.sleep(10)
driver.refresh()
driver.refresh()
driver.save_screenshot("zOcsTotal.png")
oprint("Open Web OK")

# Open a new window OCS RECEIVED
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[10])
    driver.fullscreen_window()
    driver.get(ocsrec)
    driver.get(ocsrec)
except Exception as e:
    logging.exception("Oops:")
oprint("OCSR Link OK")
driver.refresh()
oprint("Wait 10s")
time.sleep(10)
driver.refresh()
driver.refresh()
driver.save_screenshot("zOcsRec.png")
oprint("Open Web OK")

# Open a new window OCS TRANSMITTED
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[11])
    driver.fullscreen_window()
    driver.get(ocstran)
    driver.get(ocstran)
except Exception as e:
    logging.exception("Oops:")
oprint("OCSTR Link OK")
driver.refresh()
oprint("Wait 10s")
time.sleep(10)
driver.refresh()
driver.refresh()
driver.save_screenshot("zOcsTran.png")
oprint("Open Web OK")

# Open a new window ORACLE
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[12])
    driver.fullscreen_window()
    driver.get(oracle)
except Exception as e:
    logging.exception("Oops:")
oprint("ORACLE Link OK")
oprint("Wait 1s")
time.sleep(1)

# Take a screenshot
driver.save_screenshot("ztest-1.png")
oprint("Open Web OK")

#input creds
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))).send_keys("secretusername")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("secretpassword")
oprint("Login OK")

# Take a screenshot after entering a value
driver.save_screenshot("ztest-2.png")
oprint("Save OK")

#press enter
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
oprint("Press ENTER")

oprint("Wait 2s")
time.sleep(2)

# Take full screenshot
x = 100
scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(scroll_width + x, scroll_height + x)
#Get by element body
element = driver.find_element(By.TAG_NAME, 'body')
img_url = ob.get_element(driver, element, save_path=r'C:/Path/To/Python/', image_name='zORACLE.png')
oprint(img_url)
oprint("GET FINAL ORACLE OK")

# Open a new window HISTORY
try:
    driver.execute_script("window.open('');")
# Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[13])
    driver.fullscreen_window()
    driver.get(history)
except Exception as e:
    logging.exception("Oops:")
oprint("History Link OK")
oprint("Wait 1s")
time.sleep(1)

x = 100
scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(scroll_width + x, scroll_height + x)
#Get by element body
element = driver.find_element(By.TAG_NAME, 'body')
img_url = ob.get_element(driver, element, save_path=r'C:/Path/To/Python/', image_name='yHistory.png')
oprint(img_url)
oprint("GET FINAL HISTORY OK")

# Close the driver
driver.quit()
oprint("Close Driver")
driver.quit()
oprint("Quit Driver")

oprint("Wait 1s")
time.sleep(1)

#Close multiple processes selenium firefox + geckodriver
os.system('taskkill /f /t /im firefox.exe /fi "USERNAME eq (name)"')
oprint("Close firefox")
time.sleep(1)
os.system('taskkill /f /t /im geckodriver.exe /fi "USERNAME eq (name)"')
oprint("Close geckodriver")

######################Crop image##########################
#Create an Image Object from an Image
zm = Image.open('zBucket.png')
oprint("Load Image OK")

#left, upper, right, lower Crop
cropped = zm.crop((130,101,1186,587))

#Save the cropped image
cropped.save('yBucket.png')
oprint("CROP BUCKET OK")

####Main GX
#Create an Image Object from an Image
am = Image.open('zGxTotal.png')
oprint("Load Image OK")
#left, upper, right, lower Crop
cropped = am.crop((189,261,1175,505))
#Save the cropped image
cropped.save('yGxTotal.png')
oprint("CROP GX OK")

#Create an Image Object from an Image
bm = Image.open('zGxFail.png')
oprint("Load Image OK")
#left, upper, right, lower Crop
cropped = bm.crop((189,240,1176,526))
#Save the cropped image
cropped.save('yGxFail.png')
oprint("CROP GX OK")

####S-GY
#Create an Image Object from an Image
cm = Image.open('zGyTotal.png')
oprint("Load Image OK")
#left, upper, right, lower Crop
cropped = cm.crop((189,261,1175,505))
#Save the cropped image
cropped.save('yGyTotal.png')
oprint("CROP GY OK")

#Create an Image Object from an Image
dm = Image.open('zGyFail.png')
oprint("Load Image OK")
#left, upper, right, lower Crop
cropped = dm.crop((189,240,1176,526))
#Save the cropped image
cropped.save('yGyFail.png')
oprint("CROP GY OK")

####OCS
#Create an Image Object from an Image
em = Image.open('zOcsTotal.png')
oprint("Load Image OK")
#left, upper, right, lower Crop
cropped = em.crop((189,225,1176,542))
#Save the cropped image
cropped.save('yOcsTotal.png')
oprint("CROP OCS TOTAL OK")

#Create an Image Object from an Image
fm = Image.open('zOcsRec.png')
oprint("Load Image OK")
#left, upper, right, lower Crop
cropped = fm.crop((189,233,1176,535))
#Save the cropped image
cropped.save('yOcsRec.png')
oprint("CROP OCS REC OK")

#Create an Image Object from an Image
gm = Image.open('zOcsTran.png')
oprint("Load Image OK")
#left, upper, right, lower Crop
cropped = gm.crop((189,233,1176,535))
#Save the cropped image
cropped.save('yOcsTran.png')
oprint("CROP OCS TRAN OK")
######################Crop End##########################

oprint("Preparing Email")
#######SEND MAIL######

###########################
# Define the HTML document
# Add an image element
##############################################################
html = '''
    <html>
        <body>
            <p>Hi Team,<br> See inital graphs for the KPIs to be monitored hourly as requested.</p>
            <h4>DRA Couchbase Memory:</h4>
            <img src='cid:yBucket.png'>
            <h4>Gx Total Transactions:</h4>
            <img src='cid:yGxTotal.png'>
            <h4>Gx Failed Transactions:</h4>
            <img src='cid:yGxFail.png'>
            <h4>Gy Total Transactions:</h4>
            <img src='cid:yGyTotal.png'>
            <h4>Gy Failed Transactions:</h4>
            <img src='cid:yGyFail.png'>
            <h4>Sample OCS Transactions:</h4>
            <img src='cid:yOcsTotal.png'>
            <img src='cid:yOcsRec.png'>
            <img src='cid:yOcsTran.png'>
            <h4>Status of Alarms - PCRF:</h4>
            <img src='cid:yHistory.png'>
        </body>
    </html>
    '''
##############################################################

# Define a function to attach files as MIMEApplication to the email
    ## Add another input extra_headers default to None
##############################################################
def attach_file_to_email(email_message, filename, extra_headers=None):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Set up the input extra_headers for img
      ## Default is None: since for regular file attachments, it's not needed
      ## When given a value: the following code will run
         ### Used to set the cid for image
    if extra_headers is not None:
        for name, value in extra_headers.items():
            file_attachment.add_header(name, value)
    # Attach the file to the message
    email_message.attach(file_attachment)
##############################################################    

#Load env creds
load_dotenv()
oprint("Load Creds")
# Set up the email addresses and password. Please replace below with your email address and password
toaddr = ['EmailTo']
cc = ['EmailCc']
email_from = 'GatewayMail'
usrname = os.getenv("secretUser")
password = os.getenv("secretPass")

# Generate today's date to be included in the email Subject
date_str = pd.Timestamp.today().strftime('%d/%m/%Y, %H:%M')

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = ','.join(toaddr)
email_message['Cc'] = ','.join(cc)
email_message['Subject'] = f'M1 Hourly Monitoring for DRA {date_str} SGT'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))

# Attach more (documents)
## Apply function with extra_header on m1aws.png. This will render m1aws.png in the html content
##############################################################
attach_file_to_email(email_message, 'yBucket.png', {'Content-ID': '<yBucket>'})
attach_file_to_email(email_message, 'yGxTotal.png', {'Content-ID': '<yGxTotal>'})
attach_file_to_email(email_message, 'yGxFail.png', {'Content-ID': '<yGxFail>'})
attach_file_to_email(email_message, 'yGyTotal.png', {'Content-ID': '<yGyTotal>'})
attach_file_to_email(email_message, 'yGyFail.png', {'Content-ID': '<yGyFail>'})
attach_file_to_email(email_message, 'yOcsTotal.png', {'Content-ID': '<yOcsTotal>'})
attach_file_to_email(email_message, 'yOcsRec.png', {'Content-ID': '<yOcsRec>'})
attach_file_to_email(email_message, 'yOcsTran.png', {'Content-ID': '<yOcsTran>'})
attach_file_to_email(email_message, 'yHistory.png', {'Content-ID': '<yHistory>'})
##############################################################

# Convert it as a string
email_string = email_message.as_string()

# Connect to the SMTP server and send the email
smtp_server = "smtp-mail"
smtp_port = smtp-port

#context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(usrname, password)  # Check above username & password
    server.sendmail(email_from, (toaddr+cc), email_string)
    server.quit()
oprint("Email Sent OK")

#Clean Old Log Files more than 1 days
oprint("Checking Logs if older than 1 days...")

folder = "Log"

#older than the specified days
N = 1

#changing the current working directory to the folder specified
os.chdir(os.path.join(os.getcwd(), folder))

#get a list of files present in the given folder
list_of_files = os.listdir()

#get the current time
current_time = time.time()

#"day" is the number of seconds in a day
day = 86400

#loop over all the files
for i in list_of_files:
	#get the location of the file
	file_location = os.path.join(os.getcwd(), i)
	#file_time is the time when the file is modified
	file_time = os.stat(file_location).st_mtime

	#if a file is modified before N days then delete it
	if(file_time < current_time - day*N):
		oprint(f" Delete : {i}")
		os.remove(file_location)

oprint(".......Done")

# record loop end timestamp
end = datetime.now() 
# find difference loop start and end time and display
td = (end - start)
oprint(f"The time of execution of above program is : {td}s")
oprint("=======END LOG=======")
log.close()