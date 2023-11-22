import re

def isHTMLTagBracketsValid(tagCheck):
    regex = "<(\"[^\"]*\"|'[^']*'|[^'\">])*>"

    comp = re.compile(regex)

    if(tagCheck == None):
        return False
    
    if(re.search(comp,tagCheck)):
        return True
    else :
        return False
def parse_html():
    #dapetin semua tag yang sintaksnya kurung segitiganya sudah benar, belum dicek kevalidannya
    #1. filter tag yang kurungnya sudah valid
    #kalo kurungnya gak lengkap gak masuk list tags
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

    HTMLFilename = input()
    HTMLFile = "src/"+HTMLFilename
    with open(HTMLFile,'r') as file:
        HTMLStr = file.read()
    print(HTMLStr)
    tags = re.findall(r'<[^>]+>',HTMLStr) #extract semua tag dulu bodo amat valid apa gak, kalo typo gak ada kurung buka otomatis dilewatin
    print(tags)
    #CEK 1: cek apakah syntax kurung benar
    bracketStack = []
    tagCheck = []
    for tag in tags:
        bracketStack.clear()
        for char in tag:
            if(char == "<"):
                if(bracketStack): #kalau bracketStack tidak kosong (sudah ada karakter <), input kurung salah
                    tagCheck.append(False)
                    break
                else: #kalau kosong, push kurung <
                    bracketStack.append("<")
            elif(char == ">"):
                bracketStack.pop()
                tagCheck.append(True)
    print("#CEK 1: cek apakah syntax kurung benar")
    print(tagCheck)

    
    #CEK 2: cek apakah ada spasi TEPAT SETELAH KURUNG BUKA
    prevChar = ""
    tagCheck.clear()
    flag = True
    for tag in tags:
        flag = True
        for char in tag:
            if(char == " "):
                if(prevChar == "<"): #kalau spasi tepat setelah <
                    flag = False
                    break
            prevChar = char
        tagCheck.append(flag)
    print("CEK 2: cek apakah ada spasi TEPAT SETELAH KURUNG BUKA")
    print(tagCheck)    
    #if False in tagCheck: #gagal cek kurung di tag,syntax error
    #    return [],False

    #FIX 1. hilangin semua whitespace sebelum kurung tutup dan setelah karakter terakhir
    fixedTags = []
    tagFix = ""
    for tag in tags:
        listchar = [x for x in tag]
        for i in range(len(listchar)-1,-1,-1):
            if(listchar[i] == ">"):
                continue
            elif(listchar[i] != " "):
                break
            else:
                listchar[i] = ""
        fixedTags.append(tagFix.join(listchar))
    print(fixedTags)
    

                
                    
    
                
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


parse_html()