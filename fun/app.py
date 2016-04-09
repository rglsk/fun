from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from task501 import search_engines
from task501 import relevant
from shared import settings
from shared.models import RelevantData


def create_app():
    app = Flask(__name__)
    app.secret_key = settings.SECRET_KEY
    app.debug = settings.DEBUG
    app.static_folder = './static'
    return app

app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task501', methods=['GET', 'POST'])
def task501():
    template_values = {'task501': 'active'}

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
        results['duckduckgo_result'] = search_engines.duckduckgo_search(query)

        template_values['results'] = results

        return render_template('task501/index.html', **template_values)


@app.route('/relevant', methods=['POST'])
def relevant_results():
    google_relevant = bool(request.form.get('google_relevant'))
    bing_relevant = bool(request.form.get('bing_relevant'))
    duckduckgo_relevant = bool(request.form.get('duckduckgo_relevant'))
    data = {'google_relevant': google_relevant,
            'bing_relevant': bing_relevant,
            'duckduckgo_relevant': duckduckgo_relevant}

    relevant.save_relevant_data(data)

    return redirect('/task501')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000)
