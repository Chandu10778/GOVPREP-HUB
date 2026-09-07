"""
Clear old materials and seed comprehensive data
"""

from app import app
from models import db, Material, MaterialProgress

def clear_and_seed():
    """Clear old materials and seed comprehensive ones"""
    with app.app_context():
        try:
            # Clear old data
            MaterialProgress.query.delete()
            Material.query.delete()
            db.session.commit()
            print("Cleared old materials and progress data")

            # Import comprehensive materials
            from seed_comprehensive_materials_v2 import COMPREHENSIVE_MATERIALS

            # Add new materials
            for data in COMPREHENSIVE_MATERIALS:
                material = Material(
                    title=data['title'],
                    subject=data['subject'],
                    level=data['level'],
                    content=data['content'],
                    xp_reward=data['xp_reward']
                )
                db.session.add(material)

            db.session.commit()
            print(f"Successfully seeded {len(COMPREHENSIVE_MATERIALS)} comprehensive materials!")
            print(f"Breakdown by subject:")

            for subject in set([m['subject'] for m in COMPREHENSIVE_MATERIALS]):
                materials = [m for m in COMPREHENSIVE_MATERIALS if m['subject'] == subject]
                count = len(materials)
                total_xp = sum([m['xp_reward'] for m in materials])
                print(f"   {subject}: {count} materials | {total_xp} XP")

            total_xp = sum([m['xp_reward'] for m in COMPREHENSIVE_MATERIALS])
            print(f"\n💰 Total XP Available: {total_xp} XP")

        except Exception as e:
            db.session.rollback()
            print(f"Error: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    clear_and_seed()
