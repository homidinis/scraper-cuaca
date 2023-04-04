
import requests 
from bs4 import BeautifulSoup 
def semarang():
    URL = "https://weather.com/weather/today/l/28dfc69115e33e603464457ad11d35817a99877d214db3ffd8381cb1fb8b18c4"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034")
    weather_elements = results.find_all("div",class_="CurrentConditions--CurrentConditions--1swR9")
    
  
    for weather_element in weather_elements:
      loc_element = weather_element.find("h1", class_="CurrentConditions--location--kyTeL")
      time_element = weather_element.find("div", class_="CurrentConditions--timestamp--23dfw")
      temp_element = weather_element.find("span", class_="CurrentConditions--tempValue--3a50n") 
      tempDesc_element = weather_element.find("div", class_="CurrentConditions--phraseValue--2Z18W")
      precip_element = weather_element.find("div", class_="CurrentConditions--precipValue--3nxCj")
     
      return('<h2 style="text-align:center;">' + loc_element.text +'</h2>' + '<br>' 
     + '<h1 style="font-family:Arial;text-align:center;">' + temp_element.text + " F" + '</h1>' 
     + '<br>'
     + '<b>''<p style="font-family:Arial;text-align:center;">'+ tempDesc_element.text + '</p>''</b>'
     + '<br>'
     + '<p style="font-family:Arial;text-align:center;">' + precip_element.text + '</p>'
     + '<br>' 
     + '<p style="font-family:Arial;text-align:center;">' + time_element.text + '</p>'
     + '<br>'+'<br>'+
     '<a href="https://wscraper.homidinis.repl.co/" style="font-family:Arial;text-align:center;">Back</a>')
# TODO: error string replace: "can only concatenate str (not int) to str" for some reasons

def salatiga():
    URL = "https://weather.com/weather/today/l/8e88dca69853f2b6741ba295130ac14eecead836cb8e44b31bfa23bccb2caca5"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034")
    weather_elements = results.find_all("div",class_="CurrentConditions--CurrentConditions--1swR9")
    
    for weather_element in weather_elements:
      loc_element = weather_element.find("h1", class_="CurrentConditions--location--kyTeL")
      time_element = weather_element.find("div", class_="CurrentConditions--timestamp--23dfw")
      temp_element = weather_element.find("span", class_="CurrentConditions--tempValue--3a50n") 
      tempDesc_element = weather_element.find("div", class_="CurrentConditions--phraseValue--2Z18W")
      precip_element = weather_element.find("div", class_="CurrentConditions--precipValue--3nxCj")
      
     
      return('<h2 style="text-align:center;">' + loc_element.text +'</h2>' + '<br>' 
     + '<h1 style="font-family:Arial;text-align:center;">' + temp_element.text + " F" + '</h1>' 
     + '<br>'
     + '<b>''<p style="font-family:Arial;text-align:center;">'+ tempDesc_element.text + '</p>''</b>'
     + '<br>'
     + '<p style="font-family:Arial;text-align:center;">' + precip_element.text + '</p>'
     + '<br>' 
     + '<p style="font-family:Arial;text-align:center;">' + time_element.text + '</p>'
     + '<br>'+'<br>'+
     '<a href="https://wscraper.homidinis.repl.co/" style="font-family:Arial;text-align:center;">Back</a>')

def surakarta():
    URL = "https://weather.com/weather/today/l/5fe5cdcaa0e1f2ad3f1cd2acd41babbb553576d230dec69ac8a1149009934c84"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034")
    weather_elements = results.find_all("div",class_="CurrentConditions--CurrentConditions--1swR9")
    
    
    for weather_element in weather_elements:
      loc_element = weather_element.find("h1", class_="CurrentConditions--location--kyTeL")
      time_element = weather_element.find("div", class_="CurrentConditions--timestamp--23dfw")
      temp_element = weather_element.find("span", class_="CurrentConditions--tempValue--3a50n") 
      tempDesc_element = weather_element.find("div", class_="CurrentConditions--phraseValue--2Z18W")
      precip_element = weather_element.find("div", class_="CurrentConditions--precipValue--3nxCj")
     
      return('<h2 style="text-align:center;">' + loc_element.text +'</h2>' + '<br>' 
      + '<h1 style="font-family:Arial;text-align:center;">' + temp_element.text + " F" + '</h1>'
      + '<br>'
      + '<b>''<p style="font-family:Arial;text-align:center;">'+ tempDesc_element.text + '</p>''</b>'
      + '<br>'
      + '<p style="font-family:Arial;text-align:center;">' + precip_element.text + '</p>'
      + '<br>' 
      + '<p style="font-family:Arial;text-align:center;">' + time_element.text + '</p>'
      + '<br>'+'<br>'+
     '<a href="https://wscraper.homidinis.repl.co/" style="font-family:Arial;text-align:center;">Back</a>')

