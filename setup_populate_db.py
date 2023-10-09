from app import db, app, User, Product
from werkzeug.security import generate_password_hash

def setup_users_db():
    with app.app_context():
        engine = db.engines['users']
        db.metadata.create_all(engine)
        
        user = User(username='admin', password=generate_password_hash('adminpassword', method='pbkdf2:sha256'))
        
        existing_user = User.query.filter_by(username=user.username).first()
        if not existing_user:
            db.session.add(user)
            db.session.commit()
            print('User added: ', user.username)
        else:
            print('User already exists: ', user.username)

def setup_products_db():
    with app.app_context():
        engine = db.get_engine(app, bind='products')
        db.metadata.create_all(engine)
        
        product = Product(name='Example Product', description='This is an example product.')
        
        existing_product = Product.query.filter_by(name=product.name).first()
        if not existing_product:
            db.session.add(product)
            db.session.commit()
            print('Product added: ', product.name)
        else:
            print('Product already exists: ', product.name)

if __name__ == "__main__":
    setup_users_db()
    setup_products_db()
