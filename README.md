# Dokumentacja projektu

## Opis struktury projektu
Projekt składa z trzech głównych plików:
1. dataset.csv – Plik danych w formacie CSV, który zawiera 114000 wierszy z informacjami na temat utworów. Dane pobrane zostały z: https://www.kaggle.com/datasets/priyamchoksi/spotify-dataset-114k-songs/code
2. spotify_project.ipynb – Notatnik Jupyter Notebook, który zawiera cały proces analizy danych. W tym pliku znajdują się etapy:
Czyszczenie danych: Usuwanie brakujących wartości, usuwanie duplikatów, konwersje typów danych.
Eksploracyjna analiza danych (EDA): Tworzenie wykresów, obliczanie podstawowych statystyk.
Modelowanie: Budowanie i trenowanie modeli predykcyjnych.
3. spotify_streamlit.py – Plik Streamlit, który zawiera aplikację webową do wizualizacji wyników analizy danych. Aplikacja umożliwia interaktywne wyświetlanie danych oraz wizualizacji. Nie przedstawia modelów trenowanych na zbiorze danych.

Pliki projektowe działają na wersji Python==3.10.6.
W celu zainstalowania potrzebnych bibliotek, wykorzystaj kod `pip install -r requirements.txt`

Aby uruchomić aplikację Streamlit, w terminalu uruchom kod `streamlit run spotify_streamlit.py`

## Opis kolumn
1. track_id: Unikalny identyfikator Spotify dla każdego utworu.
2. artists: Nazwy artystów, którzy wykonali utwór.
3. album_name: Nazwa albumu, na którym pojawia się utwór.
4. track_name: Tytuł utworu.
5. popularity: Wartość między 0 a 100, wskazująca popularność utworu na podstawie ostatnich odtworzeń.
6. duration_ms: Długość utworu w milisekundach.
7. explicit: Wartość logiczna wskazująca, czy utwór zawiera treści dla dorosłych.
8. danceability: Określa, jak odpowiedni jest utwór do tańca (0.0 = najmniej odpowiedni, 1.0 = najbardziej odpowiedni).
9. energy: Reprezentuje intensywność i aktywność utworu (0.0 = niska energia, 1.0 = wysoka energia).
10. key: Tonacja muzyczna utworu.
11. loudness: Ogólna głośność utworu w decybelach (dB).
12. mode: Określa modalność (durowa lub molowa) utworu.
13. speechiness: Wykrywa obecność słów mówionych w utworze.
14. acousticness: Miara pewności, czy utwór jest akustyczny (0.0 = nieakustyczny, 1.0 = wysoce akustyczny).
15. instrumentalness: Przewiduje, czy utwór zawiera wokale (0.0 = zawiera wokale, 1.0 = instrumentalny).
16. liveness: Wykrywa obecność publiczności w nagraniu (0.0 = nagranie studyjne, 1.0 = występ na żywo).
17. valence: Mierzy muzyczną pozytywność przekazywaną przez utwór (0.0 = negatywna, 1.0 = pozytywna).
18. tempo: Szacowane tempo utworu w uderzeniach na minutę (BPM).
19. time_signature: Sygnatura czasowa utworu (od 3 do 7).