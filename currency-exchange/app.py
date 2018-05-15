import readline ### this module will prevent from writing input prompt to STDERR
import resources.quote
import resources.transaction

from common.utils import log

def request_parameters():
    '''
    Returns: amount, currency_in, currency_out, conversion_rate, action
    Implements input loop
    Collects values from user input
    '''
    print ('**** Welcome to Currency Converter App ****')
    # TODO while loop until valid action is entered
    action = ''

    # TODO per action, add collection and validation of user input

    amount = 0
    currency_in = ''
    currency_out = ''
    conversion_rate = 0.0

    log('amount={:.2f}, in={}, out={}, rate={}, action={}'\
        .format(amount, currency_in, currency_out, conversion_rate, action))
    return (amount, currency_in, currency_out, conversion_rate, action)

def menu():
    ''' Returns action menu to be displayed to the user'''
    return (
        '''
        D Display available quotes [default]
        Q get Quote
        S Save the new conversion rate
        X Exchange amount into the new currency
        E Exit
        > '''
)

def is_currency(currency):
    """ Validates that currency is one of the supported currencies:
    'USD', 'GBP', 'EUR', 'AUD', 'JPY' """
    pass

def is_float(string):
    ''' validates that the string can be converted to the float '''
    pass

def normalize(action):
    """ Empty input defaults to action 'D'
    allows usage of upper and low case characters
    keeps only the first character as an action
    validates that the action is one of 'Q','S','D','E'
    Returns normalized action or empty string"""

    pass

def main_command_line():
    '''
    Calls method to collect input
    Logs input parametes and values returned by functions calls
    '''
    ### log entry
    log('Started')
    while True:
        (amount, currency_in, currency_out, conversion_rate, action) = request_parameters()

        log('{}\t{}\t{}'.format(currency_in, currency_out, amount))
        currency_key = currency_in + '_' + currency_out

        if action == 'Q':
            #### 1. Get  currency quote given a currency key
            ### calculate exchange rate from currency_in to currency_out and log value as string and as JSON string
            conversion_rate = resources.quote.get_raw(currency_key)
            ### convert quote data to JSON format
            quote_json = resources.quote.to_json(currency_key, conversion_rate)
            log('{}'.format(quote_json))
            print(quote_json)
        elif action == 'X':
            ### 2. Exchange amount to the new currency
            conversion_rate = resources.quote.get_raw(currency_key)
            amount_out = resources.transaction.exchange(amount, conversion_rate)
            log('{}\t{}'.format(conversion_rate, amount_out))
            ### convert transaction data to JSON format
            transaction_json = resources.transaction.to_json(amount, amount_out, currency_in, currency_out)
            log('{}'.format(transaction_json))
            print(transaction_json)
        elif action == 'S':
            ### 3. Save currency quote
            quote_saved = resources.quote.put(currency_key, conversion_rate)
        elif action == 'D':
            #### 4. Display list of all currency quotes
            quotes = resources.quote.get_all_quotes()
            print (quotes)
        elif action == 'E':
            #### 5. Exit
            break

    log('Ended')

if __name__ == '__main__':
    main_command_line()
