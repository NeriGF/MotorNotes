import json

currency = ['USD', 'GBP', 'EUR', 'AUD','JPY']
currency_keys = ['USD_EUR','USD_GBP', 'USD_AUD','USD_JPY']
conversion_rates = [0.85, 0.74, 1.33, 110.71]
quote_dict ={}

### TODO populate quote_dict with 25 key-value pairs 'USD_EUR':0.85, 'USD_JPY':110.71 , 
### based on the above values


def find_by_currency_key(currency_key):
    ''' Returns: {currency_key: conversion_rate}'''
    pass

def save(currency_key, conversion_rate): 
    ''' Saves currency passed data
    Returns: {currency_key: conversion_rate}
    '''
    pass

def find_all():
    ''' Returns all available quotes as a list 
    [{currency_key1: conversion_rate1},{currency_key2: conversion_rate2}, ...]'''
    pass

if __name__ == '__main__':    
   print(json.dumps(find_all()))
   
    
   