def magelang():
    URL = "https://weather.com/weather/today/l/65edceb1f3cf0b42f48fee1f9977571a1d9c0993024362b3d5c3d29ead26b563"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034")
    weather_elements = results.find_all("div",class_="CurrentConditions--CurrentConditions--1swR9")
    
    for weather_element in weather_elements:
      loc_element = weather_element.find("h1", class_="CurrentConditions--location--kyTeL")
      time_element = weather_element.find("div", class_="CurrentConditions--timestamp--23dfw")
      temp_element = weather_element.find("span", class_="CurrentConditions--tempValue--3a50n") 
      tempDesc_element = weather_element.find("div", class_="CurrentConditions--phraseValue--2Z18W")
      precip_element = weather_element.find("div", class_="CurrentConditions--precipValue--3nxCj")
     
      return('<h2 style="text-align:center;">' + loc_element.text +'</h2>' + '<br>' 
     + '<h1 style="font-family:Arial;text-align:center;">' + temp_element.text + " F" + '</h1>' 
     + '<br>'
     + '<b>''<p style="font-family:Arial;text-align:center;">'+ tempDesc_element.text + '</p>''</b>'
     + '<br>'
     + '<p style="font-family:Arial;text-align:center;">' + precip_element.text + '</p>'
     + '<br>' 
     + '<p style="font-family:Arial;text-align:center;">' + time_element.text + '</p>'
     + '<br>'+'<br>'+
     '<a href="https://wscraper.homidinis.repl.co/" style="font-family:Arial;text-align:center;">Back</a>')

def pekalongan():
    URL = "https://weather.com/weather/today/l/3d1f18efb123fe0647f9864b6b190e892679049c71284dd2ed4d3d7384f1ad72"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034")
    weather_elements = results.find_all("div",class_="CurrentConditions--CurrentConditions--1swR9")
    
    for weather_element in weather_elements:
      loc_element = weather_element.find("h1", class_="CurrentConditions--location--kyTeL")
      time_element = weather_element.find("div", class_="CurrentConditions--timestamp--23dfw")
      temp_element = weather_element.find("span", class_="CurrentConditions--tempValue--3a50n") 
      tempDesc_element = weather_element.find("div", class_="CurrentConditions--phraseValue--2Z18W")
      precip_element = weather_element.find("div", class_="CurrentConditions--precipValue--3nxCj")
     
      return('<h2 style="text-align:center;">' + loc_element.text +'</h2>' + '<br>' 
     + '<h1 style="font-family:Arial;text-align:center;">' + temp_element.text + " F" + '</h1>' 
     + '<br>'
     + '<b>''<p style="font-family:Arial;text-align:center;">'+ tempDesc_element.text + '</p>''</b>'
     + '<br>'
     + '<p style="font-family:Arial;text-align:center;">' + precip_element.text + '</p>'
     + '<br>' 
     + '<p style="font-family:Arial;text-align:center;">' + time_element.text + '</p>'
     + '<br>'+'<br>'+
     '<a href="https://wscraper.homidinis.repl.co/" style="font-family:Arial;text-align:center;">Back</a>')

def tegal():
    URL = "https://weather.com/weather/today/l/6fdcf922e65d983cbe18ff432cda99dac1a7b7b6d51befb801011e55b2e20296"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034")
    weather_elements = results.find_all("div",class_="CurrentConditions--CurrentConditions--1swR9")

    
    for weather_element in weather_elements:
      loc_element = weather_element.find("h1", class_="CurrentConditions--location--kyTeL")
      time_element = weather_element.find("div", class_="CurrentConditions--timestamp--23dfw")
      temp_element = weather_element.find("span", class_="CurrentConditions--tempValue--3a50n") 
      tempDesc_element = weather_element.find("div", class_="CurrentConditions--phraseValue--2Z18W")
      precip_element = weather_element.find("div", class_="CurrentConditions--precipValue--3nxCj")
      
      return('<h2 style="text-align:center;">' + loc_element.text +'</h2>' + '<br>' 
     + '<h1 style="font-family:Arial;text-align:center;">' + temp_element.text + " F" + '</h1>'
     + '<br>'
     + '<b>''<p style="font-family:Arial;text-align:center;">'+ tempDesc_element.text + '</p>''</b>'
     + '<br>'
     + '<p style="font-family:Arial;text-align:center;">' + precip_element.text + '</p>'
     + '<br>' 
     + '<p style="font-family:Arial;text-align:center;">' + time_element.text + '</p>'
     + '<br>'+'<br>'+
     '<a href="https://wscraper.homidinis.repl.co/" style="font-family:Arial;text-align:center;">Back</a>')


  