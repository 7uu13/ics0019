import csv
from app.models import Kohvikud
from app.utils import existing_cafe, create_cafe
from app.database import Session

s = Session()

def load_cafes_from_csv(csv_filename: str):
    try:
        with open(csv_filename, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                name, location, operator, time_open, time_close = row
                if not existing_cafe(name, location):
                    create_cafe(row)
            s.commit()
    except Exception as e:
        print(f"Error: {e}")
        s.rollback()
    finally:
        for restaurant in s.query(Kohvikud).all():
            print(f"ID: {restaurant.id}, Name: {restaurant.name}, Operator: {restaurant.operator}, "
                  f"Location: {restaurant.location}, Hours: {restaurant.time_open} - {restaurant.time_close}")
        s.close()
