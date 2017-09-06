import urllib                         ##
from bs4 import BeautifulSoup         ##
from terminaltables import AsciiTable ##
########################################

f = urllib.urlopen('https://coinmarketcap.com/currencies/ethereum/#markets')
soup = BeautifulSoup(f, "lxml")

# Used in the cleaning of strings
first_tag = ">"
last_tag = "</"

# Holds all of the table data from the website
table_data = []
# Holds all of the indexing col
number_data = []
# Holds all of the exchanges col
exchange_data = []
# Holds all of the pairs col
pair_data = []
# Holds the volume over 24 hours col
volume_24_hrs_data = []
# Holds all of the prices col
price_data = []
# Holds all of the volume percentages col
volume_pct_data = []
# Holds all of the last updated col
last_update_data = []
# Dictionary where key = exchange and value = price of coin
m = {}
# Used to hold the info in dictionary m if needed to be used as a list
dictionary_list = []

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Gets all of the table data from the table on the website.
Places said data into the list table_data.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def getTableData():
    for x in soup.find_all("td"):
        table_data.append(x)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Gets all of the table data from the table on the website.
Places said data into the list table_data.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def createDataList(input):
    counter = 0

    if input == "numbers":
        counter = 0
        while counter < len(table_data):
            y = cleanData(first_tag, last_tag, str(table_data[counter]))
            number_data.append(y)
            counter += 7

    elif input == "exchanges":
        counter = 1
        while counter < len(table_data):
            clean_data = cleanData(first_tag, last_tag, str(table_data[counter]))
            deep_clean_data = deepCleanExchangeData(clean_data)
            exchange_data.append(deep_clean_data)
            counter += 7

    elif input == "pairs":
        counter = 2
        while counter < len(table_data):
            clean_data = cleanData(first_tag, last_tag, str(table_data[counter]))
            deep_clean_data = deepCleanExchangeData(clean_data)
            pair_data.append(deep_clean_data)
            counter += 7

    elif input == "volume_24_hrs":
        counter = 3
        while counter < len(table_data):
            clean_data = cleanData(first_tag, last_tag, str(table_data[counter]))
            deep_clean_data = deepCleanExchangeData(clean_data)
            volume_24_hrs_data.append(deep_clean_data)
            counter += 7

    elif input == "prices":
        counter = 4
        while counter < len(table_data):
            clean_data = cleanData(first_tag, last_tag, str(table_data[counter]))
            deep_clean_data = deepCleanExchangeData(clean_data)
            price_data.append(deep_clean_data)
            counter += 7

    elif input == "volume_pct":
        counter = 5
        while counter < len(table_data):
            clean_data = cleanData(first_tag, last_tag, str(table_data[counter]))
            deep_clean_data = deepCleanExchangeData(clean_data)
            volume_pct_data.append(deep_clean_data)
            counter += 7

    elif input == "last_update":
        counter = 6
        while counter < len(table_data):
            clean_data = cleanData(first_tag, last_tag, str(table_data[counter]))
            deep_clean_data = deepCleanExchangeData(clean_data)
            last_update_data.append(deep_clean_data)
            counter += 7

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Gets all of the table data from the table on the website.
Places said data into the list table_data.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def cleanData(start, end, s):
    return s[s.find(start)+1:s.find(end)]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Deep cleans the data that does not have all of the tags removed from the first
cleaning.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def deepCleanExchangeData(s):
    delete_to_this = ">"
    return s[s.find(delete_to_this)+1:]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Gets all of the table data from the website and creates lists that are filled
with specific data from the table data.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def fillDataLists():
    getTableData()
    createDataList('numbers')
    createDataList('exchanges')
    createDataList('pairs')
    createDataList('volume_24_hrs')
    createDataList ('prices')
    createDataList('volume_pct')
    createDataList('last_update')

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Gets all of the table data from the table on the website.
Places said data into the list table_data.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def execute():
    fillDataLists()
    '''
    print(number_data[0])
    print(exchange_data[0])
    print(pair_data[0])
    print(volume_24_hrs_data[0])
    print(price_data[0])
    print(volume_pct_data[0])
    print(last_update_data[0])
    '''

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Fills the dictionary with key = exhange and values = prices of coin.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def fillDictionary():
    for x in exchange_data:
        m[x] = price_data[exchange_data.index(x)]
    # Immediately creates a list of the dictionary
    makeList(m)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Makes a list that holds lists of the key and value of the dictionary m.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def makeList(dict):
    for key, value in dict.iteritems():
        temp = [key,value]
        dictionary_list.append(temp)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Asks the user which exchanges they wish to see.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def userInput():
    # Ask the user which exchanges they wish to see.
    exchanges = raw_input('Which exchanges do you want to check?\n(ls for list)\n')
    checkInput(exchanges)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Checks the user input. Either prints a list of the available exchanges or
the arbitrage opportunities between the specified exchanges.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def checkInput(input):
    if input.lower() == 'ls':
        for x in m:
            print(x)
    else:
        getExchanges(input)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Gets the exchange that is passed as an argument from the dictionary.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def getExchanges(input):
    exchanges = input.capitalize().split()
    for x in exchanges:
        print(m[x])

execute()
fillDictionary()

userInput()

# find the arbitrage possibilities
# find arbitrage possibilities with only certain exchanges

# Make the dictionary into a list so that you can have a generic method that
# determines the largest arbitrage opportunity based on the list that is
# inputted





'''
if __name__ == "__main__":
    start()
'''
