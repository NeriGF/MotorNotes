import models.quote_model

def exchange(amount, currency_in, currency_out):
    '''
    Returns: JSON  string outlined in to_json fuction
    '''
    currency_key = currency_in + '_' + currency_out
    quote = models.quote_model.find_by_currency_key(currency_key)
    conversion_rate = quote[currency_key]
    amount_to = amount * conversion_rate
    return to_json( ('%.2f' % amount),  ('%.2f' % amount_to), currency_key, currency_out)

def to_json(amount, amount_out, currency_in, currency_out):
    '''
    Returns: A JSON string that is a response to a currency query:
    '{ "success" : true, "error" : "", 
            "source" : {"amount" : "<amount>", "currency" : "<currency_in>"}, 
            "target" : {"amount" : "<amount_out>", "currency" : "<currency_out>"}
    }'
    Preconditions:
        currency_in is a string
        currency_out is a string
        amount is a positive float
        amount_out is a positive float
    '''

    error = ''
    success = 'true'
    if amount_out == '0.00':
        error = "Error to convert currency"
        success = 'false'
    source = '{"amount" : "' + str(amount) +' ", "currency" : "' + currency_in + '"}'
    target = '{"amount" : "' + str(amount_out) +' ", "currency" : "' + currency_out + '"}'
    return '{ "success" : ' + success + ', "error" : "'+ \
        error +'", "source" : ' + source + ', "target" : ' + target +'}'
