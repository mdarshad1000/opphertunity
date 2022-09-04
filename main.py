# Importing requirements
import requests
from bs4 import BeautifulSoup
import html5lib

# Get the HTML
url = "https://builtin.com/women-tech"
page = requests.get(url)
htmlContent = page.content

# Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify())

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))


