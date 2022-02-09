from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1, num2):
    return 'Outcome is :{}'.format(num1 + num2)


# This add a routing for the path 'bla'
@app.route('/bla')
def func():
    # return render_template('tryout.html')
    with open('tryout.html', 'r') as f:
        text = f.read()
        return text


@app.route('/get_random')
def generate_random_number():
    number = random.randint(1, 10)
    return str(number)

if __name__ == '__main__':
    app.run(debug=True)
