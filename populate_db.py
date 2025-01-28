from models import Automobilis, db
from app import app


with app.app_context():
    # db.create_all()
    duomenys = [
        {'gamintojas': 'Toyota', 'modelis': 'Corolla', 'spalva': 'Balta', 'metai': 2020, 'kaina': 15000},
        {'gamintojas': 'Volkswagen', 'modelis': 'Golf', 'spalva': 'Juoda', 'metai': 2019, 'kaina': 12000},
        {'gamintojas': 'BMW', 'modelis': 'X5', 'spalva': 'Sidabrinė', 'metai': 2022, 'kaina': 45000},
        {'gamintojas': 'Audi', 'modelis': 'Q7', 'spalva': 'Raudona', 'metai': 2021, 'kaina': 50000},
        {'gamintojas': 'Honda', 'modelis': 'Civic', 'spalva': 'Mėlyna', 'metai': 2018, 'kaina': 9000}
    ]

    for duom in duomenys:
        automobilis = Automobilis(**duom)
        db.session.add(automobilis)

    db.session.commit()
    print("Duomenys pridėti sėkmingai!")

