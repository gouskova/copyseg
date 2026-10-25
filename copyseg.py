#!/usr/bin/env python3

'''
formalizing copyseg
'''

def copyseg(string):
    '''
    Copy-seg a la McCarthy, Kimper & Mullin (2012)--formalized in Gouskova & Kasenov 
    takes a substring of the input, concatenates it with the input string by placing it somewhere inside or before or after
    '''
    outset = set() # this is the copying part
    for i in range(0, len(string)):
        outset.add(string[0:i+1]) #copy-left
        outset.add(string[i:])
        for j in range(i,len(string)): #copy-right
            outset.add(string[j])
            outset.add(string[i:j])
    outset.remove('')
    print(sorted(list(outset)))
    print(len(outset))
    cands = set()
    for cand in outset:#this is the concatenation part
        for i in range(0,len(string)+1):
            cands.add(f'{string[0:i]}-{cand}-{string[i:]}'.strip('-'))
    print(sorted(list(cands)))
    print(len(cands))
    return cands

def copyseg_l(string):
    '''
    Copy-seg a la Gouskova: takes a substring of the input and prefixes or infixes it copying from the left.
    walks through the word, takes a spot in the word and copies every substring to the right of that spot. Returns the ignored pre-string, copy, and remainder of base
    '''
    cands = set()
    for i in range(0, len(string)):
        ignore = string[0:i]
        base = string[i:len(string)]
        for j in range(0, len(base)+1):
            copy = base[0:j+1]
            cands.add(f'{ignore}-{copy}-{base}'.strip('-'))
    print(sorted(list(cands)))
    print(len(cands))
    return cands

def copyseg_r(string):
    '''
    Copy-seg a la Gouskova: takes a substring of the input and suffixes or infixes it copying from the right.
    walks through the word, takes a spot in the word and copies every substring to the left of that spot. Returns the ignored pre-string, copy, and remainder of base
    '''
    cands = set()
    for i in range(len(string)+1): 
        ignore = string[i:len(string)+1]
        base = string[0:i]
        if not base+ignore==string:
            print("ERROR")
        for j in range(len(base)):
            copy = base[j:len(base)]
            cands.add(f'{base}-{copy}-{ignore}'.strip('-'))
    print(sorted(list(cands)))
    print(len(cands))
    return cands





def epenthesis(string):
    outset=set()
    for i in range(0, len(string)+1):
        outset.add(f'{string[0:i]}V{string[i:]}')
    print(sorted(list(outset)))
    print(len(outset))


if __name__=="__main__":
    import sys
    string = sys.argv[1]
    if len(sys.argv)>2:
        if sys.argv[2] in ["l","L"]:
            copyseg_l(string)
        elif sys.argv[2] in ["r","R"]:
            copyseg_r(string)
    else:
        copyseg(string)

    #epenthesis(string)
