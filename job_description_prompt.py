
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("Brak klucza API w zmiennych środowiskowych")

openai = OpenAI(api_key=openai_api_key)

def job_data_prompt(resume_data):
    system_prompt= '''Jako asystent, Twoim zadaniem jest przeanalizowanie opisu stanowiska pracy i wypisanie jego kluczowych elementów w strukturalny sposób. 
    Dla każdego opisu wykonaj analizę i zwróć odpowiedź w następującym formacie (bez użycia markdown):
    Stanowisko: [nazwa stanowiska]
    Firma: [nazwa firmy]
    Lokalizacja: [miasto, region, kraj – jeśli dostępne]
    Tryb pracy: [zdalny / hybrydowy / stacjonarny / opcjonalnie]
    Typ zatrudnienia: [pełen etat / część etatu / umowa zlecenie / B2B / staż / praktyki / inny]
    Poziom stanowiska: [junior / mid / senior / kierownicze / specjalista]
    Opis obowiązków:
    - [punkt 1]
    - [punkt 2]
    - [punkt 3 itd.]

    Wymagania kandydata:
    - [punkt 1]
    - [punkt 2]
    - [punkt 3 itd.]

    Zalety oferty:
    - [punkt 1]
    - [punkt 2]
    - [punkt 3 itd.]

    Link do oferty: [jeśli dostępny]

    Uwagi: [opcjonalnie – np. czy wymagana znajomość języka, czy są benefity, inne szczegóły].
    Zwróć uwagę na priorytety w opisie (np. „konieczne”, „opcjonalne”, „wysoko cenione”).
    Działaj dokładnie i nie pomijaj istotnych szczegółów. Jeśli jakaś informacja nie jest dostępna w tekście, pozostaw pole puste lub napisz „nie określono”. 
    Przetwarzaj tekst tak, jakbyś przygotowywał dane do bazy ofert pracy. Używaj języka polskiego. 
    Nie dodawaj żadnych komentarzy poza formatem wynikowym.
    '''    
    prompt = [
        {'role': 'system', 'content': system_prompt}
    ]

    user_prompt = resume_data

    prompt.append({'role':'user', 'content': user_prompt})

    response = openai.chat.completions.create(
        model= "gpt-4o-mini", 
        messages=prompt,
        temperature= 0.0,
    )

    data = response.choices[0].message.content

    return data
