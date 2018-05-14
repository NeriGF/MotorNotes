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

    ### TODO add setting success or error:
    
    source = '{"amount" : "' + str(amount) +' ", "currency" : "' + currency_in + '"}'
    target = '{"amount" : "' + str(amount_out) +' ", "currency" : "' + currency_out + '"}'
    return '{ "success" : true, "error" : false, "source" : ' + source + ', "target" : ' + target +'}'
