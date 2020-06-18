import requests
import json


class ScrapeCrunchbase:
    
    def __init__(self):
        
        self.URL = 'https://api.crunchbase.com/v3.1/odm-organizations?'
        self.user_key = '0e16b2fe757d7d7f3cf3607cfc9e9abd'
        self.PARAMS={'user_key':self.user_key, 'updated_since': 2016}
        
    def scrape(self):
        resp = requests.get(url = self.URL, params=self.PARAMS) 
        json_resp=resp.json()
        return json_resp
        
        
        
if __name__=="__main__":
    
    b = ScrapeCrunchbase()
    
    a=b.scrape()
    print(a)