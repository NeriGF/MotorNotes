def exchange(amount_from, conversion_rate):
    """
    Returns: amount (a positive float with 2-digits precision)
    """
    pass

def to_json(amount, amount_out, currency_in, currency_out):
    """
    Returns: A JSON string that is a response to a currency query:
    '{ "success" : true, "error" : "", 
            "source" : {"amount" : "<amount>", "currency" : "<currency_in>"}, 
            "target" : {"amount" : "<amount_out>", "currency" : "<currency_out>"}
    }'
    Preconditions:
        currency_in is a string
        currency_out is a string
        amount is a positive float
        amount is a positive float
    """
    pass
