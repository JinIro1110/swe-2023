import boto3
import pymysql

class RDSConnector:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name, db_instance_identifier, database_name):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name
        self.db_instance_identifier = db_instance_identifier
        self.database_name = database_name

        # AWS RDS 클라이언트 생성
        self.rds_client = boto3.client('rds', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key, region_name=self.region_name)

    def get_rds_endpoint(self):
        # RDS 인스턴스 엔드포인트 조회
        response = self.rds_client.describe_db_instances(DBInstanceIdentifier=self.db_instance_identifier)
        endpoint = response['DBInstances'][0]['Endpoint']['Address']
        return endpoint

    def connect_to_mysql(self):
        # MySQL 연결 설정
        endpoint = self.get_rds_endpoint()
        conn = pymysql.connect(host=endpoint, user='yknam', password='', database=self.database_name, port=3306)
        return conn

    def execute_query(self, conn, sql_query):
        # SQL 쿼리 실행
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
            return result

    def close_connection(self, conn):
        # 연결 종료
        conn.close()


