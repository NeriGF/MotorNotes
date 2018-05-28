import json

currency = ['USD', 'GBP', 'EUR', 'AUD','JPY']
currency_keys = ['USD_EUR','USD_GBP', 'USD_AUD','USD_JPY']
conversion_rates = [0.85, 0.74, 1.33, 110.71]
quote_dict ={}

### now we will build 25 key-value pairs having the existing ones

currency_keys.insert(0, 'USD_USD')
conversion_rates.insert(0,1.0)

for i  in range(len(currency)):
    for j  in range(len(currency)):
        key = currency[i] + '_' + currency[j]
        key1 = 'USD_' + currency[i]
        position1 = currency_keys. index(key1)
        conversion_rates1 = conversion_rates[position1]
        key2 = 'USD_' + currency[j]
        position2 = currency_keys. index(key2)
        conversion_rates2 = conversion_rates[position2]
        quote_dict[key] = (conversion_rates2/conversion_rates1)

def find_by_currency_key(currency_key):
    ''' Returns: {currency_key: conversion_rate}'''
    return {currency_key:quote_dict[currency_key]}

def save(currency_key, conversion_rate): 
    ''' Saves currency passed data
    Returns: {currency_key: conversion_rate}
    '''
    quote_dict[currency_key] = conversion_rate
    return {currency_key:quote_dict[currency_key]}

def find_all():
    ''' Returns all available quotes as a list 
    {currency_key1: conversion_rate1,currency_key2: conversion_rate2, ...}'''
    return quote_dict

if __name__ == '__main__':    
    print(json.dumps(find_all()))
   
    
   