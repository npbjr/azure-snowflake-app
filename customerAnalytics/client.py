
class CustomerData:
    def __init__(self, session):
        self.session = session

    def query(self, table):
        """
            query table information
        """
      
        df = self.session.table(f"{table}").select("*").limit(10).collect()
        # df = self.session.sql(f"select * from  {self.SNOWFLAKE_DB}.TPCDS_SF100TCL.{table} LIMIT 100")
        return [row.as_dict() for row in df]

        