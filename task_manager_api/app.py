from flask import Flask
from config import Config
from database import db
from routes import load_bp
from flask import render_template

app = Flask(__name__)
app.config.from_object(Config)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/docs')
def api_docs():
    return render_template('api_docs.html')  # Assuming your API docs HTML is named 'api_docs.html'

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(load_bp)

if __name__ == '__main__':
    app.run(debug=True)
