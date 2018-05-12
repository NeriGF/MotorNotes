def get_raw(currency_in, currency_out):
    """"
    Calculates convertion_rate from currency_in to currency_out
    Returns: convertion_rate 
    
    Calculation is done based on ASSCI code of the first character in the currency string:
    val =  ord ( currency_in[0]) / ord (currency_out[0])
    """
    val = ord(currency_in[0])/ord(currency_out[0])
    return val

def to_json(currency_key, convertion_rate):
    """"
    Returns convertion rate in JSON format in the form 
    '{"EUR_USD":{"val":convertion_rate}}'
    where EUR_USD = currency_key
    """
    json_str = '{"' + currency_key +":{\"val\":" + str(convertion_rate) +'}}'
    return json_str
