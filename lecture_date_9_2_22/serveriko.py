from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    print(request.method)
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        if age > 50:
            return render_template('not_passed.html')
        else:
            return render_template('passed.html')


if __name__ == '__main__':
    app.run(debug=True)
