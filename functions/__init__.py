import json
from .sales import Sales

def create_function_apps(**kwargs):


    db = kwargs.get('db')

    app = kwargs.get('app')

    func = kwargs.get('func')

    credentials = kwargs.get('credentials')

    sales_info = Sales(**kwargs)

    @app.route(route="sales", auth_level=func.AuthLevel.ANONYMOUS)
    def sales(req: func.HttpRequest) -> func.HttpResponse:

        from_month = req.params.get("from")
        to_month = req.params.get("to")

        try:

            result = sales_info.get_sales("WEB_SALES", "2450874", "2450936")

            return func.HttpResponse(
                body=json.dumps(result),
                status_code=200,
                mimetype="application/json"
            )
        except Exception as e:
             return func.HttpResponse(
                "Error ",
                status_code=500
            )
