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
def markingAttributes(attrList):    
    #1. marking attributes
    #keterangan marking: 0: attribut 1: tanda "=" 2: dalam quotation 3: spasi diluar quotation 4. semua karakter di dalam quotation mark selain petik tutup
    marking = [0 for i in range(len(attrList))]
    mark = 0
    quotationStack = []
    for i in range(0,len(attrList)):
        if(attrList[i] == "="):
            if(len(quotationStack) == 0):
                mark = 1
            else:
                mark = 4
        elif(attrList[i] == '"'):
            if(len(quotationStack) == 0):
                quotationStack.append('"')
                mark = 2
            else:
                quotationStack.pop()
                mark = 2
        elif(attrList[i] == " "):
            if(len(quotationStack) == 0):
                mark = 3
            else:
                mark = 4
        else:
            if(len(quotationStack) == 0):
                mark = 0
            else:
                mark = 4
        marking[i] = mark
    return marking
def getAttributes(marking,attrList):
    attrElmt = ""
    attrElmtList = []
    for i in range(0,len(attrList)):
        if(marking[i] != 0):
            if(len(attrElmt) != 0):
                attrElmtList.append(attrElmt)
                attrElmt = ""
        else:
            attrElmt = attrElmt+attrList[i]
    return attrElmtList
def getStringValues(marking,attrList):
    attrElmt = ""
    attrElmtList = []
    for i in range(0,len(attrList)):
        if(marking[i] != 4):
            if(len(attrElmt) != 0):
                attrElmtList.append(attrElmt)
                attrElmt = ""
        else:
            attrElmt = attrElmt+attrList[i]
    return attrElmtList
def getAttrElmtList(tag,token):
    AttributesOnly = tag[len(token)+1:]
    #print(AttributesOnly)
    attrList = [x for x in AttributesOnly]
    #print(attrList)
    marking = markingAttributes(attrList)
    #print(marking)
    attrElmtList = getAttributes(marking,attrList)
    #print(attrElmtList)
    return attrElmtList
def getAttrStrValues(tag,token):
    AttributesOnly = tag[len(token)+1:]
    #print(AttributesOnly)
    attrList = [x for x in AttributesOnly]
    #print(attrList)
    marking = markingAttributes(attrList)
    #print(marking)
    attrStrValues = getStringValues(marking,attrList)
    #print(attrStrValues)
    return attrStrValues
def ValidateAttributes(attrElmtList,ValidAttributes):
    for attr in attrElmtList:
        if(not (attr in ValidAttributes)):
            return False
    return True
def ValidateValues(attrStringValues,ValidValues):
    for attr in attrStringValues:
        if(not (attr in ValidValues)):
            return False
    return True
def parse_html(HTMLFilename):
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

    HTMLFile = "../src/" + HTMLFilename
    with open(HTMLFile,'r') as file:
        HTMLStr = file.read()
    #print(HTMLStr)
    tags = re.findall(r'<[^>]+>',HTMLStr) #extract semua tag dulu bodo amat valid apa gak, kalo typo gak ada kurung buka otomatis dilewatin
    #print(tags)
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
    #print("#CEK 1: cek apakah syntax kurung benar")
    #print(tagCheck)
    if False in tagCheck: #gagal cek kurung di tag,syntax error
        return [],False
    
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
    #print("CEK 2: cek apakah ada spasi TEPAT SETELAH KURUNG BUKA")
    #print(tagCheck)    
    if False in tagCheck: #gagal cek kurung di tag,syntax error
        return [],False

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
    #print(fixedTags)

    #CEK 3: cek apakah tag yang diperiksa ada di list tag yang valid
    #1. hapus semua kurung di semua tag
    noBracketTags = []
    for tag in fixedTags:
        tag = tag.replace("<","")
        tag = tag.replace(">","")
        noBracketTags.append(tag)
    #2. cek kevalidan tag yang sudah dibuka
    isTagValid = []
    TokenOnly = []
    for tag in noBracketTags:
        tagChecker = ""
        tempToken =""
        for char in tag:
            if(char == "/"):
                tempToken = tempToken + char
                continue
            if(char == ' ' or char == '=' or char == '"'):
                break
            tagChecker = tagChecker+char
            tempToken = tempToken + char
        boolTag = tagChecker in validTagKeywords
        isTagValid.append(boolTag)
        TokenOnly.append(tempToken)
    #print("bool tag")
    #print(isTagValid)
    #print("tokens")
    #print(TokenOnly)
    #print("no bracket tag")
    #print(noBracketTags)
    if False in isTagValid: #gagal cek tag yang valid,syntax error
        return [],False
    
    #CEK 4: Cek keberadaan atribut wajib di tag tertentu
    #attribut wajib
    #link: rel
    #img: src
    flag = True
    for token,tag in zip(TokenOnly,noBracketTags):
        if(token == "link"): #cek apakah rel ada di attribut link
            attrElmtList = getAttrElmtList(tag,token)
            if(not("rel" in attrElmtList)): #cek apakah attribut rel ada di tag link
                flag = False
                break
            #periksa kevalidan attribut
            flag = ValidateAttributes(attrElmtList,linkAttributes)
        elif(token == "script"):
            attrElmtList = getAttrElmtList(tag,token)
            if(len(attrElmtList) != 0): #cek kevalidan attribut jika ada
                flag = ValidateAttributes(attrElmtList,scriptAttributes)
        elif(token == "a"):
            attrElmtList = getAttrElmtList(tag,token)
            if(len(attrElmtList) != 0): #cek kevalidan attribut jika ada
                flag = ValidateAttributes(attrElmtList,aAttributes)
        elif(token == "img"):
            attrElmtList = getAttrElmtList(tag,token)
            if(not("src" in attrElmtList)): #cek apakah attribut src ada di tag img
                flag = False
                break
            #periksa kevalidan attribut
            flag = ValidateAttributes(attrElmtList,imgAttributes)
        elif(token == "button"):
            attrElmtList = getAttrElmtList(tag,token)
            if(len(attrElmtList) != 0): #cek kevalidan attribut jika ada
                flag = ValidateAttributes(attrElmtList,buttonAttributes)
                if(not flag):
                    break
                attrStringValues = getAttrStrValues(tag,token)
                #print(attrStringValues)
                flag = ValidateValues(attrStringValues,buttonTypes)
        elif(token == "input"):
            attrElmtList = getAttrElmtList(tag,token)
            if(len(attrElmtList) != 0): #cek kevalidan attribut jika ada
                flag = ValidateAttributes(attrElmtList,inputAttributes)
                if(not flag):
                    break
                attrStringValues = getAttrStrValues(tag,token)
                #print(attrStringValues)
                flag = ValidateValues(attrStringValues,inputTypes)
        elif(token == "form"):
            attrElmtList = getAttrElmtList(tag,token)
            if(len(attrElmtList) != 0): #cek kevalidan attribut jika ada
                flag = ValidateAttributes(attrElmtList,formAttributes)
                if(not flag):
                    break
                attrStringValues = getAttrStrValues(tag,token)
                #print(attrStringValues)
                for attr,val in zip(attrElmtList,attrStringValues):
                    if(attr == "method"):
                        flag = ValidateValues([val],formMethods)
    #print(flag)
    if(not flag):
        return [],False
    else:
        return TokenOnly,True
    #CEK 5: Cek kebenaran syntax atribut

    #CEK 6: 
                
                    
    
                
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