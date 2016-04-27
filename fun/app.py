from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from task501 import search_engines
from task501.relevant import count_relevant_data
from shared import settings
from shared import models
from shared.settings import SQLALCHEMY_DATABASE_URI


def create_app():
    app = Flask(__name__)
    app.secret_key = settings.SECRET_KEY
    print SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.debug = settings.DEBUG
    app.static_folder = './static'

    models.db.init_app(app)
    with app.app_context():
        models.db.create_all()

    return app

app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task501', methods=['GET', 'POST'])
def task501():
    template_values = {'task501': 'active'}
    MAP = count_relevant_data()
    template_values['map_results'] = MAP

    if request.method == 'GET':
        return render_template('task501/index.html', **template_values)

    if request.method == 'POST':
        query = request.form.get('search_query')
        if not query:
            template_values['error'] = 'Query required.'
            return render_template('task501/index.html', **template_values)

        results = {}
        results['google_result'] = search_engines.google_search(query)
        results['bing_result'] = search_engines.bing_search(query)
        results['duckduckgo_result'] = search_engines.duckduckgo_search(
            query)
        print results
        template_values['results'] = results

        return render_template('task501/index.html', **template_values)


@app.route('/relevant', methods=['POST', 'DELETE'])
def relevant_results():
    if request.method == 'POST':
        google_relevant = []
        bing_relevant = []
        duckduckgo_relevant = []
        for nr in xrange(10):
            google_relevant.append(
                bool(request.form.get('google_result{}'.format(str(nr)))))
            bing_relevant.append(
                bool(request.form.get('bing_result{}'.format(str(nr)))))
            duckduckgo_relevant.append(bool(
                request.form.get('duckduckgo_result{}'.format(str(nr)))))
        data = {'google_relevant': google_relevant,
                'bing_relevant': bing_relevant,
                'duckduckgo_relevant': duckduckgo_relevant}

        for name, value in data.iteritems():
            for result in value:
                models.RelevantData(name=name, is_relevant=result).save()

        return redirect('/task501')
    if request.method == 'DELETE':
        with app.app_context():
            all_data = models.RelevantData.query.all()
            for relev in all_data:
                relev.delete()
        return ''


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)
