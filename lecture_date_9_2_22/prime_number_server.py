from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    print(request.method)
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        number = request.form['number']
        if not number.isnumeric():
            return render_template('not_a_number.html')
        number = int(number)
        for i in range(2, number):
            if number % i == 0:
                return render_template('not_passed.html')
        return render_template('passed.html')


if __name__ == '__main__':
    app.run(debug=True)
