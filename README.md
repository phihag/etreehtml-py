etreehtml is a small,copy&pasteable Python library to parse HTML code into xml.etree.ElementTree.


# Installation

etreehtml has no dependencies. If dependencies are an option, you should really use [lxml](http://lxml.de/parsing.html) instead of etreehtml.
It requires Python 2.5 or newer, including Python 3.x with and *without* 2to3.

To install it, go ahead and copy the content of [`etreehtml.py`]((https://raw.github.com/phihag/etreehtml-py/master/etreehtml.py)) and paste it above your code. Alternatively, youc an of course download the file, put it in your application&#x27;s [module search path](http://docs.python.org/tutorial/modules.html#the-module-search-path) (for example, in the directory your other code resides in, and import it with `import etreehtml`.

# Example code

    
    doc = parseHTML('<html><p>Cont<br>ent</p></html>')
    text = etree_text(doc.find('//p'))
    assert text == 'Content'
```