# Zadanie rekrutacyjne Profil Software
## Uruchomienie projektu
Projekt używa wersji pythona 3.7. Biblioteki użyte w projekcie znajdują się w pliku requirements.txt. W celu zainstalowania koniecznych bibliotek
z linii poleceń wywołaj:
```javascript
pip install -r requirements.txt
```

Przed wyświetleniem danych nalezy załadować informacje do bazy danych w tym celu wywołaj:
```javascript
python person.py --load_data PATH_TO_DATA
```
gdzie PATH_TO_DATA jest względną scieżką do pliku z danymi

lub załaduj losowe dane wywołując:
```javascript
python person.py --load_random_data HOW_MANY
```
gdzie HOW_MANY mówi ile losowych użytkowników załadować

## Dostępne komendy
* Wyświetlenie pomocy:
```javascript
python person.py -h
```

* Załadowanie danych do bazy danych. 
```javascript
python person.py --load_data PATH_TO_DATA
```
gdzie:
PATH_TO_DATA- ścierzka do pliku z danymi, przykładowo: python person.py --load_data inputs/persons.json

* Załadowanie losowych danych
```javascript
python person.py --load_random_data HOW_MANY
```
gdzie:
HOW_MANY - ilość losowych użytkowników załadowanych do bazy

* Wyświetlenie procentu kobiet i męszczyzn
```javascript
python person.py --gender_percentage
```

* Wyświetlenie procentu kobiet i męszczyzn
```javascript
python person.py --average_age gender
```
gdzie:
gender jest płcią dla której wyświetlamy średnią. Dostępne wybory: male, female, both.
Przykładowo: python person.py --average_age male

* Wyświetlenie N najpopularniejszych miast pod względem występowania
```javascript
python person.py --cities_popularity N
```
gdzie:
N- ilość wyświetlonych miast.

* Wyświetlenie N najpopularniejszych haseł pod względem występowania
```javascript
python person.py --password_popularity N
```
gdzie:
N- ilość wyświetlonych haseł.

* Wyświetlenie najleprzego hasła
```javascript
python person.py --strongest_password
```

* Wyświetlenie użytkowników urodzonych pomiędzy wskazanymi datami 
```javascript
python person.py --born_between MIN_DATE MAX_DATE
```
gdzie:
MIN_DATE - jest datą ograniczającą od dołu,
MAX_DATE - jest datą ograniczającą od góry.
Daty powinny byś w formacie YYYY-MM-DD