
import requests

# URL-адреса для получения информации о супергероях
hulk_url = 'https://akabab.github.io/superhero-api/api/id/332.json'
captain_america_url = 'https://akabab.github.io/superhero-api/api/id/149.json'
thanos_url = 'https://akabab.github.io/superhero-api/api/id/655.json'

# Выполняем GET-запросы и получаем информацию о супергероях
hulk_response = requests.get(hulk_url).json()
captain_america_response = requests.get(captain_america_url).json()
thanos_response = requests.get(thanos_url).json()

# Извлекаем значения интеллекта
hulk_intelligence = hulk_response['powerstats']['intelligence']
captain_america_intelligence = captain_america_response['powerstats']['intelligence']
thanos_intelligence = thanos_response['powerstats']['intelligence']

# Сравниваем значения интеллекта и определяем самого умного супергероя
smartest_hero = max(hulk_intelligence, captain_america_intelligence, thanos_intelligence)

# Выводим результат
if smartest_hero == hulk_intelligence:
    print('Самый умный супергерой: Hulk')
elif smartest_hero == captain_america_intelligence:
    print('Самый умный супергерой: Captain America')
else:
    print('Самый умный супергерой: Thanos')
