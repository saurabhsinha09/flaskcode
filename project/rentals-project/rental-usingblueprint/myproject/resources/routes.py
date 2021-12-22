from myproject.resources.rentalapi import PriceApi

def initialize_routes(api):
    api.add_resource(PriceApi, '/api/prices')