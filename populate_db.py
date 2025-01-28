from models import Automobilis, db
from app import app

with (app.app_context()):
    # db.create_all()
    duomenys = [
        {"gamintojas": "Toyota", "modelis": "Corolla", "spalva": "Balta", "metai": 2020, "kaina": 20000},
        {"gamintojas": "BMW", "modelis": "X5", "spalva": "Juoda", "metai": 2022, "kaina": 55000},
        {"gamintojas": "Audi", "modelis": "A4", "spalva": "Sidabrinė", "metai": 2019, "kaina": 23000},
        {"gamintojas": "Mercedes", "modelis": "C-Class", "spalva": "Raudona", "metai": 2021, "kaina": 45000},
        {"gamintojas": "Ford", "modelis": "Focus", "spalva": "Mėlyna", "metai": 2020, "kaina": 18000},
        {"gamintojas": "Volkswagen", "modelis": "Golf", "spalva": "Žalia", "metai": 2019, "kaina": 20000},
        {"gamintojas": "Tesla", "modelis": "Model 3", "spalva": "Balta", "metai": 2022, "kaina": 50000},
        {"gamintojas": "Honda", "modelis": "Civic", "spalva": "Pilka", "metai": 2021, "kaina": 21000},
        {"gamintojas": "Hyundai", "modelis": "Elantra", "spalva": "Geltona", "metai": 2020, "kaina": 19000},
        {"gamintojas": "Kia", "modelis": "Sportage", "spalva": "Ruda", "metai": 2021, "kaina": 26000},
        {"gamintojas": "Mazda", "modelis": "CX-5", "spalva": "Juoda", "metai": 2022, "kaina": 30000},
        {"gamintojas": "Subaru", "modelis": "Outback", "spalva": "Balta", "metai": 2020, "kaina": 28000},
        {"gamintojas": "Jeep", "modelis": "Wrangler", "spalva": "Mėlyna", "metai": 2023, "kaina": 60000},
        {"gamintojas": "Chevrolet", "modelis": "Malibu", "spalva": "Juoda", "metai": 2021, "kaina": 24000},
        {"gamintojas": "Nissan", "modelis": "Altima", "spalva": "Sidabrinė", "metai": 2020, "kaina": 18500}
    ]

    for duom in duomenys:
        automobilis = Automobilis(**duom)
        db.session.add(automobilis)

    db.session.commit()
    print("Duomenys pridėti sėkmingai!")
