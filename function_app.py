import azure.functions as func
import datetime
import json
import logging
from db import snowflakeDB
from functions.sales import SalesObject

app = func.FunctionApp()

#connect to snowflake
snowflakedb = snowflakeDB()
# ca = CustomerData(sf.get_session())

# data = ca.query_current_sales_result("WEB_SALES", "2450874", "2450936")
# print(data)

@app.route(route="customerData", auth_level=func.AuthLevel.ANONYMOUS)
def customerData(req: func.HttpRequest) -> func.HttpResponse:
    ca = SalesObject(snowflakedb.get_session())
    query_param = req.params.get("filterBy")
    if not query_param:
        query_param = "CUSTOMER"
    data = ca.query(query_param)
    try:
        response = func.HttpResponse(
            body=json.dumps(data), 
            status_code=200,
            mimetype="application/json"
        )
  
        return response
    except Exception as e:
        print("Error ",e)
        return func.HttpResponse(
            "Error ",
            status_code=500
        )

@app.route(route="sales", auth_level=func.AuthLevel.ANONYMOUS)
def sales(req: func.HttpRequest) -> func.HttpResponse:
    ca = SalesObject(snowflakedb.get_session())
    from_month = req.params.get("from")
    to_month = req.params.get("to")
    print(type(from_month))

    data = ca.query_current_sales_result("WEB_SALES", from_month, to_month)
    try:
        response = func.HttpResponse(
            body=json.dumps(data), 
            status_code=200,
            mimetype="application/json"
        )
  
        return response
    except Exception as e:
        print("Error ",e)
        return func.HttpResponse(
            "Error ",
            status_code=500
        )




# @app.function_name(name="customtimer")
# @app.timer_trigger(schedule="0 */5 * * * *", 
#               arg_name="customtimer",
#               run_on_startup=True) 
# def test_function(customtimer: func.TimerRequest) -> None:
#     print("fetch and update customer table from s3")



