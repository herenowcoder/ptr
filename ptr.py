#!/usr/bin/env python3
from selenium import webdriver as wd
import sys, time, socket

WD_PORT = 8910

sentence = ' '.join(sys.argv[1:])

try:
    socket.create_connection(('localhost', WD_PORT))
    d = wd.PhantomJS(port=WD_PORT)
except socket.error:
    d = wd.PhantomJS()

d.get('http://translate.google.pl/#en/pl')
d.find_element_by_id('gt-otf-switch').click()
s = d.find_element_by_id('source')
r = d.find_element_by_id('result_box')
c = d.find_element_by_id('gt-submit')
s.clear()
s.send_keys(sentence)
c.click()
while not r.text: time.sleep(0.100)
print(r.text)
