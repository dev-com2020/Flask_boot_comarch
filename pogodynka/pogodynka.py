import json
import urllib

from flask import Flask, render_template, request, abort, Response

app = Flask(__name__)


@app.route('/pogoda', methods=['GET'])
def pogoda():
    city = request.args.get('city')
    if city is None:
        abort(400, 'Brak miasta')
        data = {}
        data['q'] = request.args.get('city')
        data['appid'] = '114f96ab7fa79786add85b6f90b65ae7'
        data['units'] = 'metric'
        data['lang'] = 'pl'
        url_values = urllib.parse.urlencode(data)
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        full_url = url + '?' + url_values
        data = urllib.request.urlopen(full_url)
        resp = Response(data)
        resp.status_code = 200
    return render_template('index.html', title='Pogoda', data=json.loads(data.read().decode('utf-8')))
