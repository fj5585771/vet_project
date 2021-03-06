from flask import Flask, render_template
from controllers.animals_controller import animals_blueprint
from controllers.customers_controller import customers_blueprint

app = Flask(__name__)
app.secret_key = "super secret key"

app.register_blueprint(animals_blueprint)
app.register_blueprint(customers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
