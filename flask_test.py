from flask import Flask
app =Flask(__name__)
@app.route("/")
def home():
    return '''
    <html>
    <head><title>This is my flask app</title></head>
    <body><h1>Hello from flask</h1>
    <h2>This is added from github</h2></body>
    </html>
    '''
if __name__ == "__main__":
    app.run(debug=True)
