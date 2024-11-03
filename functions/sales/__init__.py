from datetime import datetime, timedelta
from snowflake.snowpark.functions import col, dateadd, to_date, to_decimal
import simplejson as json
from decimal import Decimal


class Sales:
    def __init__(self, **kwargs):

        self.db = kwargs.get('db')
        self.session = self.db.session

    def get_predicted_sales_result(self):
        """
            This function will return the data stored in snowflake(the predicted sales data) 
        """
        return {"data":{}}

    def get_sales(self, table, from_month, to_month):
        
        """
            This function will return the sales from and to month  
        """

        # julian_to_date = lambda x: datetime(4713, 1, 1) + timedelta(days=x-2451)

        # df = self.db.table(f"{table}").select("*").limit(50)
        fdf = self.db.execute('GET_SALES_WITH_CUSTOMER_NAMES.sql')
        # fdf = df.filter(
        #     (col("WS_SHIP_DATE_SK") >= from_month) & (col("WS_SHIP_DATE_SK") >= to_month)
        # )
        # final_res = fdf.apply(fdf.to_numeric, downcast='float')
        # df = self.session.sql(f"select * from  {self.SNOWFLAKE_DB}.TPCDS_SF100TCL.{table} LIMIT 100")

        # convert_to_float = lambda x: json.dumps(a, use_decimal=True) for a in x if instance(a, Decimal)
       
        def loop_through_values(d):
            data = {}
            for key, value in d.items():
                k = key
                v = value
                if isinstance(value, Decimal):
                    v = float(v)
                data[k] = v
            return data
        return [loop_through_values(row.as_dict()) for row in fdf]


