def legg_sammen(a, b):
    return a + b


def trekk_fra(a, b):
    return a - b


def multipliser(a, b):
    return a * b


def divider(a, b):
    if b == 0:
        raise ZeroDivisionError("Kan ikke dele på null")
    return a / b


def les_tall(tekst):
    while True:
        try:
            return float(input(tekst))
        except ValueError:
            print("Ugyldig tall, prøv igjen.")


def main():
    valg = {
        "1": ("Legg sammen", legg_sammen),
        "2": ("Trekk fra", trekk_fra),
        "3": ("Multipliser", multipliser),
        "4": ("Divider", divider),
    }

    print("Enkel kalkulator")
    for nummer, (navn, _) in valg.items():
        print(f"{nummer}. {navn}")

    valgt = input("Velg operasjon (1-4): ").strip()
    if valgt not in valg:
        print("Ugyldig valg.")
        return

    a = les_tall("Skriv inn første tall: ")
    b = les_tall("Skriv inn andre tall: ")

    navn, funksjon = valg[valgt]
    try:
        resultat = funksjon(a, b)
    except ZeroDivisionError as e:
        print(f"Feil: {e}")
        return

    print(f"Resultat: {resultat}")


if __name__ == "__main__":
    main()
