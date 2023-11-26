import os
from sentiment_analysis import BERTSentimentAnalyzer
from dotenv import load_dotenv
from preprocessing import preprocess_text
from rds_mysql import RDSConnector
from keyword_extraction import KeywordExtractor

def test(text, positive_reviews, negative_reviews):
    preprocessd_text = preprocess_text(text)
    preprocessd_texts = [sentence.text for sentence in preprocessd_text]

    for processed_text in preprocessd_texts:
        sentiment = sentiment_analyzer.perform_sentiment_analysis(processed_text)
        if sentiment == '긍정':
            positive_reviews += (processed_text + "\n")
        elif sentiment == '부정':
            negative_reviews += (processed_text + "\n")
    return positive_reviews, negative_reviews
    
if __name__ == "__main__":
    load_dotenv()
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region_name = 'ap-northeast-2'

    db_instance_identifier = 'swe-database'
    database_name = 'beluv'

    rds_connector = RDSConnector(aws_access_key_id, aws_secret_access_key, region_name, db_instance_identifier, database_name)

    connection = rds_connector.connect_to_mysql()

    sql_query = 'select * from ProductReviews where ProductID = 5;'
    result = rds_connector.execute_query(connection, sql_query)

    sentiment_analyzer = BERTSentimentAnalyzer()

    positive_reviews = ""
    negative_reviews = ""

    for row in result:
        if isinstance(row, tuple):
            product_id = row[1]
            positive_text = row[3]
            negative_text = row[4]
            positive_reviews, negative_reviews = test(positive_text + negative_text, positive_reviews, negative_reviews)


    stopwords_file = 'stopwords.txt'
    user_dictionary_file = 'user_dictionary.txt'
    keyword_dictionary_file = 'keyword_dictionary.txt'
    
    extractor = KeywordExtractor()
    positive_result = extractor.process_text(positive_reviews, stopwords_file = stopwords_file, user_dictionary_file=user_dictionary_file, keyword_dictionary_file=keyword_dictionary_file)
    negative_result = extractor.process_text(negative_reviews, stopwords_file = stopwords_file, user_dictionary_file=user_dictionary_file, keyword_dictionary_file=keyword_dictionary_file)
        
    print("긍정 키워드 및 빈도 수:")
    for keyword, frequency in positive_result:
        print(f"{keyword}: {frequency}회")

    print("부정 키워드 및 빈도 수:")
    for keyword, frequency in negative_result:
        print(f"{keyword}: {frequency}회")    

    rds_connector.close_connection(connection)
