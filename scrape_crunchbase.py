#Importing libraries
import requests
import csv

class ScrapeCrunchbase:
    
    def __init__(self):
        
        self.URL = 'https://api.crunchbase.com/v3.1/odm-organizations?'
        self.user_key = '0e16b2fe757d7d7f3cf3607cfc9e9abd'
        self.PARAMS={'user_key':self.user_key, 'page':3, 'updated_since': 2015}
        
    def scrape_data(self):
        
        scraped_data = []
        
        #Extract data using a GET request
        resp = requests.get(url = self.URL, params = self.PARAMS) 
        json_resp = resp.json()
        items = json_resp['data']['items']
        
        for i in items:
            
            data = []
            
            data.append(i['properties']['name'])
            data.append(i['properties']['primary_role'])
            data.append(i['properties']['facebook_url'])
            data.append(i['properties']['linkedin_url'])
            data.append(i['properties']['city_name'])
            data.append(i['properties']['region_name'])
            data.append(i['properties']['country_code'])
            data.append(i['properties']['short_description'])
            
            scraped_data.append(data)
        
        return scraped_data
        
    
    def write_to_csv(self, data):
        
        fields = ['name', 'primary_role', 'facebook_url', 'linkedin_url', 
                'city_name', 'region_name', 'country_code', 'short_description']
        
        filename = 'database.txt'
        
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(data)
    
if __name__=="__main__":
    
    b = ScrapeCrunchbase()
    
    data = b.scrape_data()
    
    b.write_to_csv(data)
    