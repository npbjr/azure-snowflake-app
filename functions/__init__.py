import json
from .sales import Sales

def create_function_apps(**kwargs):

    app = kwargs.get('app')

    func = kwargs.get('func')

    sales_info = Sales(**kwargs)
 
    @app.route(route="sales", auth_level=func.AuthLevel.ANONYMOUS)
    def sales(req: func.HttpRequest) -> func.HttpResponse:

        from_month = req.params.get("from")
        to_month = req.params.get("to")

        try:
            result = sales_info.get_sales("WEB_SALES", from_month, to_month)

            return func.HttpResponse(
                body=json.dumps(result),
                status_code=200,
                mimetype="application/json")

        except Exception as e:

            print(e)

            return func.HttpResponse(
                "Error ",
                status_code=500)
