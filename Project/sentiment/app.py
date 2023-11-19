from rds_mysql import RDSConnector
from sentiment_analysis import BERTSentimentAnalyzer
import os
from dotenv import load_dotenv
from preprocessing import preprocess_text

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
    sql_query = 'select * from ProductReviews;'
    result = rds_connector.execute_query(connection, sql_query)

    review_texts = ""
    for row in result:
        if isinstance(row, tuple):
            product_id = row[1]
            positive_text = row[3]
            review_texts += positive_text
            negative_text = row[4]
            review_texts += negative_text

    print(preprocess_text(review_texts))

    # Close connection
    rds_connector.close_connection(connection)

    # sentiment_analyzer = BERTSentimentAnalyzer()

    # sentence = "세 정 감 이 나 쁘 지 아나요"
    # sentiment_analyzer.perform_sentiment_analysis(sentence)