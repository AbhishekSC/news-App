import requests
import newsapi
import requests as r
import json


def mean():
            api='44a5e5f253804266a74c961b893aa184'
            sports='sports'
            # url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey=44a5e5f253804266a74c961b893aa184 "
            url = f"https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={api}"
            
            get_content=r.get(url)
            news = get_content.text
            news_py = json.loads(news)
            # print(type(news_py))
            # print(news_py["totalResults"])
            # print(news_py['articles'])
            arts = news_py['articles']
            print(type(arts))
          
            desc=[]
            news=[]
            img=[]
            urls=[]
            dateOfPublication=[]
            sources=[]
            for article in arts:
                print(article['title'])
                print('\n')
                # sources=article['source']['name']
                # news.append(article['title'])
                # desc.append(article['description'])
                # img.append(article['urlToImage'])
                # urls.append(article['url'])
                # dateOfPublication.append(article['publishedAt'])
                # print(urls)
                # print(type(article))
            # secondaryInfo= zip(sources, urls, dateOfPublication)
            # mainInfo=zip(news, desc, img)
            # for (new,des,img) in myart:
                # print(new)
                # print("======================================================================================\n", des, sourc)
mean()
# def weather_data():
#     #  Fetching weather data
#             city= 'ratlam'
#             print(city)  

#             url=f'http://api.openweathermap.org/data/2.5/weather?q={city} &appid=be5002aaef3729a505a257ea843c0428'
#             json_data=requests.get(url)
#             json_data1=json_data.text
#             data=json.loads(json_data1)
#             print(data)

#             weatherDesc= data['weather'][0]['description']
#             print(weatherDesc)
#             humi2= str(data['main']['humidity'])

#             temp10= data['main']['temp']
#             temp= int(temp10 - 273)
#             temp= str(temp)

#             wind_speed_data= str(data['wind']['speed'])
#             print(temp, humi2, wind_speed_data)
#             weatherInfo= zip(humi2, wind_speed_data, temp, )

# weather_data()
                
                
                      
            
           

