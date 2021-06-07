class Question:
    def __init__(self, pytanie, odp1, odp2, odp3, poprawna):
        self.__pytanie = pytanie
        self.__odp1 = odp1
        self.__odp2 = odp2
        self.__odp3 = odp3
        if poprawna == 1:
            self.__poprawna = self.__odp1
        elif poprawna == 2:
            self.__poprawna = self.__odp2
        else:
            self.__poprawna = self.__odp3

    def get_pytanie(self):
        return self.__pytanie

    def get_odpowiedzi(self):
        return [self.__odp1, self.__odp2, self.__odp3]

    def get_poprawna(self):
        return self.__poprawna

    def czy_poprawna(self, odpowiedz):
        return self.__poprawna == odpowiedz


class Test:
    def __init__(self):
        self.__pytania = []
        self.__punkty = 0

    def dodaj_pytanie(self, pytanie, odp1, odp2, odp3, poprawna):
        self.__pytania.append(Question(pytanie, odp1, odp2, odp3, poprawna))

    def ilosc_pytan(self):
        return len(self.__pytania)

    def get_pytanie(self, id):
        return self.__pytania[id]

    def sprawdz_odpowiedz(self, id_pytania, odpowiedz):
        if self.__pytania[id_pytania].czy_poprawna(odpowiedz):
            self.__punkty += 10
            return True
        return False

    def get_wynik(self):
        return self.__punkty


def get_test(id=0):
    test = Test()
    test.dodaj_pytanie(
        "Jakiej kategorii prawo jazdy jest wymagane, gdy chcesz kierować czterokołowcem innym niż lekki?", "B1", "A",
        "AM", 1)
    test.dodaj_pytanie("Który z obowiązków dotyczy właściciela samochodu osobowego?",
                       "Zawarcie umowy ubezpieczenia NW.", "Poddawanie pojazdu okresowym badaniom technicznym.",
                       "Zawarcie umowy ubezpieczenia Autocasco.", 2)
    test.dodaj_pytanie("Kiedy powinieneś sprawdzać ciśnienie w ogumieniu samochodu osobowego?",
                       "Bezpośrednio przed rozpoczęciem podróży.", "Po zakończeniu jazdy.",
                       "Co najmniej dobę przed zaplanowaną podróżą.", 1)
    test.dodaj_pytanie("W jaki sposób wolno Ci przewozić ładunek w przyczepie ciągniętej przez samochód osobowy?",
                       "Ładunek może zasłaniać niektóre światła przyczepy.",
                       "Ładunek nie może naruszać stateczności pojazdu.",
                       "Ładunek nie musi być zabezpieczony przed zmianą położenia.", 2)
    test.dodaj_pytanie("W jaki sposób przewieziesz ładunek w przyczepie ciągniętej przez samochód osobowy?",
                       "Zabezpieczę go przed przemieszczaniem.", "Umieszczę ładunek luźno na przyczepie.",
                       "Nie zabezpieczę ładunku przed przemieszczaniem, jeżeli będę jechał wolno.", 1)
    test.dodaj_pytanie("Jak przewieziesz ładunek sypki w przyczepie ciągniętej przez samochód osobowy?",
                       "Niezasłonięty - umieszczony poniżej wysokości burt.", "Nie przekraczajac prędkości 30 km/h.",
                       "Zasłonięty w szczelnej skrzyni ładunkowej.", 3)
    test.dodaj_pytanie(
        "Jak powinieneś zabezpieczyć urządzenie, którym zamocowałeś ładunek w przyczepie ciągniętej przez samochód osobowy?",
        "Tak, żeby mocowanie nie rozluźniło się.", "Może swobodnie zwisać z przyczepy.",
        "Nie musi być zabezpieczone przed spadnięciem podczas jazdy.", 1)
    test.dodaj_pytanie("W jaki sposób powinien być umieszczony ładunek na samochodzie osobowym?",
                       "Może nieznacznie zasłaniać tablice rejestracyjne",
                       "Może zasłaniać tylne światło przeciwmgłowe.", "Nie może ograniczać widoczności drogi.", 3)
    test.dodaj_pytanie("Jak umieścisz bagaż w samochodzie osobowym?",
                       "Najcięższe bagaże włożę najgłębiej i najniżej, w centralnej części bagażnika.",
                       "W dowolny sposób.", "Najcięższe bagaże włożę w górnej części bagażnika, nad lżejszymi.", 1)
    test.dodaj_pytanie("W jaki sposób umieścisz ładunek na przyczepie samochodu osobowego?",
                       "Tak, aby nie zasłaniał świateł przyczepy.", "Umieszczę go po jednej stronie przyczepy.",
                       "Umieszczę go zawsze w tylnej części przyczepy.", 1)

    return test


