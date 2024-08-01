from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

city = "Glasgow" #input('Enter the city you are looking for: ')
minNumBedrooms = "1" #input('Enter the number of bedrooms you are looking for: ')
maxPCM = "500" #input('Enter the max amount you are willing to pay  per month: ')


options = Options()
options.add_experimental_option('detach', True)
options.add_argument('--log-level=1')


web = webdriver.Chrome()
web.get("https://www.rightmove.co.uk/")

cookiesReject = WebDriverWait(web, 15).until(EC.element_to_be_clickable(('xpath', '//*[@id="onetrust-reject-all-handler"]')))
cookiesReject.click()

searchArea = web.find_element('xpath', '//*[@id="ta_searchInput"]')
searchArea.send_keys(city)
rentBtn = web.find_element('xpath', '//*[@id="HomePageContent_heroContainer__OlWkr"]/div[2]/div/div[2]/button[2]')
time.sleep(2)
rentBtn.click()

minBedroomsBtn = web.find_element('xpath', '//*[@id="minBedrooms"]')
minBedroomsBtn = Select(minBedroomsBtn)
minBedroomsBtn.select_by_visible_text(str(minNumBedrooms))


maxPCMBtn = web.find_element('xpath', '//*[@id="maxPrice"]')
maxPCMBtn = Select(maxPCMBtn)
maxPCMBtn.select_by_visible_text(maxPCM + ' PCM')

submitRequirements = web.find_element('xpath', '//*[@id="submit"]')
submitRequirements.click()

time.sleep(2)

allListings = web.find_elements(By.CLASS_NAME, 'l-searchResult')

#allListingsPage = web.current_url

#Look into implicit waits, such as implicitly_wait() could be a better option for the for loop below
for elt in allListings:
    elt.click()
    try:
        contactAgentBtn = web.find_element('xpath', '//*[@id="contact-agent-aside"]/div[2]/a')
        contactAgentBtn.click()
    except: #ElementNotInteractableException
        contactAgentBtn = web.find_element('xpath', '//*[@id="root"]/main/article[2]/div[2]/div[2]/a')
        contactAgentBtn.click()

    time.sleep(2)
 #   web.get(allListingsPage)
    time.sleep(2)
    web.back()
    time.sleep(4)
    web.back()
    time.sleep(4)


time.sleep(100)