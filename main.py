
from flask import request
from location import semarang,salatiga,surakarta,magelang,pekalongan,tegal 
#locations taro di sebelah biar ga berantakan

from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
@app.route("/home", methods=['POST', 'GET']) #homepage, open index
def index():
   return render_template('index.html',)

#kalau metodenya POST dan di form kota inputnya value=smg, output func semarang()
 #no case-switch di python 3.8, berantakan >:(
@app.route("/result", methods=['GET','POST'])
def result():
  if request.method=='POST': 
    if request.form.get('kota')=="smg":
      return semarang()

    elif request.form.get('kota')=="slt":
      return salatiga()

    elif request.form.get('kota')=="srk":
      return surakarta()

    elif request.form.get('kota')=="mgl":
      return magelang()

    elif request.form.get('kota')=="pkl":
      return pekalongan()

    elif request.form.get('kota')=="tgl":
      return tegal()
      
    else: return ("<h1>404! debugging yang bagus maba sekarang kembali begadang</h1>")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000) #webserver

  #code from: https://www.edureka.co/blog/web-scraping-with-python/ and stackoverflow
  #https://www.w3schools.com/tags/tag_select.asp
  #https://www.w3schools.com/tags/att_option_value.asp
  #https://www.reddit.com/r/flask/comments/2fug7o/af_getting_selected_value_from_dropdown_list/ckcx9im/
  #https://stackoverflow.com/questions/16867898/what-does-mean-in-html
  #https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
  #https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/