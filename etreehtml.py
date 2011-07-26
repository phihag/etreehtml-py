# -*- coding: utf-8 -*-

import StringIO
from HTMLParser import HTMLParser
import xml.etree.ElementTree

EMPTY_ELEMENTS = ['meta', 'link', 'br']
class EtreeHtmlParser(HTMLParser):
	def __init__(self, html=True, target=None):
		HTMLParser.__init__(self)
		if target is None:
			target = xml.etree.ElementTree.TreeBuilder()
		assert html
		self._target = target
		self._tags = []

	def handle_starttag(self, tag, attrs):
		self._target.start(tag, dict(attrs))
		if tag in EMPTY_ELEMENTS:
			self._target.end(tag)
		else:
			self._tags.append(tag)

	def handle_endtag(self, tag):
		if len(self._tags) > 0 and tag == self._tags[-1]:
			self._tags.pop()
		else:
			if tag in self._tags:
				while True:
					t = self._tags.pop()
					if t == tag:
						break
					self._target.end(t)
			else:
				return # Ignore a closed tag that hasn't been opened
		self._target.end(tag)

	def close(self):
		HTMLParser.close(self)
		for t in reversed(self._tags):
			self._target.end(t)
		return self._target.close()

	def handle_data(self, data):
		self._target.data(data)

def parses(html):
	return parse(StringIO.StringIO(html))

def parse(htmlf):
	return xml.etree.ElementTree.parse(htmlf, EtreeHtmlParser())
