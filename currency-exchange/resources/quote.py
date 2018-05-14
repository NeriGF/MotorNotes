import urllib.request
from common.utils import log
import traceback

CURRENCY_QUOTE = 'https://free.currencyconverterapi.com/api/v5/convert?compact=y&q='

quote_list = []

def get_raw(currency_key):
    '''
    Gets convertion_rate in JSON format from CURRENCY_QUOTE url
    extracts value from JSON string and returns it as float
    Uses exception handling to log possible errors
    Returns: convertion_rate
    '''
    convertion_rate = 0.0
    ### TODO handle exceptions, extract convertion_rate from json string
    #data_source = urllib.request.urlopen(CURRENCY_QUOTE + currency_key)
    #json = data_source.read().decode('utf-8')
    #returned json format:
    #{"USD_EUR":{"val":0.836901}}
    #{"status":400,"error":"Invalid query format."}
    return convertion_rate

def to_json(currency_key, convertion_rate):
    '''
    Returns convertion rate in JSON format in the form
    '{"EUR_USD":{"val":convertion_rate}}'
    where EUR_USD = currency_key
    '''
    json_str = '{"' + currency_key +':{"val":' + str(convertion_rate) +'}}'
    return json_str

def put(currency_key, convertion_rate):
    ''' Adds quote to the quotes storage (quote_list) 
    Returns: quote - json string '''
    # TODO
    pass

def get_all_quotes():
    ''' Returns all stored quotes'''
    # TODO
    pass
