#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import os
import sys
import urllib  
import urllib2  
import cookielib  

SITE = 'http://example.com:8888'
if __name__ == "__main__":
    if len(sys.argv) >= 3:
        try:
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))  
            urllib2.install_opener(opener)  
            if sys.argv[1] == 'c':#create
                msg = " ".join(sys.argv[2:])
                req = urllib2.Request(SITE,urllib.urlencode({"title":msg}))  
            if sys.argv[1] == 'd':#done
                req = urllib2.Request(SITE,urllib.urlencode({"tid": int(sys.argv[2]), "done":1}))  
            if sys.argv[1] == 'u':#update content
                req = urllib2.Request(SITE,urllib.urlencode({"tid": int(sys.argv[2]), "content": open(sys.argv[3]).read()}))  
            if sys.argv[1] == 'o':#change order
                req = urllib2.Request(SITE ,urllib.urlencode({"tid":int(sys.argv[2]), "order":0}))  

            resp = urllib2.urlopen(req)  
            os.system("growl -nostiky %s"%resp.read())
        except Exception, e:
            os.system("growl -nostiky NetworkError")
    else:
        os.system("growl -nostiky no argument")
