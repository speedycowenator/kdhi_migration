import bs4
import urllib.request
import csv
import time


#------Need
#48500
#49000(only +300)

#47500
#48000
#------Done

#44500
#45000
#45500
#46500
#47000
current = 35200
end = current + 100
#end - 43000
links_range = range(current, end)
source_list = []
print("Initializing")
for code in links_range:
	try: 
		itteration = code
		print(code)
		print("Pre pull")
		link_base = "http://www.uriminzokkiri.com/index.php?ptype=ccentv&mtype=view&no="
		#itv/php_tmp/flvplayer.php?ptype=centertv&no="
		print("start")
		link = link_base + str(code) + "#pos"
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
			source_list.append(source)
	except:
		try:
			time.sleep(15)
			itteration = code
			print(code)
			print("Pre pull")
			link_base = "http://www.uriminzokkiri.com/index.php?ptype=ccentv&mtype=view&no="
			#itv/php_tmp/flvplayer.php?ptype=centertv&no="
			print("start")
			link = link_base + str(code) + "#pos"
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
				source_list.append(source)
		except:
			time.sleep(300)
			try: 
				itteration = code
				print(code)
				print("Pre pull")
				link_base = "http://www.uriminzokkiri.com/index.php?ptype=ccentv&mtype=view&no="
				#itv/php_tmp/flvplayer.php?ptype=centertv&no="
				print("start")
				link = link_base + str(code) + "#pos"
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
					source_list.append(source)
			except:
				pass



	print(itteration)
	itteration -= 1
with open('uri_video_links_{}.csv'.format(str(current)), 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',',
								quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		for source in source_list:
			filewriter.writerow([source])

print("Completed")
