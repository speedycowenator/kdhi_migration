
import bs4
import urllib.request

url = 'https://kdhi.webflow.io/'
#url = 'https://kdhi-archive-code-builder.webflow.io/'

webpage=str(urllib.request.urlopen(url).read())
soup = bs4.BeautifulSoup(webpage, features = "lxml")
link = soup.find_all('script')
link_count = len(link)
java_loc = link_count - 2
java_location = link[java_loc]
java_location = java_location.get('src')
print(java_location)