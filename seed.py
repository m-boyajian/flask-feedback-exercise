from models import User, Feedback, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

User.query.delete()

Feedback.query.delete()