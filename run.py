import requests
import os
from datetime import datetime
import toml
import json
from dotenv import load_dotenv
import csv


def loadAPI(url):
    
     #the below 3 lines are there simply to test the understanding of how to work with .env
    load_dotenv()  #parse .env, and make those variable as enviromental variables
    key=os.getenv('API_key')
        
    try:
        response = requests.get(url)
        
        
        if response.status_code == 200:
            try:
                text_data = response.text
                json_data = json.loads(text_data)
                link=json_data['message']
                
            except json.JSONDecodeError as e:
                print(f"request failed: {str(e)}")
        else:
            print(f"it's failed to load data from API with status code: {response.status_code}")
            
    except requests.RequestException as e:
        print(f"exception: {str(e)}")
    return link

def output_csv(link):
    csv_file = "output.csv"
    with open(csv_file,'w') as f:
        f.write(link)
    

def run():
    
    app_config=toml.load('config.toml')
    url=app_config['web']['url']
    
    link=loadAPI(url)
    output_csv(link)

if __name__=='__main__': 
    run()
    
    

