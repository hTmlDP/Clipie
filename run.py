import pip
def install(package):
    pip.main(['install', package])
from sys import exit
from urllib import urlopen, quote
try:
    import easygui
except:
    install('easygui')
    try:
    	import easygui
    except:
    	print '\033[91mCouldn\'t install the easy module!\nTry to run this script using sudo or "sudo pip install easygui"\033[91m'
try:
    import clipboard
except:
    install('clipboard')
    try:
    	import clipboard
    except:
    	print '\033[91mCouldn\'t install the clipboard module!\nTry to run this script using sudo or "sudo pip install clipboard"\033[0m'
try:
    import pynotify
except:
    install('py-notify')
    try:
        import pynotify
    except:
        print '\033[91mCouldn\'t install the pynotify module!\nTry to run this script using sudo or "sudo pip install py-notify"\033[0m' 
from time import sleep

try:
    pynotify and clipboard and easygui
except:
    print "\033[91m\033[1m[FATAL ERROR] Couldn't load required modules.\033[0m"
    exit(0)

def short_url(url):
    res=urlopen("http://po.st/api/shorten?apiKey=%s&longUrl=%s" % (config.API_KEY, quote(url))).read()
    exec('def content():\n\treturn %s' % res)
    return content()['short_url']
try:
    import config
except:
    print "\033[91m\033[1m[FATAL ERROR] Couldn't load config.py\033[0m"
    exit(0)
pynotify.init("Clipie")
print "\033[94mClipie has started successfully!\033[0m"
def checkurl(url):
	url=url[url.find('//')+2:]
	for i in config.BLACKLIST:
		if url.find(i)==0:
			return False
	for i in config.WHITELIST:
		if url.find(i)==0:
                        return 'dontask'
	return True
if __name__=='__main__':
    cache=clipboard.paste()
    while 1:
    	content=clipboard.paste()
    	if content!=cache:
    	    if content and (content.find('http://')==0 or content.find('https://')==0):
    		shorturl=content
		check=checkurl(content)
		if not check: cache=shorturl; continue
    		if len(content)>150:
    		    content=content[:150]+'...'
    		if check=='dontask' or easygui.ynbox('Do you want to shrink %s?' % content, 'Clipie', ('Yes', 'No')):
                    shorturl=short_url(shorturl)
    		    clipboard.copy(shorturl)
    		    n = pynotify.Notification("Clipie", "Copied URL: %s" % shorturl)
    		    n.show()
    		cache=shorturl


