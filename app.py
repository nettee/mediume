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
        data = downloader.download_page(link)
        return data


if __name__ == '__main__':
    app.run()