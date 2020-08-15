import requests
from bs4 import BeautifulSoup
import os.path
import pickle
import pathlib


HERE = pathlib.Path(__file__).parent

all_git_ignore = []

def _fetchAllModuleData():
	if os.path.isfile(f"{HERE}/cache_links.txt"):
		return "cache_links"
	else:
		r = requests.get("https://github.com/github/gitignore/")
		soup = BeautifulSoup(r.content,'lxml')
		links = soup.find_all('a')
		for i in links:
		    if '.gitignore' in i.attrs['href']:
		        module = i.attrs['href'].replace('blob/','')
		        final_module_url = f'https://raw.githubusercontent.com{module}'
		        all_git_ignore.append(final_module_url)
		with open(f"{HERE}/cache_links.txt", "wb") as pickle_file:
			pickle.dump(all_git_ignore,pickle_file)
		return "done"


def createModuleGitignore(moduleInput):
	callback = _fetchAllModuleData()
	if callback == "cache_links":
		with open(f"{HERE}/cache_links.txt", "rb") as pickle_file:
			all_git_ignore = pickle.load(pickle_file)
	elif callback == "done":
		with open(f"{HERE}/cache_links.txt", "rb") as pickle_file:
			all_git_ignore = pickle.load(pickle_file)

	moduleInput = moduleInput.lower()
	download_module_url = ''
	Flag = False
	for module in all_git_ignore:
	    if moduleInput in module[58:-10].lower():
	    	Flag = True
	    	download_module_url = module
	    	data = requests.get(download_module_url)
	    	data = data.content.decode()
	    	fileName = download_module_url[-10:]
	    	with open(fileName, 'w') as modFile:
	    		modFile.write(data)
	    	break

	if Flag == False:
		print("ERROR: type -h for help")
	else:
		print(f"Sucessfully add .gitignore file for {moduleInput}")

	
