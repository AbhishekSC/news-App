from flask import Flask, render_template, request
from flask.helpers import total_seconds
import requests
import newsapi
import requests as r
import json
from win32com.client import Dispatch
import datetime
from itertools import zip_longest


app = Flask(__name__)


def basic_structure(url):
    get_content = r.get(url)
    news = get_content.text
    news_py = json.loads(news)
    # print(type(news_py))
    # print(news_py["totalResults"])
    # print(news_py['articles'])
    arts = news_py['articles']
    # print(type(arts))

    # making list for storing news data
    desc = []
    news = []
    img = []
    urls = []
    dateOfPublication = []
    sources = []
    # taking the main data
    for article in arts:
        sources = article['source']['name']
        news.append(article['title'])
        desc.append(article['description'])
        img.append(article['urlToImage'])
        urls.append(article['url'])
        dateOfPublication.append(article['publishedAt'])
        # print(sources)
        # print(type(article))

    mainInfo = zip_longest(news, desc, img, urls, sources)
    return mainInfo, img, news


def speak(string):
    speak = Dispatch("SAPI.Spvoice")
    speak.speak(string)


def weather_data(city):
    #  Fetching weather data
    city= city 
    print(city)
    if(city == False):
        city= 'indore'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city} &appid=be5002aaef3729a505a257ea843c0428'
    else:
        city= city
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city} &appid=be5002aaef3729a505a257ea843c0428'

    json_data = requests.get(url)
    json_data1 = json_data.text
    data = json.loads(json_data1)

    weatherInfo=[]
    weatherDesc = data['weather'][0]['description']

    humi2 = str(data['main']['humidity'])
    weatherInfo.append(humi2)

    temp10 = data['main']['temp']
    temp = int(temp10 - 273)
    temp = str(temp)
    weatherInfo.append(temp)

    wind_speed_data = str(data['wind']['speed'])
    weatherInfo.append(wind_speed_data)
    weatherInfo.append(weatherDesc)
    return weatherInfo


@app.route('/', methods=['GET', 'POST'])
def general_news():
    city = request.form.get("cityn", False)
    # date and time
    x = datetime.datetime.now()
    dateInfo = x.strftime("%x")

    # api and url
    api = '44a5e5f253804266a74c961b893aa184'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey=44a5e5f253804266a74c961b893aa184 "
    mainInfo, imgs, news = basic_structure(url)
    Total_weather_data= weather_data(city)
   
    # return render_template('index.html', context=mainInfo, dInfo=dateInfo, weather= Total_weather_data)
    return render_template('index.html', context = mainInfo, dInfo=dateInfo, temperature= Total_weather_data[1], humidity= Total_weather_data[0], windS= Total_weather_data[2],  cityN=city, weather_description= Total_weather_data[3], imgs= imgs, news= news)

# Health News Section
@app.route('/health', methods=['GET', 'POST'])
def health_news():
    choices = "health"
    x = datetime.datetime.now()
    dateInfo = x.strftime("%x")

    api = '44a5e5f253804266a74c961b893aa184'
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={choices}&apiKey={api}"
    mainInfo, m, n= basic_structure(url)

    return render_template('health.html', context=mainInfo, dInfo=dateInfo)
    # return render_template('health.html', context = mainInfo, dInfo=dateInfo, temperature= , humidity=humi2, windS=wind_speed_data, detailTemp= weatherDesc, cityN=city)

# Sports News Section
@app.route('/sports', methods=['GET', 'POST'])
def sports_news():
    choices = "sports"
    x = datetime.datetime.now()
    dateInfo = x.strftime("%x")

    api = '44a5e5f253804266a74c961b893aa184'
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={choices}&apiKey={api}"
    mainInfo, m,n = basic_structure(url)

    return render_template('sports.html', context=mainInfo, dInfo=dateInfo)


# Science News Section
@app.route('/science', methods=['GET', 'POST'])
def science_news():
    choices = "science"
    x = datetime.datetime.now()
    dateInfo = x.strftime("%x")

    api = '44a5e5f253804266a74c961b893aa184'
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={choices}&apiKey={api}"
    mainInfo,m,n = basic_structure(url)

    return render_template('science.html', context=mainInfo, dInfo=dateInfo)
    # return render_template('health.html', context = mainInfo, dInfo=dateInfo, temperature=temp, humidity=humi2, windS=wind_speed_data, detailTemp= weatherDesc, cityN=city)

# business News Section
@app.route('/business', methods=['GET', 'POST'])
def business_news():
    choices = "business"
    x = datetime.datetime.now()
    dateInfo = x.strftime("%x")

    # api and url
    api = '44a5e5f253804266a74c961b893aa184'
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={choices}&apiKey={api}"
    mainInfo,m,n = basic_structure(url)

    return render_template('business.html', context=mainInfo, dInfo=dateInfo)
    # return render_template('health.html', context = mainInfo, dInfo=dateInfo, temperature=temp, humidity=humi2, windS=wind_speed_data, detailTemp= weatherDesc, cityN=city)

# Entertainment News Section
@app.route('/entertainment', methods=['GET', 'POST'])
def entertainment_news():
    choices = "entertainment"
    x = datetime.datetime.now()
    dateInfo = x.strftime("%x")

    # api and url
    api = '44a5e5f253804266a74c961b893aa184'
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={choices}&apiKey={api}"
    mainInfo,m,n = basic_structure(url)

    return render_template('entertainment.html', context=mainInfo, dInfo=dateInfo)
    # return render_template('health.html', context = mainInfo, dInfo=dateInfo, temperature=temp, humidity=humi2, windS=wind_speed_data, detailTemp= weatherDesc, cityN=city)

# Technology News Section
@app.route('/technology', methods=['GET', 'POST'])
def technology_news():
    choices = "technology"
    x = datetime.datetime.now()
    dateInfo,m,n = x.strftime("%x")

    # api and url
    api = '44a5e5f253804266a74c961b893aa184'
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={choices}&apiKey={api}"
    mainInfo = basic_structure(url)

    return render_template('technology.html', context=mainInfo, dInfo=dateInfo)
    # return render_template('health.html', context = mainInfo, dInfo=dateInfo, temperature=temp, humidity=humi2, windS=wind_speed_data, detailTemp= weatherDesc, cityN=city)


@app.route('/about')
def about_section():
    return render_template('about.html')


# if __name__=="__main__" :
app.run(debug=True, port=8000)
