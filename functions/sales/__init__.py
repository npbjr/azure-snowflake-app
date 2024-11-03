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

        sql_res = self.db.execute('GET_SALES_CUSTOMER_INFO.sql')
 
        def convert_decimal_object_to_float(d):
            data = {}
            for key, value in d.items():
                k = key
                v = value
                if isinstance(value, Decimal):
                    v = float(v)
                data[k] = v
            return data
        return [convert_decimal_object_to_float(row.as_dict()) for row in sql_res]


