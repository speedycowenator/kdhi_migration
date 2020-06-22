import bs4
import urllib.request
import csv
import time

print("Pre pull")
link_base = "http://www.uriminzokkiri.com/index.php?ptype=ccentv&mtype=view&no="
link = link_base + str(45000) + "#pos"
print(link)
webpage=str(urllib.request.urlopen(link).read())
soup = bs4.BeautifulSoup(webpage, features="lxml")
print("pre-video")
videos = soup.findAll('video')
for video in videos:
	#print(video)
	tags = video.findAll("source") 

	tag_string = '' 
	for tag in tags:
		tag_string += str(tag)
	tag_string = tag_string.split('"')
	source = (tag_string[1])
print(source)