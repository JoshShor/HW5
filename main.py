import re

# Check if the string starts with "The" and ends with "Spain":

testString = "int A1 = 5"

def sepspacer(txt):
    x1 = re.sub("\(", " ( ", txt)
    x2 = re.sub("\)", " ) ", x1)
    x3 = re.sub("\:", " : ", x2)
    x4 = re.sub("\;", " ; ", x3)
    return x4

new_test_string = sepspacer(testString)

parsed = re.split("\s", new_test_string)  # split white space

def kword_searcher(txt):
    kword_stringer = '^int$|^if$|^else$|^float$'
    k_word_search = re.search(kword_stringer, txt)
    if k_word_search:
        return True
    else:
        return False

def oper_searcher(txt):
    oper_stringer = '^[=]$|^[+]$|^[>]$|^[*]$'
    oper_search = re.search(oper_stringer, txt)
    if oper_search:
        return True
    else:
        return False

def sep_searcher(txt):
    sep_stringer = '^[(]$|^[)]$|^[:]$|\"|^[;]$'
    sep_search = re.search(sep_stringer, txt)
    if sep_search:
        return True
    else:
        return False


def id_searcher(txt):
    id_stringer = ""
    k_word_search = re.search("^int$|^if$|^else$|^float$", txt)
    id_search = re.search(r'[A-Z|a-z]+\d+|[a-z|A-Z]+', txt)

    if not k_word_search:
        if id_search:
            return True
    else:
        return False

def lit_searcher(txt):
    lit_stringer = '\".*\"'
    floatstuff = '([0-9]*[.])[0-9]+'  # float (consists of 1 or more digits before and after decimal point)
    intstuff = '^[0-9]+$'
    lit_search1 = re.search(intstuff, txt)
    lit_search2 = re.search(floatstuff, txt)
    lit_search3 = re.search(lit_stringer, txt)
    if lit_search1 or lit_search2 or lit_search3:
        return True
    else:
        return False

for i in parsed:
    kwordsearch = kword_searcher(i)
    opersearch = oper_searcher(i)
    sepsearch = sep_searcher(i)
    idsearch = id_searcher(i)
    litsearch = lit_searcher(i)

    if kwordsearch:
        k_word = i
        print(k_word + " is a keyword")
    elif not kwordsearch:
        print(i + " is not a keyword")
    if opersearch:
        oper = i
        print(oper + " is a op")
    elif not opersearch:
        print(i + " is not a op")
    if sepsearch:
        sep = i
        if sep[0] == "\"":
            sep = "\""
        print(sep+ " is a separator")
    elif not sepsearch:
        print(i + " is not a separator")
    if idsearch:
        identifiers = i
        print(identifiers + " is an identifier")
    elif not idsearch:
        print(i + " is not an identifier")
    if litsearch:
        lit = i
        print(lit + " is a literal")
    elif not litsearch:
        print(i + " is not a literal")

def CutOneLineTokens(tinyPieLine):
    new_test_string = sepspacer(testString)
    parsed = re.split("\s", new_test_string)  # split white space

    k_word = ""
    oper = ""
    sep = ""
    identifiers = ""
    lit = ""

    for i in parsed:
        kwordsearch = kword_searcher(i)
        opersearch = oper_searcher(i)
        sepsearch = sep_searcher(i)
        idsearch = id_searcher(i)
        litsearch = lit_searcher(i)

        if kwordsearch:
            k_word = i
            # print(k_word)
        if opersearch:
            oper = i
            # print(oper)
        if sepsearch:
            sep = i
            if sep[0] == "\"":
                sep = "\""
            # print(sep)
        if idsearch:
            identifiers = i
            # print(identifiers)
        if litsearch:
            lit = i
            # print(lit)

    print("<type, token> list: [<key," + k_word + ">, <id," + identifiers + ">, <op," + oper + ">, <lit," + lit + ">]")

CutOneLineTokens(testString)