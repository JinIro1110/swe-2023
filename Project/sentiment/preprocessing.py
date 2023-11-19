from hanspell import spell_checker
from soynlp.normalizer import *
import pandas as pd
from kiwipiepy import Kiwi

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
    spellcheck_text = spellcheck(text)
    normalize_text = normalize(spellcheck_text)

    for sentence in split(normalize_text):
        result.append(sentence)

    return result
