def isHTMLTagBracketsValid(tagCheck):
    regex = "<(\"[^\"]*\"|'[^']*'|[^'\">])*>"

    comp = re.compile(regex)

    if(tagCheck == None):
        return False
    
    if(re.search(comp,tagCheck)):
        return True
    else :
        return False