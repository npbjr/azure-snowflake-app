
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
        print(self.session)

    def get_session(self):
        return self.session

# if __name__ == "__main__":
#     sfdb = SnowFlakeDb()
#     print(sfdb.query("CUSTOMER"))