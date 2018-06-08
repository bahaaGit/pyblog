from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Helylo World!"


print("hello");
if __name__ == '__main__':
    app.run(debug=True)