import os
from sentiment_analysis import BERTSentimentAnalyzer
from dotenv import load_dotenv
from preprocessing import preprocess_text
from rds_mysql import RDSConnector
from keyword_extraction import KeywordExtractor
import json
import mysql.connector

class SentimentAnalysisManager:
    def __init__(self):
        self.sentiment_analyzer = BERTSentimentAnalyzer()
        self.keyword_extractor = KeywordExtractor()
        self.keyword_dictionary = 'keyword_test.txt'
        self.user_dictionary = 'user_dictionary.txt'
        self.positive_keywords_dict = {}
        self.negative_keywords_dict = {}

    def sentiment_reanalysis(self, positive_text, negative_text):
        positive_processed_text = preprocess_text(positive_text)
        positive_preprocessed_texts = [sentence.text for sentence in positive_processed_text]

        positive_reviews = []
        negative_reviews = []

        for processed_text in positive_preprocessed_texts:
            sentiment = self.sentiment_analyzer.perform_sentiment_analysis(processed_text)
            if sentiment == 2:
                positive_reviews.append(processed_text + ".\n")
            elif sentiment == 0:
                negative_reviews.append(processed_text + ".\n")

        negative_processed_text = preprocess_text(negative_text)
        negative_preprocessed_texts = [sentence.text for sentence in negative_processed_text]

        for processed_text in negative_preprocessed_texts:
            sentiment = self.sentiment_analyzer.perform_sentiment_analysis(processed_text)
            if sentiment == 2:
                positive_reviews.append(processed_text + ".\n")
            elif sentiment == 0:
                negative_reviews.append(processed_text + ".\n")

        return positive_reviews, negative_reviews

    def process_reviews(self, reviews):
        for row in reviews:
            if isinstance(row, tuple):
                review_id = row[0]
                product_id = row[1]
                user_id = row[2]
                positive_text = row[3]
                negative_text = row[4]

                positive_reviews, negative_reviews = self.sentiment_reanalysis(positive_text, negative_text)

                positive_text_combined = " ".join(positive_reviews)
                keywords = self.keyword_extractor.process_text(
                    positive_text_combined,
                    user_dictionary_file=self.user_dictionary,
                    keyword_dictionary_file=self.keyword_dictionary
                )
                for keyword, _ in keywords:
                    self.positive_keywords_dict[keyword] = self.positive_keywords_dict.get(keyword, 0) + 1

                negative_text_combined = " ".join(negative_reviews)
                keywords = self.keyword_extractor.process_text(
                    negative_text_combined,
                    user_dictionary_file=self.user_dictionary,
                    keyword_dictionary_file=self.keyword_dictionary
                )
                for keyword, _ in keywords:
                    self.negative_keywords_dict[keyword] = self.negative_keywords_dict.get(keyword, 0) + 1
        # 결과 정렬
        positive_keywords_result = [{"keyword": keyword, "score": count} for keyword, count in self.positive_keywords_dict.items()]
        negative_keywords_result = [{"keyword": keyword, "score": count} for keyword, count in self.negative_keywords_dict.items()]

        # 정렬
        positive_keywords_result = sorted(positive_keywords_result, key=lambda x: x["score"], reverse=True)
        negative_keywords_result = sorted(negative_keywords_result, key=lambda x: x["score"], reverse=True)

        output_data = {
            "positiveKeywords": positive_keywords_result[:5],
            "negativeKeywords": negative_keywords_result[:5]
        }
        return output_data

if __name__ == "__main__":
    load_dotenv()
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region_name = 'ap-northeast-2'

    db_instance_identifier = 'swe-database'
    database_name = 'beluv'

    rds_connector = RDSConnector(aws_access_key_id, aws_secret_access_key, region_name, db_instance_identifier, database_name)

    connection = rds_connector.connect_to_mysql()

    sentiment_manager = SentimentAnalysisManager()
    cursor = connection.cursor()
    for i in range(1, 10):
        sql_query = f'select * from ProductReviews where productid = {i};'
        result = rds_connector.execute_query(connection, sql_query)

        json_result = sentiment_manager.process_reviews(result)

        # 상위 5개 키워드만 가져오도록 수정
        for j in range(5):
            positive_keyword_info = json_result['positiveKeywords'][j] if j < len(json_result['positiveKeywords']) else None
            negative_keyword_info = json_result['negativeKeywords'][j] if j < len(json_result['negativeKeywords']) else None

            positive_keyword = positive_keyword_info["keyword"] if positive_keyword_info else None
            positive_score = positive_keyword_info["score"] if positive_keyword_info else None

            negative_keyword = negative_keyword_info["keyword"] if negative_keyword_info else None
            negative_score = negative_keyword_info["score"] if negative_keyword_info else None

            query = """
                INSERT INTO ProductKeywords (ProductID, PositiveKeyword, PositiveRating, NegativeKeyword, NegativeRating)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (i, positive_keyword, positive_score, negative_keyword, negative_score)
            cursor.execute(query, values)

    connection.commit()
    cursor.close()
    print("Results inserted into the database.")

