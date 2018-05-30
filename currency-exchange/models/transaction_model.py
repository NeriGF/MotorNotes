import json

class TransactionModel():
    
    ## TODO add class attributes here (total, tx list, id generator)
    
    def __init__(self, currency_in, currency_out, amount_in, amount_out, commission):
        ''' Initialization of all transaction attributes:
           currency_in, currency_out, amount_in, amount_out, commission, _id 
         
        '''
        pass
        
    def save(self):
        ''' increments total by commission amount of transaction;
        adds transaction object to the transaction storage
        Returns self '''
        
        pass

    def find_all():
        ''' Returns all transactions stored in transaction storage ''' 
        pass

    def get_total():
        '''Returns value of class attribute total'''
        pass


#### Run this test to see if your implementation works.    
if __name__ == '__main__':
    transaction = TransactionModel('USD', 'EUR', 100, 80, 10)
    transaction.save()
    transaction = TransactionModel('AUD', 'USD', 100, 75.19, 7.52)
    transaction.save()
    transaction = TransactionModel('USD', 'JPY', 100, 11071, 10)
    transaction.save()
        
    for transaction in TransactionModel.find_all():
        print(json.dumps(vars(transaction)))
   
    total  = TransactionModel.get_total()
    print ("Total {}" . format ('%.2f' % total))
    
    
    
