Shopee Web Scraping Tool
=================================================

[Description]
=================================================

- shopee_scraping.py is a script that allows users to scrape the name, price, and link of a specified item from   the Shopee website. The script prompts the user to input the name of the item they want to scrape, as well as   the number of pages they want to scrape. It then uses Selenium and BeautifulSoup to automate the process of     navigating to the search results page and extracting the desired information. The script scrapes the     specified number of pages and stores the scraped data in a CSV file.

[Getting Started]
=================================================

- To use this script, you'll need to make sure that the required libraries are installed on your system. You     can do this by running the following command in your terminal:

			`pip install -r requirements.txt`

- This will install all the necessary third-party libraries listed in the requirements.txt file. Once the     libraries are installed, you can run the shopee_scraping.py script to scrape the name, price, and link of the   specified item from Shopee.


[Usage]
=================================================

- Clone or download the project
- Open your terminal and navigate to the directory containing shopee_scraping.py
- Make sure that the required libraries are installed
- Run the shopee_scraping.py script by following the command:

			`python shopee_scraping.py`

- There will be a prompt to enter the name of the item and number of pages you desire to scrape.

- After running the script, it will scrape the desired information and save it to a .csv file in your current     working directory. This file will contain a list of the items that were scraped from the website.



[Limitations and Possible Future Improvements]
=================================================

- The script lacks error handling for invalid user input
- It can only scrape one item per CSV file
- Outputs like price can't be sorted in correct ascending or descending order
- Scraping of multiple pages can be automated without the need of closing the web browser every iteration, This   would allow for more efficient and faster scraping of data.
- ETC

