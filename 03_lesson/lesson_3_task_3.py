from address import Address
from mailing import Mailing
to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "15", "7")
mailing = Mailing(to_address, from_address, 250, "TRACK123456789")
result = (f"Отправление {mailing.track} из {from_address.get_full_address()} "
          f"в {to_address.get_full_address()}. "
          f"Стоимость {mailing.cost} рублей.")
print(result)