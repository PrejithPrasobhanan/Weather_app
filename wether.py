from flask import Flask , render_template,request
import requests


app = Flask('weather')

@app.route('/' ,methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('prejith')
        print(data)
        url = f'https://api.openweathermap.org/data/2.5/weather?q={data}&appid=0c1f63f761e0caf78712ec7b00736ec0'
        print(url)
        api_data = requests.get(url)
        python_dict = api_data.json()
        print(python_dict)
        temp = python_dict['main']['temp']
        atm = python_dict['weather'][0]['description']
        hum= python_dict['main']['humidity']
        pres= python_dict['main']['pressure']
        speed= python_dict['wind']['speed']
        cou= python_dict['sys']['country']

        return render_template('index.html',temp = temp,data=data, atm=atm,hum =hum, pres =pres,speed=speed, cou=cou)
    else:
        return render_template('place.html')


app.run(port=8000)