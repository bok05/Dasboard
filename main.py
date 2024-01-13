import pyautogui
import pytesseract
from PIL import Image, ImageShow
import re
import time
import logging

# Logging konfigurieren
logging.basicConfig(filename='extracted_text.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Pfad zu Tesseract-OCR konfigurieren
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Funktion, um einen Screenshot zu machen und Text daraus zu extrahieren
def capture_and_extract_text(region=None):
    # Einen Screenshot eines bestimmten Bereichs machen
    screenshot = pyautogui.screenshot(region=region)

    # Bild in Text umwandeln
    text = pytesseract.image_to_string(screenshot)

    # Loggen Sie den extrahierten Text
    logging.info('Extrahierter Text: %s', text)

    return text

# Definieren Sie den Bereich, den Sie überwachen möchten (x, y, Breite, Höhe)
monitor_region = (1500, 900, 1916, 1080)  # Beispielwerte, anpassen nach Bedarf

# Die Schleife, die kontinuierlich nach dem gewünschten Textmuster sucht
desired_text = None
while True:
    extracted_text = capture_and_extract_text(region=monitor_region)

    # Prüfen, ob der Text dem gewünschten Muster entspricht
    if re.search("Twitch", extracted_text): # Verwenden Sie Ihr spezifisches Muster
        print(extracted_text)
        Live = extracted_text
        print("Gefundener Text:", Live)
          # Schleife beenden, wenn das Muster gefunden wurde

  # Kurze Pause, um das System nicht zu überlasten
    if re.search("Wathsapp", extracted_text): # Verwenden Sie Ihr spezifisches Muster
        print(extracted_text)
        Nachricht = extracted_text
        print("Gefundener Text:", Nachricht)
          # Schleife beenden, wenn das Muster gefunden wurde
    if re.search("Bereal", extracted_text): # Verwenden Sie Ihr spezifisches Muster
        print(extracted_text)
        Bereal = extracted_text
        print("Gefundener Text:", Bereal)
          # Schleife beenden, wenn das Muster gefunden wurde
    if re.search("Youtube", extracted_text): # Verwenden Sie Ihr spezifisches Muster
        print(extracted_text)
        Youtube = extracted_text
        print("Gefundener Text:", Youtube)
          # Schleife beenden, wenn das Muster gefunden wurde
    if re.search("Beer", extracted_text): # Verwenden Sie Ihr spezifisches Muster
        print(extracted_text)
        Beer = extracted_text
        print("Gefundener Text:", Beer)
          # Schleife beenden, wenn das Muster gefunden wurde

    time.sleep(1)
# Weiterer Code kann hier folgen, der `desired_text` verwendet
