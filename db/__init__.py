print(" --- importing modules ---")
from snowflake.snowpark.session import Session
import snowflake.snowpark.functions as F
from dotenv import dotenv_values
import json

config = dotenv_values("./.env")
print(" --- import done ---")

class snowflakeDB:

    def __init__(self):
        self.SNOWFLAKE_DB = "SNOWFLAKE_SAMPLE_DATA"

        print("---- Connecting to Snowflake ----")


        self.config_params = {
            "account":config.get('ACCOUNT'),
            "user":config.get('USER'),
            "password":config.get('PASSWORD'),
            "role":config.get('ROLE'),
            "warehouse":config.get('WARHOUSE'),
            "database":self.SNOWFLAKE_DB,
            "schema":"TPCDS_SF100TCL"
        }

        self.session = Session.builder.configs(self.config_params).create()

        print("---- Connection Success ----")
        print(self.session)

    def get_session(self):
        return self.session

# if __name__ == "__main__":
#     sfdb = SnowFlakeDb()
#     print(sfdb.query("CUSTOMER"))