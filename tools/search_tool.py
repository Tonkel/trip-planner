import json
import os
from dotenv import load_dotenv

import requests
from langchain.tools import tool

#load the environment variables from the .env file, then assign the SERPER_API_KEY to a variable
load_dotenv()
SERPER_API_KEY = os.getenv('SERPER_API_KEY')


class SearchTools():

  @tool("Search the internet")
  def search_internet(query):
    """Useful to search the internet
    about a a given topic and return relevant results"""
    top_result_to_return = 5
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # check if there is an organic key (standard, unpaid results)
    if 'organic' not in response.json():
      return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
    else:
      results = response.json()['organic']
      string = []
      #formatting the results to be more readable
      #loop through the results and add the title, link and snippet to the string
      for result in results[:top_result_to_return]:
        try:
          string.append('\n'.join([
              f"Title: {result['title']}", f"Link: {result['link']}",
              f"Snippet: {result['snippet']}", "\n-----------------"
          ]))
        #if the result is not a dictionary, skip it
        except KeyError:
          continue

      return '\n'.join(string)