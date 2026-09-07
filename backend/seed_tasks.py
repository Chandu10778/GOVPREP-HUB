from app import app, db
from models import Task

def seed_tasks():
    with app.app_context():
        Task.query.delete()
        db.session.commit()

        tasks_data = [
            {"title": "Polity: Understand Constitution and Rights", "subject": "Polity", "description": "Study the Preamble, Fundamental Rights, DPSP, and basic structure doctrine.", "stage": 1, "xp": 20},
            {"title": "History: Ancient India Review", "subject": "History", "description": "Cover Indus Civilization, Maurya and Gupta empires, and key cultural developments.", "stage": 1, "xp": 20},
            {"title": "Geography: Basics of Physical Geography", "subject": "Geography", "description": "Learn about atmosphere, hydrosphere, lithosphere and major maps.", "stage": 1, "xp": 20},
            {"title": "Current Affairs: Month Review", "subject": "Current Affairs", "description": "Summarize top 20 national and international news events.", "stage": 1, "xp": 20},
            {"title": "Quantitative Aptitude: Ratio & Proportion Drills", "subject": "Quantitative Aptitude", "description": "Practice 25 questions on ratios, percentages and speed-distance.", "stage": 1, "xp": 20},
            {"title": "Polity: Federalism and Centre-State Relations", "subject": "Polity", "description": "Deep dive into division of powers, inter-state council, and dispute resolution.", "stage": 2, "xp": 30},
            {"title": "History: Medieval Indian Polity", "subject": "History", "description": "Learn about Delhi Sultanate, Mughals, and policies.", "stage": 2, "xp": 30},
            {"title": "Geography: Indian Monsoon & Climate", "subject": "Geography", "description": "Analyze monsoon patterns, cyclones, and climate change impact.", "stage": 2, "xp": 30},
            {"title": "Current Affairs: Economy & Schemes", "subject": "Current Affairs", "description": "Study major government schemes and economic policy updates.", "stage": 2, "xp": 30},
            {"title": "Quantitative Aptitude: Time & Work Advanced", "subject": "Quantitative Aptitude", "description": "Solve 20 questions on pipes, men, efficiency and time improvement.", "stage": 2, "xp": 30},
            {"title": "Polity: Judiciary and Civil Services", "subject": "Polity", "description": "Learn role of Supreme Court, high courts and appointment procedures.", "stage": 3, "xp": 40},
            {"title": "History: Modern Freedom Struggle", "subject": "History", "description": "Focus on 1857, Gandhi-era movement, India’s independence pipeline.", "stage": 3, "xp": 40},
            {"title": "Geography: Economic Geography", "subject": "Geography", "description": "Understand resources, agriculture, and regional development.", "stage": 3, "xp": 40},
            {"title": "Current Affairs: International Relations", "subject": "Current Affairs", "description": "Decimals 5 current global treaties and geopolitical flashpoints.", "stage": 3, "xp": 40},
            {"title": "Quantitative Aptitude: Data Interpretation", "subject": "Quantitative Aptitude", "description": "Practice advanced graphs, tables, and caselet problems.", "stage": 3, "xp": 40},
            {"title": "Polity: Revision & PYQ Polity", "subject": "Polity", "description": "Solve previous year polity MCQs and consolidate key facts.", "stage": 5, "xp": 50},
            {"title": "History: Revision & PYQ History", "subject": "History", "description": "Solve previous year history MCQs and recall timelines.", "stage": 5, "xp": 50},
        ]

        for task_data in tasks_data:
            task = Task(
                title=task_data["title"],
                subject=task_data["subject"],
                description=task_data["description"],
                stage=task_data["stage"],
                xp=task_data["xp"]
            )
            db.session.add(task)

        db.session.commit()
        print(f"Seeded {len(tasks_data)} exam-oriented tasks successfully!")

if __name__ == "__main__":
    seed_tasks()