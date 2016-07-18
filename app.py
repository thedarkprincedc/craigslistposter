from BeautifulSoup import BeautifulSoup
from lxml import html
import requests
import mechanize

br1 = mechanize.Browser()

br = mechanize.Browser()
br.set_handle_robots(False)
response = br.open("https://accounts.craigslist.org/login")
br.select_form("login")
br['inputEmailHandle'] = "sirbrettmosley@gmail.com"
br['inputPassword'] = "DricasM4x"
br.submit();
#print br.response().read()
response = br.open("https://accounts.craigslist.org/login/home")
#print response

#tree = html.fromstring(response)
soup = BeautifulSoup(response)
#print "\n\n\n\n"

tbody = soup.findAll('table')[1].tbody
#print tbody.tr.find('td', 'postingID')
for row in tbody.findAll('tr'):
    status = row.find('td', 'status').text
    postid = row.find('td', 'postingID').text
    print row.find('td', 'buttons').div
    
    print row.find('td', 'expdate')
    br.select_form("login")
    br.submit();
    #for cells in row.findAll('td'):
    #    if cells['class'] == 'status Z':
    #        print cells.text
    #    if cells['class'] == 'status Z':
#print response.read()