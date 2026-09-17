from flask import Flask
import os
app = Flask(__name__)
HTML= "<h1>Loja do Gurue</h1><p><a href='https://wa.me/258860681343'>pefir no WhatsApp</a></p>"
@app.route('/')
def home():
    return HTML
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)