"""Module 11 Assignment
Julie Haas
LIS 5937
Spring 2021"""

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

''' Set the URL to the website and access the site with requests library '''
url = 'https://covidtracking.com/data/download'
response = requests.get(url)
#print(response)

'''Parse the html with BeautifulSoup for a nicer, nested data structure '''
soup = BeautifulSoup(response.text, 'html.parser')

'''
# Find line number of every line of code that has an <a> tag.
print("\nFind and print all 'a' tags:\n")
line_number = 0
for tag in soup.findAll("a"):
    line_number += 1
    print("{0} {1}: {2}".format(line_number, tag.name, tag.text))

# Test download of first file, located at line 77
one_a_tag = soup.findAll("a")[77]
link = one_a_tag["href"]
print(link) # prints "/data/download/alaska-history.csv" 

download_url = 'https://covidtracking.com'+ link
urllib.request.urlretrieve(download_url,+link[link.find('/*_')+1:])
'''

# Download the whole data set. Do a for loop through all a tags
line_count = 1 # variable to track what line you are on
for one_a_tag in soup.findAll('a', href=True):  # 'a' tags are for links
    if line_count >= 77: # code for text files starts at line 77
        link = one_a_tag['href']
        download_url = 'https://covidtracking.com/' + link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('/data/download/')+14:])
        time.sleep(1) # pause the code for a sec
    # add 1 for next line
    line_count += 1
