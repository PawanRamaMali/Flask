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


# Add variables in route
@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='Tina'):
    return '<h1> hello there {} </h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
