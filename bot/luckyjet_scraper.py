import requests
from bs4 import BeautifulSoup

def fetch_luckyjet_data(endpoint_url, user_agent):
    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(endpoint_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Exemple de récupération de données (à adapter selon le site)
        result = soup.find("div", class_="luckyjet-result")
        return result.text.strip() if result else None

    except Exception as e:
        print("Erreur lors du scraping :", e)
        return None
