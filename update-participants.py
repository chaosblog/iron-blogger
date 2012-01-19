#!/usr/bin/python

import render
import os
import sys
import xmlrpclib
import subprocess


XMLRPC_ENDPOINT = 'http://blog-URL.tld/xmlrpc.php'  # Wordpress RPC-URL - e.g. http://chaosblog.wordpress.com/xmlrpc.php
USER            = 'username'  # wordpress-username
BLOG_ID         = 0
PAGE_ID         = 12

try:
    subprocess.call(['stty', '-echo'])
    passwd = raw_input("Password for %s: " % (USER,))
    print
finally:
    subprocess.call(['stty', 'echo'])

x = xmlrpclib.ServerProxy(XMLRPC_ENDPOINT)
page = x.wp.getPage(BLOG_ID, PAGE_ID, USER, passwd)

text = render.render_template('templates/users.tmpl')
page['description'] = text

x.wp.editPage(BLOG_ID, PAGE_ID, USER, passwd, page, True)
