from flask import *

from mediume.downloader import Downloader

app = Flask(__name__)

downloader = Downloader()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/view', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        link = request.form['link']
        return redirect(url_for('view', link=link))
    else:
        link = request.args.get('link')
        file_path = 'page.html'

        def on_progress(*args, **kwargs):
            pass

        downloader.download_page(link, file_path, on_progress)

        with open('page.html', 'r') as f:
            data = f.read()
        return data


if __name__ == '__main__':
    app.run()