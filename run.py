from app import app, db
from app.models import User

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0')