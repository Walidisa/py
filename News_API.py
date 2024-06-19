from newsapi import NewsApiClient
import requests
def check_internet_connection():
    try:
        response = requests.get('https://www.google.com')
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

if not check_internet_connection():
    print("No internet connection. Please check your network settings.")
    exit()
else:
    newsapi = NewsApiClient(api_key='d7e0d34a808c4b319e68046097287a52')
    topic = input("What would you like to know about?: ")

    headlines = newsapi.get_everything(q=topic, language='en', sort_by='relevancy')
    articles = headlines['articles']

    print("HERE ARE THE HEADLINES!!")

    for x,y in enumerate(articles):
        print(f'{x} {y['title']}')

    num = int(input("Which headline whould you like to know more about?: ")) 

    for key, value in articles[num].items():
        print(f'\n{key.ljust(15)} {value}')
    print("\n")