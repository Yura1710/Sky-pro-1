from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79277463218"))
catalog.append(Smartphone("Samsung", "Galaxy A23", "+79273456789"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12 pro", "+79276543789"))
catalog.append(Smartphone("Aplee", "iPhone 12 pro Max", "+79278764567"))
catalog.append(Smartphone("Realme", "13", "+79275674567"))
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
    