from flask import Flask, jsonify, make_response, request, render_template_string
from Scrapping_web import scrapping_page
from utils.parse import list2div

app = Flask('python-flask-seed')


@app.route('/', methods=['GET'])
def index():
    return render_template_string(u'<div align="center"> {cont} </div>'.format(cont=list2div(*scrapping_page())))


@app.route('/<path:path>', methods=['GET', 'POST'])
def not_found(path):
    response = {'error': 'route not found'}
    return make_response(jsonify(response), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
