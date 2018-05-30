import urllib.request
from common.utils import log
from models.quote_model import QuoteModel
import traceback
import json


class Quote:
    '''  
    Class to handle requests to update / retrieve quote
    '''
    def put(currency_key, conversion_rate):
        ''' Adds quote to the quotes storage (quote_list)
        If quote exists updates the existing one 
        Returns: quote in JSON format'''
        print (currency_key, conversion_rate)    
        quote = QuoteModel(currency_key, conversion_rate)
        quote.save()   
        return json.dumps(vars(quote))

    def get (currency_key):
        ''' Return: quote in JSON format '''
        quote = QuoteModel.find_by_currency_key(currency_key)    
        return json.dumps(vars(quote))

class QuoteList:
    ''' Colection of Quote objects'''
    def get ():
        ''' Returns all stored quotes as an array of JSON-formatted quote
        '''
        return [json.dumps(vars(quote)) for quote in QuoteModel.find_all()]   
    
