from hanspell import spell_checker
from soynlp.normalizer import *
from kiwipiepy import Kiwi
import re

def clean_str(text): # 불용어 처리
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s\n]'         # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','', string=text)
    text = re.sub('\n', '.', string=text)
    return text 

def spellcheck(text):
    spelled_sent = spell_checker.check(text)
    hanspell_sent = spelled_sent.checked

    return hanspell_sent

def normalize(text):
    emoticon_norm = emoticon_normalize(text, num_repeats= 2)
    repeat_norm = repeat_normalize(emoticon_norm, num_repeats= 2)
    
    return repeat_norm

def split(text): # 문장 분리
    kiwi = Kiwi()
    return kiwi.split_into_sents(text)

def preprocess_text(text):
    result = []
    clean_text = clean_str(text)
    spellcheck_text = spellcheck(clean_text)
    normalize_text = normalize(spellcheck_text)

    for sentence in split(normalize_text):
        result.append(sentence)

    return result
