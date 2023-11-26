from kiwipiepy import Kiwi
from kiwipiepy.utils import Stopwords
from collections import Counter

class KeywordExtractor:
    def __init__(self):
        self.kiwi = Kiwi(model_type='sbg')
        self.stopwords = Stopwords()

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
        with open(keyword_dictionary_file, 'r', encoding='utf-8') as keyword_file:
            self.keyword_dictionary = set(keyword_file.read().splitlines())

    @staticmethod
    def read_file_to_tuples(file):
        lines = file.read().splitlines()
        return [tuple(line.split()) for line in lines]

    def extract_noun(self, text):
        result = self.kiwi.tokenize(text, stopwords=self.stopwords)
        noun_list = [token.form for token in result if token.tag in ['NNG', 'NNP', 'VV', 'XR', 'VA-I', 'VA']]
        return noun_list

    def process_text(self, text, stopwords_file=None, user_dictionary_file=None, keyword_dictionary_file = None):
        if stopwords_file:
            self.load_stopwords(stopwords_file)

        if user_dictionary_file:
            self.load_user_dictionary(user_dictionary_file)

        if keyword_dictionary_file:
            self.load_keyword_dictionary(keyword_dictionary_file)

        noun_list = self.extract_noun(text)
        filtered_noun_list = [noun for noun in noun_list if noun in self.keyword_dictionary]

        counter = Counter(filtered_noun_list)
        keyword_frequency_pairs = [(keyword, frequency) for keyword, frequency in counter.most_common()]

        return keyword_frequency_pairs

