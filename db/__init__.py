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

    def test(self):
        try:
            df = self.session.sql("select * from  SNOWFLAKE_SAMPLE_DATA.TPCH_SF100.CUSTOMER LIMIT 10000000")
            
            #note the the group_by has a different spelling
            df2 = df.group_by("C_MKTSEGMENT").agg(F.sum("C_ACCTBAL").alias("SUBTOTAL"))
            
            # #create a total sum to be used for percentage calculation
            # acct_bal_total = df2.agg(F.sum("SUBTOTAL").alias("SUBTOTAL"))
            
            # #converting total sum to a pandas df, so as to extract a variable
            # pdf  = acct_bal_total.toPandas()
            # total_sum = pdf.iloc[0,0]
                
            # #create a new column called percentage using the total sum variable
            # df2 = df2.with_column("percentage",(df2["SUBTOTAL"]*100)/total_sum)
            # df2 = df2.sort(F.col("percentage").desc())
                
            #display the contents of the dataframe 
            df2.show()

        finally:
            #closing the connection
            self.session.close()

# if __name__ == "__main__":
#     sfdb = SnowFlakeDb()
#     print(sfdb.query("CUSTOMER"))