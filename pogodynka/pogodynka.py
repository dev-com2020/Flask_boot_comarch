import json
import urllib.parse
import urllib.request

from flask import Flask, render_template, request, abort, Response

# app = Flask(__name__)


# @app.route('/pogoda', methods=['GET'])
# def pogoda():
#     global data
#     city = request.args.get('city')
#     if city is None:
#         abort(400, 'Brak miasta')
#     data = {'q': request.args.get('city'), 'appid': '114f96ab7fa79786add85b6f90b65ae7', 'units': 'metric',
#                 'lang': 'pl'}
#     url_values = urllib.parse.urlencode(data)
#     url = 'http://api.openweathermap.org/data/2.5/forecast'
#     full_url = url + '?' + url_values
#     data = urllib.request.urlopen(full_url)
#     resp = Response(data)
#     resp.status_code = 200
#     return render_template('index2.html', title='Pogoda', data=json.loads(data.read().decode('utf-8')))
#
# # if __name__ == '__main__':
# #     app.run(debug=True)