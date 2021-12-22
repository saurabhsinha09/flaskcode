from flask import Response, request
from flask_restful import Resource
from myproject.models import Price, PriceSchema

price_schema = PriceSchema(many=True)  

class PriceApi(Resource):
    def get(self):
        prices = Price.query.all()
        result = price_schema.dump(prices)
        return result