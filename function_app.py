import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="http_snowflake_analytics", auth_level=func.AuthLevel.ANONYMOUS)
def http_snowflake_analytics(req: func.HttpRequest) -> func.HttpResponse:
    
    return func.HttpResponse(
        "snowflake integration using snowpark is in Progress", 
        status_code=200
    )

@app.route(route="http_snowflake_ingest_data", auth_level=func.AuthLevel.ANONYMOUS)
def http_snowflake_ingest_data(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(
        "snowflake integration using snowpark is in Progress", 
        status_code=200
    )
        