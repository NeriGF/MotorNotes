import readline ### this module will prevent from writing input prompt to STDERR
import resources.quote
import resources.transaction

from common.utils import log

         
def request_parameters():
    """
        Returns: amount, currency_in, currency_out
        Collects values from user input
    """
    amount_prompt = 'Enter the amount to convert > '
    amount = input(amount_prompt)
    currency_from_prompt = 'Enter the currency code to convert from,  a 3-character string > '
    currency_in = input(currency_from_prompt)
    currency_to_prompt = 'Enter the currency code to convert to,  a 3-character string > '
    currency_out = input(currency_to_prompt)
    return (amount, currency_in, currency_out)

def main_command_line():
    """
       Calls method to collect input
       Logs input parametes and values returned by functions calls
    """
    ### log entry 
    log("Started")
    ### collect input values and log them
    (amount, currency_in, currency_out) = request_parameters()
    log("{}\t{}\t{}".format(currency_in, currency_out, amount))
    
    ### calculate exchange rate from currency_in to currency_out and log value as string and as JSON string
    convertion_rate = resources.quote.get_raw(currency_in, currency_out)
    
    ### convert quote data to JSON format
    quote_json = resources.quote.to_json(currency_in + "_" + currency_out, convertion_rate)
    log("{}".format(quote_json))
    
    ### calculates amount in the currency_out
    amount_out = resources.transaction.exchange(amount, convertion_rate)
    log("{}\t{}".format(convertion_rate, amount_out))
    
    ### convert transaction data to JSON format
    transaction_json = resources.transaction.to_json(amount, amount_out, currency_in, currency_out)
    log("{}".format(transaction_json))
    
    print(transaction_json) 
    
    log("Ended")

if __name__ == '__main__':
    main_command_line()