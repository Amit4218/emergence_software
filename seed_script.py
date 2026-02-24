import json

from config.db import SessionLocal
from src.models.project_model import Project


def seed_fake_data():
    db = SessionLocal()

    try:
        if db.query(Project).count() == 0:
            # Load JSON file
            with open("fake_data.json", "r") as f:
                data = json.load(f)
            for item in data:
                project = Project(**item)
                db.add(project)

            db.commit()
            print("Fake data seeded successfully!")
        else:
            print("fake data already seeded")

    except Exception as e:
        db.rollback()
        print("Error seeding data:", e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_fake_data()
