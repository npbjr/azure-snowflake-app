import azure.functions as func
from db import snowflakdb as db
from functions import create_function_apps
from jobs import create_cronjobs
from dotenv import dotenv_values

app = func.FunctionApp()

credentials = dotenv_values(".env")

instances = {"app": app, "credentials": credentials , "db": db(credentials), "func":func}


create_function_apps(**instances)





