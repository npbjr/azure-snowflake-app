"""
Utilize AI prediction model
Feed list of sales data
the list will compose of data before and after ads has been shown
example data from january to may without ads
with data from august to december with ads
AI to create a prediction for the next months per ads type
"""
def get_prediction_result(data):...
def store_data_to_snowflake(data):...
def feed_to_prediction_model(data):
    ai_model = get_prediction_result(data)
    store_data_to_snowflake(ai_model)