# -*- coding: utf-8 -*-

import time
import nltk
import konlpy
from konlpy.corpus import kolaw
from konlpy.tag import Kkma

def Stats(k) :  #명사와 형용사의 값을 리턴함
    noun_print = kolaw.open(k).read()
    sum = 0
    for i in noun_print.splitlines():
        value = i.split(":")
        sum=int(value[1])+sum
    return sum

def Noun():
    noun = Kkma().nouns(readbook)   #명사를 추출
    f = open('noun.txt','w')    #사전에 단어를 저장
    f.writelines(noun)
    f.close()
    print('사전완성(명사)')

    if Stats('noun.txt') >= 0 :
        print("밝음(명사)")
    else :
        print("어두움(명사)")

def Adjective():
    adjective = konlpy.tag.Twitter().pos(readbook)
    grammar = """
    AP : {<A.*>*}
    """
    parser = nltk.RegexpParser(grammar).parse(adjective)

    f = open('adjective.txt','w')
    for subtree in parser.subtrees():
        if subtree.label()=='AP':
            b = ' '.join((e[0] for e in list(subtree)))+':\n'
            f.writelines(b)
    f.close()
    print('사전완성(형용사)')

    if Stats('adjective.txt') >= 0 :
        print("빠름(형용사)")
    else :
        print("느림(형용사)")

def Verb():
    verb = konlpy.tag.Twitter().pos(readbook)
    grammar = """
    VP : {<V.*>*}
    """
    parser = nltk.RegexpParser(grammar).parse(verb)

    f = open('verb.txt','w')
    for subtree in parser.subtrees():
        if subtree.label()=='VP':
            b = ' '.join((e[0] for e in list(subtree)))+':\n'
            f.writelines(b)
    f.close()
    print('사전완성(동사)')

def __main__() :
    Noun()  #명사 함수
    Adjective() #형용사 함수
    Verb()  #동사 함수
    
inbook = input()
t = time.time() #시간
readbook = kolaw.open(inbook).read()    #파일 읽어오기
__main__()
print('%.02f'%(time.time()-t)+'초 걸렸습니다.')  #시간