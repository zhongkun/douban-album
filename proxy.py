import urllib2
import os
import os.path
import traceback
import hashlib
from random import choice


user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        ]

#Need more random cookie and user_agents,ensure http request safe

header = {}
header['User-Agent'] = choice(user_agents)
header['Referer'] = 'http://www.douban.com'


def download_image(url, path ):
    try:
        print path
        print url                
        sp = url.split('.')
        suffix = sp[len(sp)-1]
        if not os.path.exists(path):
            os.makedirs(path)


        path = '%s%s.%s' % (path, hashlib.md5(url).hexdigest(), suffix)
        if not os.path.isfile(path):
            req = urllib2.Request(url=url,headers=header)
            img_data = urllib2.urlopen(req).read()

            out = open(path,'wb+')
            out.write(img_data)
            out.close()

        return '%s.%s' % (hashlib.md5(url).hexdigest(), suffix)
    except:
        print traceback.print_exc()
