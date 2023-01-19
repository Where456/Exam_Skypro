import logging

from flask import request, jsonify

from flask import Flask, render_template

from utils import get_data_all, search_station, today, get_data_by_pk

app = Flask(__name__)


logging.basicConfig(filename='logs/api.log', level=logging.INFO, filemode="w",
                    format='%(asctime)s [%(levelname)s] %(message)s')


@app.route("/")
def main_page():
    logging.info('Главная страница запрошена')
    text = get_data_all()
    return render_template('index.html', text=text)


@app.route("/search/")
def page_search():
    logging.info('Запрос поиска')
    w = request.args.get('s')
    word = search_station(w)
    return render_template('search.html', word=word)


@app.route("/today/")
def page_timetable():
    logging.info('Запрос поиска')
    data = today()
    return render_template('today.html', data=data)


@app.errorhandler(404)
def not_found_error(e):
    return 'Сервер не найден'


@app.errorhandler(500)
def internal_error(e):
    return 'Внутренняя ошибка сервера'


@app.route("/api/alldata/")
@app.route("/api/alldata")
def api_posts():
    data = get_data_all()
    return jsonify(data)


@app.route("/api/data/<int:pk>/")
@app.route("/api/data/<int:pk>")
def api_post(pk):
    data = get_data_by_pk(pk)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
