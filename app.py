from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='index')


@app.route('/qrcode')
def qrcode():
    return render_template('qrcode.html', name='qrcode')


def get_sm(m):
    switch = {1: '一月', 2: '二月', 3: '三月', 4: '四月', 5: '五月', 6: '六月',
              7: '七月', 8: '八月', 9: '九月', 10: '十月', 11: '十一月', 12: '十二月'}
    return switch[m]


UA = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


@app.route('/today')
def today():
    now = datetime.datetime.now()
    print(now.month, now.day)
    u = "https://api.avatardata.cn/HistoryToday/LookUp?key=f7b28a4506af42b297a7925bfb0d9b89&yue=" + \
        str(now.month) + "&ri=" + str(now.day) + "&type=1&page=1&rows=40"
    print(u)
    print('going to request')
    response = requests.get(url=u, headers=UA, verify=False)
    todays = response.json()['result']
    print('get!')
    return render_template('today.html', name='today', sm=get_sm(now.month), day=now.day, todays=todays)


@app.route('/relationship')
def relationship():
    return render_template('relationship.html', name='relationship')


@app.route('/rubbish')
def rubbish():
    return render_template('rubbish.html', name='rubbish')


@app.route('/translate')
def translate():
    return render_template('translate.html', name='translate')


@app.route('/random')
def random():
    return render_template('random.html', name='random')


if __name__ == '__main__':

    #app.run(debug=True)
    app.run(host='0.0.0.0',
      port= 5000,
      debug=True)
