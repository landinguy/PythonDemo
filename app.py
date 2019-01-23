from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name')
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
