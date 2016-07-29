#!/usr/bin/env python
from selenium import webdriver
import sys, time

sentence = ' '.join(sys.argv[1:])
d = webdriver.PhantomJS()
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
