import re
from bs4 import BeautifulSoup
def parse_html(HTMLString):
    #dapetin semua tag yang sintaksnya kurung segitiganya sudah benar, belum dicek kevalidannya
    #1. filter tag yang kurungnya sudah valid
    #kalo kurungnya gak lengkap gak masuk list tags
    ActualTags = re.findall(r'<[^>]+>', HTMLString)
    noAttributeTags = []
    validTagKeywords =['html','head','body','title','link','script','h1','h2','h3','h4','h5','h6','p','br','em','b','abbr','strong','small','hr','div','a','img','button','form','input','table','tr','td','th']
    linkAttributes = ['rel','href']
    scriptAttributes = ['src']
    aAttributes = ['href']
    imgAttributes = ['src','alt']
    buttonAttributes = ['type']
    buttonTypes = ['submit','reset','button']
    formAttributes = ['action','method']
    formMethods = ['GET','POST']
    inputAttributes = ['type']
    inputTypes = ['text','password','email','number','checkbox']

    TagName = ""
    noAttributeTag =""

    soup = BeautifulSoup(HTMLString, "html.parser")
    return soup.find_all()

html_doc = """
<html>
    <body>
        <h1>Hello, BeautifulSoup!</h1>
        <ul>
            <li><a href="http://example.com">Link 1</a></li>
            <li><a href="http://scrapy.org">Link 2</a></li>
        </ul>
    </body>
</html>
"""

print(parse_html(html_doc))