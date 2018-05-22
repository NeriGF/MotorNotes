import urllib.request
from common.utils import log
import models.quote_model
import traceback
import json


def put(currency_key, conversion_rate):
    ''' Adds quote to the quotes storage (quote_list) 
    Returns: JSON string \'{"<currency_key>": <convertion_rate>}\''''
    quote = models.quote_model.save(currency_key, conversion_rate)    
    return json.dumps(quote)

def get (currency_key):
    quote = models.quote_model.find_by_currency_key(currency_key)    
    return json.dumps(quote)

def get_all_quotes():
    ''' Returns all stored quotes in JSON format'''
    return json.dumps(models.quote_model.find_all())
    

