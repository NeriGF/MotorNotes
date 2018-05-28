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
    # while loop until valid action is entered
    while True:
      input_menu = menu()
      try: reply = input('What do you want to do: ' + input_menu)
      except:
          action = 'E'
          break
      action = normalize(reply)
      if action == '':
          print('Invalid input <{}>'.format(reply))
      else:
          break

    amount = 0
    currency_in = ''
    currency_out = ''
    conversion_rate = 0.0

    if action == 'D' or action == 'E':
        pass
    if action == 'Q' or action == 'S' or action == 'X':
        while True:
            currency_in = input('Currency from [USD]: ')
            if currency_in == '': currency_in = 'USD'
            if not is_currency(currency_in):
                print('Invalid currency symbol <{}>'.format(currency_in))
                continue
            currency_out = input('Currency to [EUR]: ')
            if currency_out == '': currency_out = 'EUR'
            if not is_currency(currency_out):
                print('Invalid currency symbol <{}>'.format(currency_out))
                continue
            break
    if action == 'S':
        while True:
            conversion_rate = input('User-defined conversion rate: ')
            if conversion_rate == '': continue
            if not is_float(conversion_rate):
                print('Invalid float value <{}>'.format(conversion_rate))
                continue
            conversion_rate = float(conversion_rate)
            break
    if action == 'X':
        while True:
            amount = input('Amount to convert [0.0]: ')
            if amount == '': amount = 0.0
            if not is_float(amount):
                print('Invalid float value <{}>'.format(amount))
                continue
            amount = float(amount)
            break

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
    return (currency in ['USD', 'GBP', 'EUR', 'AUD','JPY'])

def is_float(string):
    ''' validates that the string can be converted to the float '''
    try:
        float(string)
    except ValueError:
        return False
    return True

def normalize(action):
    """ Empty input defaults to action 'D'
    allows usage of upper and low case characters
    keeps only the first character as an action
    validates that the action is one of 'Q','S','D','E'
    Returns normalized action or empty string"""

    a = action.strip()
    if (a == ""): a='D'
    if (a[0].upper() in ['D','Q','S','X','E']):
        return a[0].upper()
    else:
        return ''

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
            quote_json = resources.quote.get(currency_key)
            log('{}'.format(quote_json))
            print(quote_json)
        elif action == 'X':
            ### 2. Exchange amount to the new currency
            transaction_json = resources.transaction.exchange(amount, currency_in, currency_out)
            log('{}'.format(transaction_json))
            print(transaction_json)
        elif action == 'S':
            ### 3. Save currency quote
            quote_json = resources.quote.put(currency_key, conversion_rate)
            log('{}'.format(quote_json))
            print(quote_json)
        elif action == 'D':
            #### 4. Display list of all currency quotes
            quotes = resources.quote.get_all_quotes()
            log(quotes)
            print (quotes)
        elif action == 'E':
            #### 5. Exit
            break

    log('Ended')

if __name__ == '__main__':
    main_command_line()
