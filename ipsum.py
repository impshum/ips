#!/usr/bin/python
import urllib, pyperclip
a = urllib.urlopen('http://loripsum.net/api/').read()
pyperclip.copy(a)
b = pyperclip.paste()
