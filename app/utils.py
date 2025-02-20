from app.database import Session
from app.models import Kohvikud

s = Session()

def existing_cafe(name, location: str) -> bool:
    cafe = s.query(Kohvikud).filter(
            Kohvikud.name == name,
            Kohvikud.location == location,
    ).first()
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
    s.add(cafe)
