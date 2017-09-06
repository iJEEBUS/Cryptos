import urllib                         ##
from bs4 import BeautifulSoup         ##
from terminaltables import AsciiTable ##
########################################

# Reads the entire HTML from the website that is passed through
f = urllib.urlopen('https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20130428&end=20170906')
# Turns the HTML into a BeautifulSoup object that can be manipulated
soup = BeautifulSoup(f, "lxml")

# Holds all of the historical data from a coin
historical_data = []

# Holds only the closing price data of a coin
closing_price_data = []

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Computes the SMA given a list of numbers.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def computeSMA(m):
    # Holds total of all numbers in the inputted list
    total = 0
    # Holds how many prices are added together
    number_of_prices = 0

    # Iterates though the inputted list
    for x in m:
        # Convert the data to a float
        price = float(x)
        # Running total of all the numbers in the list
        total += price
        # Running total of how many numbers used
        number_of_prices += 1

    # print the SMA of the numbers
    print(total/number_of_prices)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Extract all of the table data from the historical data section of the website
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def getAllData():
    # Temporary list to hold the data
    temp = []
    # Iterates through all of the td objects from the website
    for x in soup.find_all('td'):
        # Appends to the historical_data list
        temp.append(x)
    # Return temporary list
    return temp

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Pulls the data from the historical_data list and extracts just the closing
prices.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def createClosingPriceList(listedData, iterations):
    # Used to get the most recent closing price
    closing_price_index = 4
    # Used for the while loop so avoid infinite loops
    current_iteration = 0

    # Loops through the historical_data
    while current_iteration < iterations:
        # Append the closing price to closing_price_data
        closing_price_data.append(listedData[closing_price_index])
        # Closing prices are 7 indices apart from eachother
        closing_price_index += 7
        # Self explanatory
        current_iteration += 1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Gets all of the table data from the table on the website.
Places said data into the list table_data.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def cleanData(s):
    # Used in the cleaning of strings
    first_tag = ">"
    last_tag = "</"

    # Temporary list to hold the output of the cleaned numbers
    temp = []
    # Iterate over each item in the inputted list s
    for x in s:
        # Converts item to string to clean
        number_as_string = str(x)
        # Assigns name to the cleaned number
        cleaned_number = number_as_string[number_as_string.find(first_tag)+1:number_as_string.find(last_tag)]
        # Appends the clean number to the temporary list
        temp.append(cleaned_number)
    # Return the cleaned number list
    return temp

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Execute the entire program
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def run(days):
    historical_data = getAllData()
    closing_price_data = createClosingPriceList(historical_data, days)
    cleaned_closing_price_data = cleanData(closing_price_data)
    simple_moving_average = computeSMA(cleaned_closing_price_data)
    print(simple_moving_average)


if __name__ == "__name__":
    run()
