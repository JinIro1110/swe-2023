from kiwipiepy import Kiwi
from kiwipiepy.utils import Stopwords
from collections import Counter
import networkx as nx

class KeywordExtractor:
    def __init__(self):
        self.kiwi = Kiwi(model_type='sbg')
        self.stopwords = Stopwords()
        self.keyword_dictionary = {}

    def load_stopwords(self, stopwords_file):
        with open(stopwords_file, 'r', encoding='utf-8') as stopword_file:
            stopwords_tuples = self.read_file_to_tuples(stopword_file)
            for s, pos in stopwords_tuples:
                self.stopwords.add((s, pos))

    def load_user_dictionary(self, user_dictionary_file):
        with open(user_dictionary_file, 'r', encoding='utf-8') as user_dictionary_file:
            user_dictionary_tuples = self.read_file_to_tuples(user_dictionary_file)
            for word, pos in user_dictionary_tuples:
                self.kiwi.add_user_word(word, pos)

    def load_keyword_dictionary(self, keyword_dictionary_file):
        self.keyword_dictionary = {}
        with open(keyword_dictionary_file, 'r', encoding='utf-8') as keyword_file:
            lines = keyword_file.readlines()
            for line in lines:
                keywords = line.strip().split()
                if keywords:
                    group_key = keywords[0]  # 대표 키워드는 첫 번째 키워드로 설정
                    if group_key not in self.keyword_dictionary:
                        self.keyword_dictionary[group_key] = set()
                    self.keyword_dictionary[group_key].update(keywords)

    @staticmethod
    def read_file_to_tuples(file):
        lines = file.read().splitlines()
        return [tuple(line.split()) for line in lines]

    def extract_noun(self, text):
        result = self.kiwi.tokenize(text, stopwords=self.stopwords)
        noun_list = [token.form for token in result if token.tag in ['NNG', 'NNP', 'VV', 'XR', 'VA-I', 'VA']]
        return noun_list

    def textrank(self, text):
        words = self.extract_noun(text)

        graph = nx.Graph()
        window_size = 4
        for i in range(len(words) - window_size + 1):
            window = words[i:i + window_size]
            for j in range(window_size):
                for k in range(j + 1, window_size):
                    if window[j] != window[k]:
                        graph.add_edge(window[j], window[k])

        scores = nx.pagerank(graph)
        return scores

    def process_text(self, text, stopwords_file=None, user_dictionary_file=None, keyword_dictionary_file=None):
        if stopwords_file:
            self.load_stopwords(stopwords_file)

        if user_dictionary_file:
            self.load_user_dictionary(user_dictionary_file)

        if keyword_dictionary_file:
            self.load_keyword_dictionary(keyword_dictionary_file)

        textrank_scores = self.textrank(text)

        noun_list = self.extract_noun(text)
        filtered_noun_list = []
        for noun in noun_list:
            for group_key, group_keywords in self.keyword_dictionary.items():
                if noun in group_keywords:
                    filtered_noun_list.append(group_key)
                    break
            else:
                filtered_noun_list.append(noun)

        # Filter out non-keyword items
        filtered_noun_list = [item for item in filtered_noun_list if item in self.keyword_dictionary]

        counter = Counter(filtered_noun_list)
        keyword_frequency_pairs = [(keyword, textrank_scores.get(keyword, 0)) for keyword, _ in counter.most_common()]

        return keyword_frequency_pairs

