import json
from BeautifulSoup import BeautifulSoup
import os
import urllib2
from urllib import urlretrieve
import time
import logging

"Sample URL -->http://www.cartrade.com/new/Maruti-Suzuki/Esteem"
url = "http://www.cartrade.com/new/"
input_file = "car_database.txt"
def fetch_cars():
   count = 0
   logging.basicConfig(filename='carfetcher.log', level=logging.INFO)
   try:
	   f = open(input_file,"r")
	   current_dir = os.getcwd()
	   content = f.read()
	   data = json.loads(content)
	   for make in data :
		logging.info("Maker-->"+make)
		logging.info("--->")
		models = data[make]
		make_search = str(make).replace(" ","-")
		for model in models:
		    count = count + 1
		    logging.info("Model-->"+model)
		    model = str(model).replace(" ","-")
		    new_url = url + make_search + "/" + model
		    logging.info("URL--->"+new_url)
		    soup =BeautifulSoup(urllib2.urlopen(new_url).read())
		    #logging.info(soup)
		    for img in soup('img',{'class':'carModelImg'}):
			href = img['src']
			image_name = href.split("/")[-1]
			outpath = os.path.join(current_dir,image_name)
			logging.info("Downloading --->"+href)
			urlretrieve(href,outpath)
		    time.sleep(5)
	   print(count)		    
   except Exception as e:
	  print(e)
if __name__ == '__main__':
	fetch_cars()
