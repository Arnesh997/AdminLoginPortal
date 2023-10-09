from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_BINDS'] = {
    'users': 'sqlite:///users.db',
    'products': 'sqlite:///products.db'
}

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Product(db.Model):
    __bind_key__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        new_product = Product(name=name, description=description)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('dashboard'))

    products = Product.query.all()
    return render_template('dashboard.html', products=products)

# [include other routes...]

if __name__ == "__main__":
    app.run(debug=True)
