from app import app, db, User
from werkzeug.security import generate_password_hash

# Manually push an application context
with app.app_context():
    db.create_all()

    # Replace 'admin' and 'admin_password' with desired credentials
    admin = User(username='admin', password=generate_password_hash('admin_password', method='pbkdf2:sha256'))

    db.session.add(admin)
    db.session.commit()

print("Database setup completed!")
