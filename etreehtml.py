# -*- coding: utf-8 -*-

try:
	from io import StringIO
except ImportError: # pragma: nocover
	from StringIO import StringIO
try:
	from html.parser import HTMLParser
except ImportError: # pragma: nocover
	from HTMLParser import HTMLParser
import xml.etree.ElementTree

class _EtreeHtmlParser(HTMLParser):
	EMPTY_ELEMENTS = ['meta', 'link', 'br']
	def __init__(self, html=True, target=None):
		HTMLParser.__init__(self)
		if target is None:
			target = xml.etree.ElementTree.TreeBuilder()
		assert html
		self._target = target
		self._tags = []
	def handle_starttag(self, tag, attrs):
		self._target.start(tag, dict(attrs))
		if tag in self.EMPTY_ELEMENTS:
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
def parseHTML(htmlf):
	return xml.etree.ElementTree.parse(htmlf, _EtreeHtmlParser())
def parseHTMLs(html):
	return parseHTML(StringIO(html))
