import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Load .env file safely
env_path = BASE_DIR / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    load_dotenv()  # fallback (search default locations)

class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        'mysql+pymysql://root:1234@localhost/gamified_app'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Groq API
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_API_URL = os.getenv(
        "GROQ_API_URL",
        "https://api.groq.com/openai/v1/chat/completions"
    )

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

    # Optional: validation (VERY useful 🔥)
    @staticmethod
    def validate():
        if not Config.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing in .env")
        if not Config.OPENAI_API_KEY:
            print("Warning: OPENAI_API_KEY not set (optional)")