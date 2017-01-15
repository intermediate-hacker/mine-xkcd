# mine-xkcd
Python (2.7x) script that downloads all XKCD comics within a given range so you can read them from your hard-drive anytime.

**Modules needed**

BeautifulSoup: **apt-get install python-bs4**

[Optional. If you want to use the "--wget" option.] Wget: pip install wget

Useage:

**python mine_xkcd.py [path to download] [last_comic_index]**

Optional arguments: --start n (start from the nth comic)

		    --wget (use the wget module for downloading)
		    
		    --verbose (print diagnostic information)
		    
		    --tries n (make n attempts to download file)

Examples:

Download comics 1 to 100 into directory "test/":

**python mine_xkcd.py test 100**

Download comics 95 to 100 into directory "hello/":

**python mine_xkcd.py test 100 --start 95**


