import requests 

URL = "http://localhost:3030/A3/query"

theQuery = '''
    PREFIX A3: <http://www.kbe.com/pump.owl#>
    SELECT ?pump
    WHERE {
	?pump a A3:Pump.
    }
'''
  
# defining a query params 
PARAMS = {'query': theQuery}  
 
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

#Checking the result
print("Result:", r.text)
data = r.json()
print("JSON:", data)



