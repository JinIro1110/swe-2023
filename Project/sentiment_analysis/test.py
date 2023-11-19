from rds_mysql import RDSConnector
# Example usage in another file
if __name__ == "__main__":
    # AWS 계정 정보 설정
    aws_access_key_id = ''
    aws_secret_access_key = ''
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
    for row in result:
        print(row)

    # Close connection
    rds_connector.close_connection(connection)