#!/usr/bin/env python
#! -*- coding: utf-8 -*-

# Author: Muhammad A. Tirmazi

import sys
import urllib2
import urllib
import os
from bs4 import BeautifulSoup

def download_image(img, down_path, use_wget, verbose, max_attempt, attempt=0):

	if verbose: print "Attempt:", attempt

	try:
		if use_wget:
			wget.download(img, down_path)
		else:
			urllib.urlretrieve(img, down_path)
	except:
		if attempt < max_attempt:
			download_image(img, down_path, use_wget, verbose, max_attempt, attempt+1)
			return
		else:
			print "Failed."
			return

	print "Downloaded."

def open_url(i, use_wget, verbose, max_attempt, attempt = 0):
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
			if attempt < max_attempt:
				open_url(i, soup, use_wget, max_attempt, attempt+1)
				return "FAILED"
			else:
				if verbose: print "Failed"
				return "FAILED"

		img = "http:" + soup.find("div", {"id" : "comic"}).img["src"]
		return img

		if verbose: print "Opened url"


def extract(path, last, use_wget, verbose, start, max_attempt):
	if use_wget: import wget

	if verbose:
		print "Beginning."
		if use_wget: print "Using wget."

	for i in range(start, last + 1):
		if verbose: print "Loading url: ", i

		img = open_url(i, use_wget, verbose, max_attempt)

		ext = ".png"
		if i < 120: ext = ".jpg"

		down_path = path + "/" + str(i) + ext

		if verbose: print "Downloading: ", i, " to ", down_path
		download_image(img, down_path, use_wget, verbose, max_attempt)


if __name__ == "__main__":
	if "--help" in sys.argv:
		print "usage: ", sys.argv[0], "<directory> <last comic index> <options>"

	else:
		use_wget = False
		verbose = False
		start = 1
		max_attempt = 3

		if "--wget" in sys.argv:
			use_wget = True

		if "--verbose" in sys.argv:
			verbose = True

		if "--tries" in sys.argv:
			val_index = sys.argv.index("--tries") + 1

			try: max_attempt = int(sys.argv[val_index])
			except:
				print "Syntax error. Use --help. Using default trie value"
				max_attempt = 3

		if "--start" in sys.argv:
			val_index = sys.argv.index("--start") + 1

			try: start = int(sys.argv[val_index])
			except:
				print "Syntax error. Use --help. Using default start value"
				start = 1		

		if not os.path.exists(sys.argv[1]):
			os.makedirs(sys.argv[1])		

		extract(sys.argv[1], int(sys.argv[2]), use_wget, verbose, start, max_attempt)