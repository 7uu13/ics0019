from models import Kohvikud
from config import db
import csv

def existing_cafe(name, location: str) -> bool:
    cafe = Kohvikud.query.filter_by(name=name, location=location).first()
    return cafe is not None

def create_cafe(cafe_info: list) -> None:
    name, location, operator, time_open, time_close = cafe_info
    cafe = Kohvikud(
        name=name,
        location=location,
        operator=operator,
        time_open=time_open,
        time_close=time_close
    )
    db.session.add(cafe)

def load_cafes_from_csv(csv_filename: str):
    try:
        with open(csv_filename, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                name, location, operator, time_open, time_close = row
                print(row)
                if not existing_cafe(name, location):
                    create_cafe(row)
                    db.session.commit()
    except Exception as e:
        print(f"Error: {e}")
        db.session.rollback()
    finally:
        for restaurant in Kohvikud.query.all():
            print(f"ID: {restaurant.id}, Name: {restaurant.name}, Operator: {restaurant.operator}, "
                  f"Location: {restaurant.location}, Hours: {restaurant.time_open} - {restaurant.time_close}")
        db.session.close()
