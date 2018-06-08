from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

posts = [
    {
        'author': 'Jame Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Corey Steve',
        'title': 'Blog Post 1',
        'content': 'virtualenvwrapper is a set of extensions to Ian Bicking’s ',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Abdul Aziz Bah',
        'title': 'Blog Post 1',
        'content': 'Organizes all of your virtual environments in one place',
        'date_posted': 'May 21, 2018'
    }
]


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/home')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)