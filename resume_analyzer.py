
from PyPDF2 import PdfReader
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("Brak klucza API w zmiennych środowiskowych")

openai = OpenAI(api_key=openai_api_key)


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

def cv_prompt(cv_parser):

    system_prompt = """Jesteś specjalistą ds. rekrutacji i analizy danych. Twoim zadaniem jest dokładnie przeanalizować przesłane CV i wyodrębnić z niego następujące informacje w uporządkowanej formie:
    - Umiejętności:
    Techniczne (np. języki programowania, narzędzia, technologie)
    Miękkie (np. komunikacja, praca w zespole)
    - Doświadczenie zawodowe:
    Dla każdej pozycji:
    Nazwa firmy
    Rola / stanowisko
    Okres zatrudnienia
    Główne obowiązki i osiągnięcia
    Kluczowe umiejętności zdobyte
    - Wykształcenie:
    Kierunek studiów
    Poziom (licencjat, magister itp.)
    Uczelnia
    Rok ukończenia
    - Języki obce:
    Język i poziom biegłości (np. B2, C1)
    Certyfikaty (jeśli dostępne)
    - Inne istotne informacje:
    Certyfikaty branżowe
    Kursy dodatkowe
    Projekty własne lub open source
    Wolontariat / działalność społeczna

    Zwróć wynik analizy w formacie JSON, oto przykład:
    {
      "umiejetnosci": {
        "techniczne": ["Java", "Git", ...],
        "miekke": ["Komunikacja", "Praca w zespole", ...]
      },
      "doswiadczenie": [
        {
          "firma": "ABC Sp. z o.o.",
          "stanowisko": "Programista Java",
          "okres": "2020–2023",
          "obowiazki": ["Tworzenie aplikacji backendowych", "Udział w code review", ...],
          "osiagniecia": ["Zoptymalizowanie działania serwisu o 30%", ...]
        }
      ],
      "edukacja": [
        {
          "uczelnia": "Uniwersytet Jagielloński",
          "kierunek": "Informatyka",
          "poziom": "Magister",
          "rok_ukonczenia": 2020
        }
      ],
      "jezyki_obce": [
        {
          "jezyk": "angielski",
          "poziom": "B2"
        }
      ],
      "inne_informacje": {
        "certyfikaty": ["Oracle Certified Java Programmer", ...],
        "projekty": ["Aplikacja do zarządzania zadaniami – GitHub", ...],
        "wolontariat": []
      }
    }
    """

    prompt = [
        {'role': 'system', 'content': system_prompt}
    ]

    user_prompt = cv_parser

    prompt.append({'role':'user', 'content': user_prompt})

    response = openai.chat.completions.create(
        model= "gpt-4o-mini", 
        messages=prompt,
        temperature= 0.0,
    )

    cv_description = response.choices[0].message.content

    return cv_description
