from models.quote_model import QuoteModel
from models.transaction_model import TransactionModel
import json

COMMISSION_RATE = 0.1 # 10% 

class Transaction: 

    def get(id) :
        '''  Given transaction id (integer) finds transaction and returns as the first element of a list.
         If transaction is not found returns an empty list '''
        pass
        
    def _to_json(self):
        '''
        Returns Transaction representation as JSON string:
        {"currency_in": "USD", 
        "currency_out": "EUR", 
        "amount_in": 1000.0, 
        "amount_out": 850.0, 
        "commission": 100.0, 
        "_id": 1}
        '''        
        pass

    
    def _calculate_commission (amount_in, currency_in):
        '''
        Calculates commision in USD given COMMISSION_RATE
        Returns: comission amount as a positive float
        '''
        pass
        

class TransactionList:
    def get(): 
        '''Returns  list of JSON formatted transactions:
        [{"currency_in": "USD", 
        "currency_out": "EUR", 
        "amount_in": 1000.0, 
        "amount_out": 850.0, 
        "commission": 100.0, 
        "_id": 1}
        {"currency_in": "USD", 
        "currency_out": "EUR", 
        "amount_in": 1000.0, 
        "amount_out": 850.0, 
        "commission": 100.0, 
        "_id": 2}, ...]
        ''' 
        pass

    def post(amount, currency_in, currency_out):
        '''
        given currency_in, currency_out and amount calculates amount_to and commision,  saves it in transaction storage
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
        currency_key = currency_in + '_' + currency_out
        conversion_rate = QuoteModel.find_by_currency_key(currency_key).conversion_rate
        amount_to = amount * conversion_rate
        commission = Transaction._calculate_commission(amount, currency_in)
        transaction = TransactionModel(currency_in, currency_out, amount, amount_to, commission)
        transaction.save()
        return Transaction._to_json(transaction)
             
         


class TotalIncome:
    def get():
        '''
        Returns: sum of commisions for  all stored exchange transactions
        
        '''
        pass 

    
