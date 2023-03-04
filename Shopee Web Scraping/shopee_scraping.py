import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd



#Function to get the name of item
def get_item_name(soup,prop):
    item_name_obj = soup.find_all('div',class_='ie3A+n bM+7UW Cve6sh')
    for name in item_name_obj:
        prop['Item'].append(name.text)    


#Function to get the price of item
def get_item_price(soup,prop):
    item_price_obj = soup.find_all('div',class_='vioxXd rVLWG6')
    for price in item_price_obj:
        span = (price.find_all('span'))
        initial_list = []
        for i in range(len(span)):
            if i == 2:
                initial_list.append('-')
            initial_list.append(span[i].text)
        prop['Price'].append(''.join(initial_list))


#Function to get the link of item
def get_item_link(soup,prop):
    item_link_obj = soup.find_all('a', {'data-sqe': 'link'},href=True)
    for link in item_link_obj:
        prop['Link'].append(f"https://shopee.ph{link.get('href')}")


#Function to save the 'prop' dictionary as a CSV file in the current working directory
def write_as_csv(prop,item):
    df = pd.DataFrame.from_dict(prop,orient='index')
    df = df.transpose()
    df = df.to_csv(f'{item} price as of {date.today()}.csv',index=False,header=True)

#The main function
def sub_main(item,page,prop):

    options = Options()

    #maximizes the window when the browser is launched.
    options.add_argument("start-maximized") 

    #disables the automation switch to prevent detection by websites that block automated browser activity
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    #allows the browser to continue running even if the Python script exits.
    options.add_experimental_option("detach", True)

    #set to False to prevent the browser from using an automation extension
    options.add_experimental_option("useAutomationExtension", False)

    #specifies the location/filepath of brave.exe on my pc
    options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

    #downloads the appropriate webdriver for the browser. no need to download and specify the location of webdriver in pc 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)

    #opens the browser and directs to the given item's webpage
    driver.get(f'https://shopee.ph/search?keyword={item}&page={page}')

    #automatically scrolls down the web page in order to scrape all the desired elements in the page and then pauses the script for 3 seconds to allow the page to load. this is necessary because of Shopee's lazy loading feature. 
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.5);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    #gets the content of the webpage
    page_source = driver.page_source

    #converts the HTML content of the webpage to bs4 elements
    soup = BeautifulSoup(page_source,'html.parser')

    get_item_name(soup,prop)
    get_item_price(soup,prop)
    get_item_link(soup,prop)
    

    driver.close()


def main():
    #Prompts the user to input the desired item and then formats the text to comply with the URL's structure
    item_initial = str(input('Enter the name of the item: '))
    item = item_initial.replace(' ', '%20')

    #Prompts the user to input the desired number of pages to scrape
    pages = int(input('Enter number of pages to be scraped: '))
    
    #Dictionary where the scraped elements are stored as strings
    prop = {'Item':[],'Price':[],'Link':[]}

    for page in range(pages):
        sub_main(item,page,prop)

    write_as_csv(prop,item_initial)

if __name__ == '__main__':
    main()
    
    






    