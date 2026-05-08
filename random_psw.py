import secrets
import string
import time

# ANSI renk kodları
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Karakter setleri
LOWER = "abcçdefgğhıijklmnoöprsştuüvyz"
UPPER = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
NUMBERS = string.digits
SYMBOLS = "!'^+%&/()=?~*_-<>#:;"

ALL_CHARS = LOWER + UPPER + NUMBERS + SYMBOLS


def password_strength(length):
    if length < 12:
        return "Zayıf"
    elif length < 20:
        return "Orta"
    elif length < 30:
        return "Güçlü"
    else:
        return "Çok Güçlü"


def generate_password():
    length = secrets.randbelow(25) + 16

    # Her karakter türünden en az 1 tane
    password = [
        secrets.choice(LOWER),
        secrets.choice(UPPER),
        secrets.choice(NUMBERS),
        secrets.choice(SYMBOLS)
    ]

    # Kalan karakterleri doldur
    for _ in range(length - 4):
        password.append(secrets.choice(ALL_CHARS))

    # Karıştır
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def main():
    print(f"{CYAN}Şifre oluşturuluyor...{RESET}")

    try:
        while True:
            password = generate_password()

            print(
                f"\r{RED}Durdurmak için CTRL+C → {password}{RESET}",
                end=""
            )

            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\n")

        print(f"{GREEN}=== OLUŞTURULAN ŞİFRE ==={RESET}")
        print(f"{GREEN}Şifre : {password}{RESET}")
        print(f"{GREEN}Uzunluk : {len(password)}{RESET}")

        print(
            f"{YELLOW}Güç Seviyesi : "
            f"{password_strength(len(password))}{RESET}"
        )


if __name__ == "__main__":
    main()