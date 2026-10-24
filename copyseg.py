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
            cands.add(f'{string[0:i]}-{cand}-{string[i:]}')
    print(sorted(list(cands)))
    print(len(cands))

def copyseg_l(string):
    '''
    Copy-seg a la Gouskova: takes a substring of the input and prefixes or infixes it copying from the left.
    walks through the word, takes a spot in the word and copies every substring to the right of that spot. Returns the ignored pre-string, copy, and remainder of base
    '''
    cands = set()
    for i in range(0, len(string)):
        ignore = string[0:i]
        base = string[i:len(string)]
        for j in range(0, len(base)):
            copy = string[0:j+1]
            cands.add(f'{ignore}-{copy}-{base}')
    print(sorted(list(cands)))
    print(len(cands))


def epenthesis(string):
    outset=set()
    for i in range(0, len(string)+1):
        outset.add(f'{string[0:i]}V{string[i:]}')
    print(sorted(list(outset)))
    print(len(outset))


if __name__=="__main__":
    import sys
    string = sys.argv[1]
    print("\n\n\n")
    print("Applying copy-left")
    copyseg_l(string)
    print("\n\n\n")
    #copyseg(string)

    #epenthesis(string)
