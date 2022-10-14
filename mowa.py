import requests

city = input('input the city name: ')
print("You have entered",city)

# city = 'Nellore'

print('Displaying Weater report for: ' + city)

#fetch the weater details
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#display the result
print(res.text)