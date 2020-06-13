# ćwiczenie 1
lorem_ipsum = """Lorem Ipsum jest tekstem stosowanym jako przykładowy
wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w.
przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków
później zaczął być używany przemyśle elektronicznym, pozostając praktycznie
niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy
Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne
wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na
komputerach osobistych, jak Aldus PageMaker"""

# ćwiczenie 2
imie = "Konrad"
nazwisko = "Łuczaj"

litera_1 = imie[2]
litera_2 = nazwisko[3]

liczba_liter_1 = imie.count(litera_1)
liczba_liter_2 = nazwisko.count(litera_2)

print(
  "W tekście jest {0} liter {1} oraz {2} liter {3}"
  .format(liczba_liter_1, litera_1, liczba_liter_2, litera_2)
)

# ćwiczenie 3
print("{:->10}".format("test"))

print("{:-<10}".format("test"))

print("{:-^10}".format("test"))

slownik = {'pierwszy': 'Python', 'drugi': '3.7'}

print("{first} {last}".format(first='test2', last='test1'))

ja = {"imie": "Konrad", "nazwisko": "Łuczaj"}

print("{p[imie]} {p[nazwisko]}".format( p = ja ))

# ćwiczenie 4
zmienna_typu_string = "{imie} {nazwisko}".format(imie=imie, nazwisko=nazwisko)

print(dir(zmienna_typu_string))
help(zmienna_typu_string.swapcase)

print(zmienna_typu_string.swapcase())

# ćwiczenie 5
ja = "Konrad Łuczaj"
print((ja[::-1]).capitalize())

# ćwiczenie 6
lista_1 = list(range(1, 11))

lista_2 = lista_1[5:]
lista_1 = lista_1[:5]

print(lista_1)
print(lista_2)

# ćwiczenie 7
lista = lista_1 + lista_2
lista.insert(0, 0)
kopia_listy = lista
lista.sort(reverse=True)

print(lista)

# ćwiczenie 8
lista_studentow = ((123456789, "Brad Pitt"), (987654321, "George Clooney"))

# ćwiczenie 9
slownik = {
    123456789: {
        'imie': "Brad",
        'nazwisko': "Pitt",
        'wiek': 56,
        'e-mail': "brad.pitt@gmail.com",
        'rok urodzenia': 1963,
        'adres': "Shawnee, Oklahoma, Stany Zjednoczone"
    },
    9876543621: {
        'imie': "George",
        'nazwisko': "Clooney",
        'wiek': 59,
        'e-mail': "goerge.clooney@gmail.com",
        'rok urodzenia': 1961,
        'adres': "Lexington, Kentucky, Stany Zjednoczone"
    }

}

# ćwiczenie 10
numery_telefonow = ["100 200 300", "400 500 600", "700 800 900", "100 200 300"]
print(set(numery_telefonow))

# ćwiczenie 11
for x in range(1, 11):
    print(x)

# ćwiczenie 12
for x in range(100, 15, -5):
    print(x)

# ćwiczenie 13
telefony = [
    {
        "producent": "Apple",
        "model": "X",
        "cena": 4999
    },
    {
        "producent": "Samsung",
        "model": "S20",
        "cena": 5299
    },
    {
        "producent": "Xiaomi",
        "model": "Mi Mix 3",
        "cena": 3699
    }
]

print('\nLista telefonów:')
for telefon in telefony:
    print(
        "\nProducent: {producent}\nModel: {model}\nCena: {cena}"
        .format(
            producent=telefon["producent"],
            model=telefon["model"],
            cena=telefon["cena"]
            )
        )