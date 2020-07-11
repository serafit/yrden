import requests

def get_proxy (url: str) -> str:
	
    a = requests.get(url)
    filename = "proxies.txt"

    file = open(filename, 'w+')
    file.write(a.text) 
    file.close()

    return filename