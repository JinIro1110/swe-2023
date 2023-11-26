import boto3
import pymysql
import os
from dotenv import load_dotenv

class RDSConnector:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name, db_instance_identifier, database_name):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name
        self.db_instance_identifier = db_instance_identifier
        self.database_name = database_name

        load_dotenv()
        self.rds_client = boto3.client('rds', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key, region_name=self.region_name)

    def get_rds_endpoint(self):
        response = self.rds_client.describe_db_instances(DBInstanceIdentifier=self.db_instance_identifier)
        endpoint = response['DBInstances'][0]['Endpoint']['Address']
        return endpoint

    def connect_to_mysql(self):
        endpoint = self.get_rds_endpoint()
        conn = pymysql.connect(host=endpoint, user=os.getenv('USER_NAME'), password=os.getenv('USER_PASSWORD'), database=self.database_name, port=3306)
        return conn

    def execute_query(self, conn, sql_query):
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
            return result

    def close_connection(self, conn):
        conn.close()


