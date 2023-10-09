from app import app, db, User
from werkzeug.security import generate_password_hash

# List of users to be added to the database
users_to_add = [
    {"username": "admin", "password": "admin_password"},
    {"username": "user1", "password": "user1_password"},
    {"username": "user2", "password": "user2_password"},
    {"username": "user3", "password": "user3_password"},
]

# Create an application context
with app.app_context():
    # Create the database and table
    db.create_all()
    
    # Add user instances to the session
    for user_info in users_to_add:
        # Check if user already exists
        existing_user = User.query.filter_by(username=user_info["username"]).first()
        
        if existing_user is None:
            new_user = User(
                username=user_info["username"],
                password=generate_password_hash(user_info["password"], method='pbkdf2:sha256')
            )
            db.session.add(new_user)
        else:
            print(f"User {user_info['username']} already exists. Skipping...")

    # Commit the session to the database
    print('Database setup and populated.')
    db.session.commit()
