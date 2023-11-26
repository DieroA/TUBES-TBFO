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
        elif(attrList[i] == '"' or attrList[i] == '”'):
            if(len(quotationStack) == 0):
                quotationStack.append('"')
                mark = 2
            elif(quotationStack[0] == "'"):
                mark = 4
            else:
                quotationStack.pop()
                mark = 2
        elif(attrList[i] == " "):
            if(len(quotationStack) == 0):
                mark = 3
            else:
                mark = 4
        elif(attrList[i] == "'"):
            if(len(quotationStack) == 0):
                quotationStack.append("'")
                mark = 5
            elif(quotationStack[0] == '"'):
                mark = 4
            else: 
                quotationStack.pop()
                mark = 5
        else:
            if(len(quotationStack) == 0):
                mark = 0
            else:
                mark = 4
        marking[i] = mark
    return marking
def markingValidation(attrList):
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
        elif(attrList[i] == '"' or attrList[i] == '”'):
            if(len(quotationStack) == 0):
                quotationStack.append('"')
                mark = 2
            elif(quotationStack[0] == "'"):
                mark = 4
            else:
                quotationStack.pop()
                mark = 2
        elif(attrList[i] == " "):
            if(len(quotationStack) == 0):
                mark = 3
            else:
                mark = 4
        elif(attrList[i] == "'"):
            if(len(quotationStack) == 0):
                quotationStack.append("'")
                mark = 5
            elif(quotationStack[0] == '"'):
                mark = 4
            else: 
                quotationStack.pop()
                mark = 5
        else:
            if(len(quotationStack) == 0):
                mark = 0
            else:
                mark = 4
        marking[i] = mark
    return (len(quotationStack) == 0)
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
    # print(AttributesOnly)
    attrList = [x for x in AttributesOnly]
    # print(attrList)
    marking = markingAttributes(attrList)
    # print(marking)
    attrElmtList = getAttributes(marking,attrList)
    # print(attrElmtList)
    return attrElmtList
def getAttrStrValues(tag,token):
    AttributesOnly = tag[len(token)+1:]
    # print(AttributesOnly)
    attrList = [x for x in AttributesOnly]
    # print(attrList)
    marking = markingAttributes(attrList)
    # print(marking)
    attrStrValues = getStringValues(marking,attrList)
    # print(attrStrValues)
    return attrStrValues
def AttrQuotationValidation(tag,token):
    AttributesOnly = tag[len(token)+1:]
    # print(AttributesOnly)
    attrList = [x for x in AttributesOnly]
    # print(attrList)
    markingV = markingValidation(attrList)
    return markingV
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
    globalAttributes =['id','class','style']
    linkAttributes = ['rel','href','id','class','style']
    scriptAttributes = ['src','id','class','style']
    aAttributes = ['href','id','class','style']
    imgAttributes = ['src','alt','id','class','style']
    buttonAttributes = ['type','id','class','style']
    buttonTypes = ['submit','reset','button']
    formAttributes = ['action','method','id','class','style']
    formMethods = ['GET','POST']
    inputAttributes = ['type','id','class','style']
    inputTypes = ['text','password','email','number','checkbox']

    HTMLFile = "../src/" + HTMLFilename
    try:
        with open(HTMLFile,'r',encoding="utf8") as file:
            HTMLStr = file.read()
    except:
        print(f"Gagal membuka file html {HTMLFilename}.")
        exit()
    if("<html>" in HTMLStr):
        s1 = HTMLStr.split("<html>")[0]
        s1 = s1.rstrip()
        if(s1 != ""):
            return [],False
    if("</html>" in HTMLStr):
        s2 = HTMLStr.split("</html>")[1]
        s2 = s2.rstrip()
        if(s2 != ""):
            return [],False
        #1. periksa apakah ada string sebelum <html>
        
    tags = re.findall(r'<[^>]+>',HTMLStr) #extract semua tag dulu bodo amat valid apa gak, kalo typo gak ada kurung buka otomatis dilewatin
    # print(tags)
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
    # print("#CEK 1: cek apakah syntax kurung benar")
    # print(tagCheck)
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
    # print("CEK 2: cek apakah ada spasi TEPAT SETELAH KURUNG BUKA")
    # print(tagCheck)    
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
    
    #FIX 2. hilangin semua comment yang ada di html
    for tags in fixedTags:
        if(("<!--" in tags) and ("-->" in tags)):
            fixedTags.remove(tags)
    # print(fixedTags)
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
    # print("bool tag")
    # print(isTagValid)
    # print("tokens")
    # print(TokenOnly)
    # print("no bracket tag")
    # print(noBracketTags)
    if False in isTagValid: #gagal cek tag yang valid,syntax error
        return [],False
    
    #CEK 4: Cek keberadaan atribut wajib di tag tertentu
    #attribut wajib
    #link: rel
    #img: src
    flag = True
    TokenNew = []
    for token,tag in zip(TokenOnly,noBracketTags):
        if (not flag):
            break
        # print(token)
        AttrElmtList = getAttrElmtList(tag,token)
        # print(AttrElmtList)
        TokenNew.append(token)
        if(token == "input"):
            AttrStrValues = getAttrStrValues(tag,token)
            # print(AttrStrValues)
            for attr,val in zip(AttrElmtList,AttrStrValues):
                if(attr == "type"):
                    flag = ValidateValues([val],inputTypes)
                    if(flag):
                        TokenNew.append(attr)
                    else:
                        flag = False
                else:
                    TokenNew.append(attr)
        elif(token == "button"):
            AttrStrValues = getAttrStrValues(tag,token)
            # print(AttrStrValues)
            for attr,val in zip(AttrElmtList,AttrStrValues):
                if(attr == "type"):
                    flag = ValidateValues([val],buttonTypes)
                    if(flag):
                        TokenNew.append(attr)
                    else:
                        flag = False
                else:
                    TokenNew.append(attr)
        elif(token == "form"):
            AttrStrValues = getAttrStrValues(tag,token)
            # print(AttrStrValues)
            for attr,val in zip(AttrElmtList,AttrStrValues):
                if(attr == "method"):
                    flag = ValidateValues([val],formMethods)
                    if(flag):
                        TokenNew.append(attr)
                    else:
                        flag = False
                else:
                    TokenNew.append(attr)
        else:
            for attr in AttrElmtList:
                TokenNew.append(attr)
        # print(TokenNew)
    # print(flag)
    if(not flag):
        return [],False
    else:
        return TokenNew,True