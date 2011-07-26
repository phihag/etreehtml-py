# -*- coding: utf-8 -*-

from etreehtml import parseHTML,etree_text
import platform

def test_example():
	doc = parseHTML('<html><p>Cont<br>ent</p></html>')
	text = etree_text(doc.find('.//p'))
	assert text == 'Content'

def test_basic():
	html = '''<html><body>text</body></html>'''
	et = parseHTML(html)
	assert et.getroot().tag == 'html'
	assert et.find('./body').text == 'text'

	html = '''<html>
	<body>
		te<b id="1">x</b>t
	</body>
	</html>'''
	et = parseHTML(html)
	assert et.getroot().tag == 'html'
	assert et.find('.//b').get('id') == '1'
	assert et.find('.//b').text == 'x'

def test_brokenText():
	html = '<html><body>a<br/>b<br/>c</body></html>'
	et = parseHTML(html)
	assert etree_text(et.find('.//body')) == 'abc'

def test_emptyTags():
	html = '''<html>
	<meta name="foo" value="bar">
	<body>
		te<br><strong>x</strong>t
	</body>
	</html>'''
	et = parseHTML(html)
	assert et.getroot().tag == 'html'
	assert et.find('./meta').get('name') == 'foo'
	assert et.find('.//strong').text == 'x'
	assert len(et.findall('.//br')) == 1

def test_unclosedTags():
	html = '''<html>
	<body>
		te<br><strong>xt'''
	et = parseHTML(html)
	assert et.getroot().tag == 'html'
	assert et.find('.//strong').text == 'xt'
	assert len(et.findall('.//br')) == 1

def test_wronglyClosedTags():
	html = '''<html>
	<body>
		te</br><strong>x</em></strong>t
	</html>
	</body>'''
	et = parseHTML(html)
	assert et.getroot().tag == 'html'
	assert et.find('.//strong').text == 'x'
	assert len(et.findall('.//br')) == 0

	html = '</root-close><root></root>'
	et = parseHTML(html)
	assert et.getroot().tag == 'root'

if __name__ == '__main__':
	testfuncs = [f for fname,f in locals().items() if fname.startswith('test_')]
	for tf in testfuncs:
			tf()
	try:
		pyimpl = platform.python_implementation()
	except:
		pyimpl = '[unknown Python]'
	print('Tested on ' + pyimpl + ' ' + platform.python_version() + '.')
