#!/usr/bin/env python
#coding: utf-8

__doc__=""" 2010-12-15 I am trying to register YY.duowan.com only to find out this nigger site had all my favorite id taken or reserved. I am trying to find 4-5 characters and short ones out of urbandictionary.com as my new minor id and Gmail. Hence this script. It took me nearly one hor to crawl words start with A. Damn those defintions!"""

import re, urllib2
from urllib import unquote

#urbandictionary.com start with '[' and ends with '%EF%BF%BD' (\ufffd)

ud_words=['a']
last='a'

while 'Z\xC3\xA6zzzzzz' not in ud_words:
    page=urllib2.urlopen('http://www.urbandictionary.com/nearby.next.php?term='+last).read()
    r=re.findall(r'define\.php\?term=(.*?)\\\"', page, re.M)
    print ' '.join(r)
    last=r[-1]
    r=map(unquote, r)
    ud_words+=r

open('urbandictionary.txt').write('\r\n'.join(ud_words))

 