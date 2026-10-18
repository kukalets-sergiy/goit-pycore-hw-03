import re


def normalize_phone(phone_number: str) -> str:
    # Remove all non-digit characters except for the leading plus sign
    phone = re.sub(r"[^\d+]", "", phone_number)

    # if the phone number starts with a plus sign, return it as is
    if phone.startswith("+"):
        return phone

    # if the phone number starts with "380" or "38", add a plus sign in front
    if phone.startswith("380"):
        return "+" + phone

    if phone.startswith("38"):
        return "+" + phone

    # if the phone number doesn't start with a plus sign or "380" or "38", add the default country code "+38"
    return "+38" + phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
