from flask import Flask
from flask_cors import CORS
from config import Config
from models import db

# Import routes
from routes.auth import auth
from routes.tasks import tasks
from routes.user import user
from routes.materials import materials
from routes.chat import chat

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)

# Register routes
app.register_blueprint(auth)
app.register_blueprint(tasks)
app.register_blueprint(user)
app.register_blueprint(materials)
app.register_blueprint(chat)

# Validate config on startup
try:
    Config.validate()
    print("✅ Config validated - Groq API key ready!")
except ValueError as e:
    print(f"❌ Config error: {e}")

# Create tables and ensure schema updates for existing DBs
with app.app_context():
    db.create_all()

    # Migrate older user table schema if missing fields
    from sqlalchemy import inspect, text
    inspector = inspect(db.engine)

    if inspector.has_table('user'):
        columns = [c['name'] for c in inspector.get_columns('user')]
        if 'streak' not in columns:
            with db.engine.begin() as conn:
                conn.execute(text('ALTER TABLE user ADD COLUMN streak INTEGER DEFAULT 0'))

    if inspector.has_table('task'):
        columns = [c['name'] for c in inspector.get_columns('task')]
        if 'subject' not in columns:
            with db.engine.begin() as conn:
                conn.execute(text("ALTER TABLE task ADD COLUMN subject VARCHAR(100) DEFAULT 'General'"))
        if 'description' not in columns:
            with db.engine.begin() as conn:
                conn.execute(text("ALTER TABLE task ADD COLUMN description TEXT"))
        if 'stage' not in columns:
            with db.engine.begin() as conn:
                conn.execute(text("ALTER TABLE task ADD COLUMN stage INTEGER DEFAULT 1"))

    # Create missing tables
    db.create_all()

@app.route('/')
def home():
    return "Backend Running 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)