from kiwipiepy import Kiwi
from kiwipiepy.utils import Stopwords
from collections import Counter
import networkx as nx # TextRank
kiwi = Kiwi()
def read_file_to_tuples(file_path): #텍스트 파일 튜플로 변환
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return [tuple(line.split()) for line in lines]
def extract_noun(text, stopwords_tuples, user_dictionary_tuples, window_size = 4):
    stopwords = Stopwords()
    for s, pos in stopwords_tuples:
        print(s, pos)
        stopwords.add((s, pos))
    for word, pos in user_dictionary_tuples:
        kiwi.add_user_word(word, pos)
    # 형태소 분석
    tokens = kiwi.tokenize(text, stopwords=stopwords)
    words = [token.form for token in tokens if token.tag in ['NNG', 'NNP', 'VV', 'XR', 'VA-I', 'VA']]
    # 단어 간 관계를 나타내는 그래프 생성
    graph = nx.Graph()
    for i in range(len(words) - window_size + 1):
        window = words[i:i + window_size]
        for j in range(window_size):
            for k in range(j + 1, window_size):
                if window[j] != window[k]:
                    graph.add_edge(window[j], window[k])
    # TextRank 실행
    scores = nx.pagerank(graph)
    return scores
kiwi.add_user_word("불용어", "NNP")
stopwords_file = 'stopwords.txt'
stopwords_tuples = read_file_to_tuples(stopwords_file)
user_dictionary_file = 'user_dictionary.txt'
user_dictionar_tuples = read_file_to_tuples(user_dictionary_file)
text = """아이가 쓸 로션 검색하다 대용량 저렴하게 잘 구매했어요 포장상태도 괜찮고 유효기간도 엄청 넉넉합니다.
향은 아이가 맡아도 거부감 없을 향이라 혼자서도 잘 바르네요 묽은 재형이라 촉촉한 느낌이 강하고 바르고 나서 끈적거림이 없어요.
우선 펌프 타입이라 사용이 편리해서 좋습니다.
제형이 조금 묽은 듯 하나 발림성이 괜찮습니다.
수분감이나 흡수성도 만족합니다.
가족들이 대부 건조한 피부들인데 보통 수비력 좋은 제품들은 끈적이는 제품들이 많아.
그런데 보습력이 괜찮아.
다들 만족하며 사용하고 있습니다.
한 달 가까이 사용하며 다른 건 그런대로 만족하며 사용하는데 워낙 인위적인 향은 안 좋아하는 편이라 처음 맡을 땐 강한 향이 언뜻 좋게 느껴지는데 좀."""
noun_list = extract_noun(text, stopwords_tuples, user_dictionar_tuples)
print(noun_list)
# counter = Counter(noun_list)
# print("키워드 및 빈도 수:")
# for keyword, frequency in counter.most_common():
#     print(f"{keyword}: {frequency}회")
# print("-----------\n")
# print("키워드 및 중요도:")
# for keyword, score in sorted(noun_list.items(), key=lambda x: x[1], reverse=True):
#     print(f"{keyword}: {score}")