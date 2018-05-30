import json

currency = ['USD', 'GBP', 'EUR', 'AUD','JPY']
currency_keys = ['USD_EUR','USD_GBP', 'USD_AUD','USD_JPY']
conversion_rates = [0.85, 0.74, 1.33, 110.71]
quote_dict ={}

### now we will build 25 key-value pairs having the existing ones

currency_keys.insert(0, 'USD_USD')
conversion_rates.insert(0,1.0)
for i  in range(len(currency)):
    for j  in range(len(currency)):
        key = currency[i] + '_' + currency[j]
        key1 = 'USD_' + currency[i]
        position1 = currency_keys. index(key1)
        conversion_rates1 = conversion_rates[position1]
        key2 = 'USD_' + currency[j]
        position2 = currency_keys. index(key2)
        conversion_rates2 = conversion_rates[position2]
        quote_dict[key] = (conversion_rates2/conversion_rates1)

class QuoteModel():
    
    def __init__(self, currency_key, conversion_rate):
        ''' Object initialzer '''
        self.currency_key = currency_key
        self.conversion_rate = conversion_rate

    def find_by_currency_key(currency_key):
        ''' Returns: QuoteModel object'''
        conversion_rate = quote_dict[currency_key]
        return QuoteModel(currency_key, conversion_rate)
    
    def save(self): 
        ''' Returns: QuoteModel object'''
        quote_dict[self.currency_key] = self.conversion_rate
        return QuoteModel(self.currency_key, self.conversion_rate)

    def find_all():
        ''' Returns:  list of all stored QuoteModel objects '''
        return [QuoteModel(k,v) for k,v in quote_dict.items()]

    def delete (currency_key):
        del quote_dict[currency_key]
        

   
if __name__ == '__main__':    
    for quote in QuoteModel.find_all():
        print(json.dumps(vars(quote)))
   
    
