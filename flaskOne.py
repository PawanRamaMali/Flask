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


# Jinja Template
@app.route('/watch')
def top_movies():
    movie_list = ['Autopsy of jane doe',
                  'Neon demon',
                  'Ghost in a shell',
                  'Kong: skull island',
                  'John wick 2',
                  'Spiderman - homecoming']

    return render_template('movies.html',
                           movies=movie_list,
                           name='Harry')


# Jinja Template table
@app.route('/tables')
def movies_plus():
    movies_dict = {'Autopsy of jane doe': 02.14,
                   'Neon demon': 3.20,
                   'Ghost in a shell': 1.50,
                   'Kong: skull island': 3.50,
                   'John wick 2': 02.52,
                   'Spiderman - homecoming': 1.48}

    return render_template('table_data.html',
                           movies=movies_dict,
                           name='Sally')


# Jinja Filters
@app.route('/filters')
def filter_data():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('filter_data.html',
                           movies=movies_dict,
                           name=None,
                           film='a christmas carol')


# Jinja MACROS
@app.route('/macros')
def jinja_macros():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('using_macros.html', movies=movies_dict)

if __name__ == '__main__':
    app.run(debug=True)
