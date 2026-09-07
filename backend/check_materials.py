import sys
sys.path.append(r'c:\Users\chand\OneDrive\Desktop\project\backend')
from app import app
from models import Material

with app.app_context():
    total_count = Material.query.count()
    print(f"Total materials in database: {total_count}")

    subjects = ['Polity', 'History', 'Geography', 'Current Affairs', 'Quantitative Aptitude']
    for subject in subjects:
        count = Material.query.filter_by(subject=subject).count()
        print(f"{subject}: {count} materials")