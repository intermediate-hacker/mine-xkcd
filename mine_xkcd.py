import sys
import urllib2
import urllib
import os
from bs4 import BeautifulSoup

def download_three_times(img, down_path, use_wget, verbose, attempt=0):

	if verbose: print "Attempt:", attempt

	try:
		if use_wget:
			wget.download(img, down_path)
		else:
			urllib.urlretrieve(img, down_path)
	except:
		if attempt < 3:
			download_three_times(img, down_path, use_wget, verbose, attempt+1)
			return
		else:
			print "Failed."
			return

	print "Downloaded."

def open_three_times(i, use_wget, verbose, attempt = 0):
		soup = None

		if verbose: print "Attempt:", attempt
		try:
			if use_wget:
				url = "http://xkcd.com/" + str(i) + "/"
				index_file = str(i) + ".temp"
				wget.download(url, index_file)
				soup = BeautifulSoup(open(index_file))
				os.remove(index_file)
			else:
				url = "https://xkcd.com/" + str(i) + "/"
				f = urllib2.urlopen(url)
				soup = BeautifulSoup(f.read())
		except:
			if attempt < 3:
				open_three_times(i, soup, use_wget, attempt+1)
				return "FAILED"
			else:
				if verbose: print "Failed"
				return "FAILED"

		img = "http:" + soup.find("div", {"id" : "comic"}).img["src"]
		return img

		if verbose: print "Opened url"


def extract(path, last, use_wget, verbose, start):
	if use_wget: import wget

	if verbose:
		print "Beginning."
		if use_wget: print "Using wget."

	for i in range(start, last + 1):
		if verbose: print "Loading url: ", i

		img = open_three_times(i, use_wget, verbose)

		ext = ".png"
		if i < 120: ext = ".jpg"

		down_path = path + "/" + str(i) + ext

		if verbose: print "Downloading: ", i, " to ", down_path
		download_three_times(img, down_path, use_wget, verbose)


if __name__ == "__main__":
	if "--help" in sys.argv:
		print "usage: ", sys.argv[0], "<directory> <last comic index> <options>"

	else:
		use_wget = False
		verbose = False
		start = 1

		if "--wget" in sys.argv:
			use_wget = True

		if "--verbose" in sys.argv:
			verbose = True

		if "--start" in sys.argv:
			val_index = sys.argv.index("--start") + 1

			try: start = int(sys.argv[val_index])
			except:
				print "Syntax error. Use --help. Using default start value"
				start = 1				

		extract(sys.argv[1], int(sys.argv[2]), use_wget, verbose, start)