#Add that if user re-runs the program it can detect properties it has already applied to and doesnt apply to them again
#For the intial city search bar could use this video in order to be able to call rightmove's api to speed up the processing time

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
fName = "John"
lName = "Appleseed"
telNum = "07928561045"
email = "johnappleseed@gmail.com"
#Need to add a message above where user inputs their address telling them the specific format to put it in e.g. "(House Number) Street Name City Postcode with space inbetween"
postcode = "EH1 2NG"
addressLine1 = "362B Castlehill"
addressLine2 = "Old Town"
adressCity = "Edinburgh"
currUserAddress = addressLine1 + " " + addressLine2 + " " + adressCity + " " + postcode
correctArea = False





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
rentBtn.click()

locationListContainer = web.find_element(By.XPATH, '//*[@id="locationIdentifier"]')
locationList = locationListContainer.find_elements(By.TAG_NAME, 'option')
for loc in locationList:
    if loc.text == city:
        print("Found city")
        correctArea = True
        loc.click()
        break

if correctArea == False:
    exit(1)

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
    
    detailsBtn = web.find_element(By.XPATH, '//*[@id="moreDetailsRequested"]')
    detailsBtn.click()

    viewingBtn = web.find_element('xpath', '//*[@id="toViewProperty"]')
    viewingBtn.click()

    fNameInput = web.find_element('xpath', '//*[@id="toViewProperty"]')
    fNameInput.send_keys(fName)

    telInput = web.find_element('xpath', '//*[@id="phone.number"]')
    telInput.send_keys(telNum)

    emailInput = web.find_element('xpath', '//*[@id="email"]')
    emailInput.send_keys(email)

    postcodeInput = web.find_element('xpath', '//*[@id="postcode"]')
    postcodeInput.send_keys(postcode)

    time.sleep(2)

    suggestedResultsContainer = web.find_element('xpath', '//*[@id="app-content"]/div/div/div/div[1]/form/div/div/div[6]/div[2]/ul')
    suggestedResults = suggestedResultsContainer.find_elements(By.TAG_NAME, 'li')

    for address in suggestedResults:
        text = address.text.replace(",", "")
        print(text)
        if currUserAddress in text:
            print("Found Address")
            address.click()
            break


    time.sleep(2)
 #   web.get(allListingsPage)
    time.sleep(2)
    web.back()
    time.sleep(4)
    web.back()
    time.sleep(4)


time.sleep(100)
