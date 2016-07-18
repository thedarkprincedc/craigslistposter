#!/usr/bin/python
import re
import sys
from mechanize import Browser

if (len(sys.argv) < 2):
        print 'renew.py <username> <password>'
else:

        br = Browser()
        br.set_handle_equiv(False)
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        br.open('https://accounts.craigslist.org/')
        print br.title()

        br.select_form(name='login')

        br.form['inputEmailHandle'] = sys.argv[1]
        br.form['inputPassword'] = sys.argv[2]

        response = br.submit()  # submit current form
        print br.title()
        done = 'false'
        previousurl = ''
        while done == 'false':
                br.open('https://accounts.craigslist.org/')
                done = 'true'
                for f in br.forms():
                        for c in f.controls:
                                if c.value == 'renew':
                                        if previousurl != f.action:
                                                print f.action
                                                br.open(f.action)
                                                br.select_form(nr=2)
                                                response = br.submit()
                                                done = 'false'
                                                previousurl = f.action

