def exchange(amount_from, conversion_rate):
    '''
    Returns: amount (a positive float with 2-digits precision)
    '''
    amount_to = (float(amount_from) * conversion_rate)
    return ('%.2f' % amount_to)

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
