# This is a python script to search for a repository in github
# Note: BeautifulSoup is required for this script

# Importing beautifulsoup
from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description='A search engine for Github.')
parser.add_argument("search_term", help="Enter the search term")

args = parser.parse_args()
str = args.search_term

url = "https://github.com/search?utf8=%E2%9C%93&q="+str
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

# Set of words whose results we want to avoid
exceptions = ["/topics","/search","/login","https://","/features","/mobile","/customer-stories","/security","/team","/enterprise","/explore","/collections","/trending","#start","/join","/marketplace","/pricing","/nonprofit","/stargazers","/issues"]

repos = ["Search Results"]
# printing the repo names
for link in soup.find_all('a'):
	repo_name = link.get("href")
	
	# checking if the name is present in the array of expections
	for j in range(len(exceptions)):
		exception=exceptions[j]
		flag = False
		if repo_name.find(exception) != -1:
			break
		else:	
			flag = True
	if flag:
		repos.append(repo_name+"\n")
		
print(*repos)
