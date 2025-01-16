# import request to extract api data and pandas for datafram
import requests
import pandas as pd 

# requests.get method to extract api
response = requests.get('https://api.datamuse.com/words?rel_rhy=funny')

if response.status_code == 200:

    # convert the text data in json
    data = response.json()

    # create a dataframe of the data
    df = pd.DataFrame(data)
    
    # save the file in csv format using pandas to_csv method
    df.to_csv("api_data.csv", index=False)

else:
    print(f"API request failed with status code: {response.status_code}")