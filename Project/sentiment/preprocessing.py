from hanspell import spell_checker
from soynlp.normalizer import *
import pandas as pd
import kss

def spellcheck(text):
    spelled_sent = spell_checker.check(text)
    hanspell_sent = spelled_sent.checked

    return hanspell_sent

def normalize(text): # 위에서 자음, 모음 제거하고 있긴함
    emoticon_norm = emoticon_normalize(text, num_repeats= 2)
    repeat_norm = repeat_normalize(emoticon_norm, num_repeats= 2)
    
    return repeat_norm

def split(text): # 문장 분리
    return kss.split_sentences(text)

def preprocess_text(text):
    if pd.isna(text):
        return ''
    result = []
    spellcheck_text = spellcheck(text)
    normalize_text = normalize(spellcheck_text)
    for sentence in split(normalize_text):
        result.append(sentence)

    return result

sentence = "안녕하세요. 안녕하세요."

result = preprocess_text(sentence)

print(result)