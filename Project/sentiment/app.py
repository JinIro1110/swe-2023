from rds_mysql import RDSConnector
import os
from sentiment_analysis import BERTSentimentAnalyzer
from dotenv import load_dotenv
from preprocessing import preprocess_text

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

    # RDS 데이터베이스 연결 정보 설정
    db_instance_identifier = 'swe-database'
    database_name = 'beluv'

    # Create an instance of the RDSConnector class
    rds_connector = RDSConnector(aws_access_key_id, aws_secret_access_key, region_name, db_instance_identifier, database_name)

    # Connect to MySQL
    connection = rds_connector.connect_to_mysql()

    # Execute SQL query
    sql_query = 'select * from ProductReviews LIMIT 10;'
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

    print("positive : ", positive_reviews)
    print("----------- :", type(positive_reviews))
    print("negative : ", negative_reviews)
    print("----------- :", type(negative_reviews))

    rds_connector.close_connection(connection)
