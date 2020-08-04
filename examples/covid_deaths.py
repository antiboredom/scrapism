import requests

response = requests.get("https://feeds-elections.foxnews.com/covid/covid.json")

data = response.json()

us_deaths_total = data[1]["DeathsToday"]
us_deaths_today = data[1]["DeathsChange"]

print("Total US Deaths: {}".format(us_deaths_total))
print("Total US Deaths Today: {}".format(us_deaths_today))

