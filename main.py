#scraper weather.com
import requests #yang request html dari weather.com
from bs4 import BeautifulSoup #HTML parser
#cari website yang bisa menyediakan weather dengan api koordinat / berdasarkan lokasi
from flask import Flask, render_template #webserver
app = Flask(__name__)
#use selenium untuk akses geolocation dan pake geolocation sbg arg di URL?
#make button in webserver to select location  then ^
#case() untuk tiap daerah? jadi loc_element=weather_element find h1, class=${id for x location};
#jadi if(lokasi a) then loc_class = currentconditions_xyz if lokasi b then loc_class=current_conditions abc
#store lokasi di file lain lalu diimport biar rapih
#magelang pekalongan salatiga semarang surakarta tegal
#or define function define weatherPage()=case(lokasi){isinya for weather_element in weather_elements tapi classnya manut lokasi} jadi def index tinggal call fungsi weatherPage() yang narik data dari dropdown sheet?

@app.route('/') #route ke root directory, ga ada folder, arg ganti nama folder kalo mau ada page lebihan
def index():
  URL = "https://weather.com/weather/today/l/28dfc69115e33e603464457ad11d35817a99877d214db3ffd8381cb1fb8b18c4"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find(id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034")
  weather_elements = results.find_all("div",class_="CurrentConditions--CurrentConditions--1swR9")
  #cari asset yang match [awalan][currentconditions dkk]

  for weather_element in weather_elements:
    loc_element = weather_element.find("h1", class_="CurrentConditions--location--kyTeL")
    time_element = weather_element.find("div", class_="CurrentConditions--timestamp--23dfw")
    temp_element = weather_element.find("span", class_="CurrentConditions--tempValue--3a50n")
    tempDesc_element = weather_element.find("div", class_="CurrentConditions--phraseValue--2Z18W")
    rainChance_element = weather_element.find("div", class_="CurrentConditions--precipValue--3nxCj")

  return(
  '<h2 style="text-align:center;">' + loc_element.text +'</h2>' + '<br>'
  + '<h1 style="font-family:Arial;text-align:center;">' + temp_element.text + " F" + '</h1>' #cari stringreplace; derajat jadi kosong/petik; angka polosan diconvert ke int; integer parse; rumus
  + '<br>'
  + '<p style="font-family:Arial;text-align:center;>'+ tempDesc_element.text + '</p>'
  + '<br>'
  + '<p style="font-family:Arial;text-align:center;">' + time_element.text + '</p>'
  + '<br>'
  + '<p style="font-family:Arial;text-align:center;">' + rainChance_element.text + '</p>')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000) #webserver

  #code from: https://www.edureka.co/blog/web-scraping-with-python/ and stackoverflow
