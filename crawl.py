from mechanize import Browser

def crawl(j,linkset):
	if j>=len(linkset):
		return
	else:
		try:								#to handle E404
			br = Browser()
			br.set_handle_robots(False)
			br.open(linkset[j])
			f = open('linkset.txt','a')
			for i in br.response().read().split("<a href")[1:]:
				try:
					link = i.split(">")[0].split("\"")[1]
					if 'http' in link:
						if link not in linkset:
							linkset.append(link)
							f.write(linkset[-1])
							f.write("\n")
				except:
					pass
			print j
			crawl(j+1,linkset)
		except:
			crawl(j+1,linkset)
linkset=['https://www.google.com']
crawl(0,linkset)







