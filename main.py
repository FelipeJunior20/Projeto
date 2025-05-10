from flask import Flask

app = Flask(__name__)
app.secret_key = '1a2b3c4d5e6f7g8h9i0j'  

from routes import *

if __name__ == "__main__":
    app.run(debug=True)