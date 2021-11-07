from flask import Flask, request, render_template

# Create Flask object of Flask class
app = Flask(__name__)


# Define routes

@app.route('/index')
@app.route('/')
def hello_flask():
    return "hello flask !!"


# Add query parameters
@app.route('/new')
def query_strings(greetings="hello"):
    query_val = request.args.get('greetings', greetings)
    return '<h1> the greeting is : {0} </h1>'.format(query_val)


# Define variables in route
@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='Tina'):
    return '<h1> hello there {} </h1>'.format(name)


# String variables
@app.route('/text/<string:name>')
def text_display(name="hello"):
    return '<h1> the string is {}'.format(name) + '</h1>'


# Number variables
@app.route('/add/<int:num1>/<int:num2>')
def add_two_numbers(num1=0, num2=0):
    return '<h1> the addition of numbers is {}'.format(num1+num2) + '</h1>'


# Float variables
@app.route('/sum/<float:num1>/<float:num2>')
def sum_two_numbers(num1, num2):
    return '<h1> the sum of numbers is {}'.format(num1+num2) + '</h1>'


# Render Template
@app.route('/render')
def show_html_template():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
