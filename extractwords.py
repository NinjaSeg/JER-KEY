#!/bin/python
import xml.etree.ElementTree as ET
tree = ET.parse('dialog.xml')

import string

wordpop=dict()
for dialog in tree.findall('.//dialog'):
	for line in dialog.text.upper().splitlines():
		words = line.split()
		if len(words) > 1:
			words.pop(0)
			for word in words:
				word = word.strip(string.punctuation)
				wordpop[word] = wordpop.get(word,0) + 1

from operator import itemgetter
wordpop = sorted(wordpop.iteritems(), key=itemgetter(1), reverse=True)

f=open('/usr/share/dict/words','r')
dict=set(f.read().upper().splitlines())

for word in wordpop:
	if word[0] not in dict:
		#print '%i %s' % (word[1], word[0])
		print '%s' % (word[0])
