from kiwipiepy import Kiwi
from kiwipiepy.utils import Stopwords
from collections import Counter
kiwi = Kiwi()

def read_file_to_tuples(file_path): #텍스트 파일 튜플로 변환
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return [tuple(line.split()) for line in lines]

def extract_noun(text, stopwords_tuples, user_dictionary_tuples):
    stopwords = Stopwords()
    for s, pos in stopwords_tuples:
        print(s, pos)
        stopwords.add((s, pos))

    for word, pos in user_dictionary_tuples:
        kiwi.add_user_word(word, pos)

    result = kiwi.tokenize(text, stopwords=stopwords)
    print(result)
    for token in result:
        if token.tag in ['NNG', 'NNP']:
            yield token.form

kiwi.add_user_word("불용어", "NNP")
stopwords_file = 'stopwords.txt'
stopwords_tuples = read_file_to_tuples(stopwords_file)

user_dictionary_file = 'user_dictionary.txt'
user_dictionar_tuples = read_file_to_tuples(user_dictionary_file)

text = "분석 결과에서 불용어만 제외하고 출력할 수도 있다. 사용자사전 추가했음하지만 분석이 내가 원하는 분석인지 얘가 원하는 분석인지  키워드 분석에 따라 달라질 듯? 분석이 분석에 분석하지만 분석함에 분석을 분석추 분석야"
noun_list = extract_noun(text, stopwords_tuples, user_dictionar_tuples)

counter = Counter(noun_list)

print("키워드 및 빈도 수:")
for keyword, frequency in counter.most_common():
    print(f"{keyword}: {frequency}회")