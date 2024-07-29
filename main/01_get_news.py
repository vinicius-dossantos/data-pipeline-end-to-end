from newsapi import NewsApiClient

#api = NewsApiClient(api_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
api = NewsApiClient(api_key='b7530f3b765c4e7e9df66a956368b4e7')

print(api.get_everything(q='trump'))