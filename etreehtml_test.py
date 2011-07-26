# -*- coding: utf-8 -*-

import etreehtml
import xml.etree.ElementTree

def test_basic():
	html = '''<html><body>text</body></html>'''
	et = etreehtml.parses(html)
	assert et.getroot().tag == 'html'
	assert et.find('./body').text == 'text'

	html = '''<html>
	<body>
		te<b id="1">x</b>t
	</body>
	</html>'''
	et = etreehtml.parses(html)
	assert et.getroot().tag == 'html'
	assert et.find('//b').get('id') == '1'
	assert et.find('//b').text == 'x'

def test_emptyTags():
	html = '''<html>
	<meta name="foo" value="bar">
	<body>
		te<br><strong>x</strong>t
	</body>
	</html>'''
	et = etreehtml.parses(html)
	assert et.getroot().tag == 'html'
	assert et.find('./meta').get('name') == 'foo'
	assert et.find('//strong').text == 'x'
	assert len(et.findall('//br')) == 1

def test_unclosedTags():
	html = '''<html>
	<body>
		te<br><strong>xt'''
	et = etreehtml.parses(html)
	assert et.getroot().tag == 'html'
	assert et.find('//strong').text == 'xt'
	assert len(et.findall('//br')) == 1

def test_wronglyClosedTags():
	html = '''<html>
	<body>
		te</br><strong>x</em></strong>t
	</html>
	</body>'''
	et = etreehtml.parses(html)
	assert et.getroot().tag == 'html'
	assert et.find('//strong').text == 'x'
	assert len(et.findall('//br')) == 0

	html = '</root-close><root></root>'
	et = etreehtml.parses(html)
	assert et.getroot().tag == 'root'

