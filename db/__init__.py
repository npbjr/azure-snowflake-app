
from snowflake.snowpark.session import Session
import snowflake.snowpark.functions as F
from dotenv import dotenv_values
import json
print(" --- import done ---")

class snowflakdb:

    def __init__(self, credentials):
        self.SNOWFLAKE_DB = "SNOWFLAKE_SAMPLE_DATA"

        print("---- Connecting to Snowflake ----")

        self.config_params = {
            "account":credentials['ACCOUNT'],
            "user":credentials['USER'],
            "password":credentials['PASSWORD'],
            "role":credentials['ROLE'],
            "warehouse":credentials['WAREHOUSE'],
            "database":self.SNOWFLAKE_DB,
            "schema":"TPCDS_SF100TCL"
        }

        self.session = Session.builder.configs(self.config_params).create()

        print("---- Connection Success ----")

    def session(self):
        return self.session

    def execute(self, script):
        with open(f'db/sql_scripts/{script}', 'r') as text:
            sql = text.read()
        return self.session.sql(sql).limit(50).collect()

    def get_json_format(self, sql_result): ...


