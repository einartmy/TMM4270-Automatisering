# importing the requests library - MAKING REQUEST TO FUSEKI example.
import requests 

URL = "http://127.0.0.1:3030/kbe/query"

# defining a query params 
PARAMS = {'query':"""
INSERT {
    ?block kbe:hasVolume ?volume.
} 
WHERE {
  ?block a kbe:Block.
  ?block kbe:hasL ?length.
  ?block kbe:hasW ?width.
  ?block kbe:hasH ?height.
  BIND(?length * ?width * ?height AS ?volume).
} 
"""}
#PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>SELECT ?side WHERE {?cube a kbe:Cube.?cube kbe:hasSide ?side.}'} 
 
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

#Checking the result
print("Result:", r)