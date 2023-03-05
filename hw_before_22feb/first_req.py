import requests

trial_adres = "https://www.python.org/"

full_page = requests.get(trial_adres)
print(full_page.headers)
