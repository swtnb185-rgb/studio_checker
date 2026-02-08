import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_okubo_status():
    # 本日の日付を取得
    today = datetime.now().strftime("%Y/%m/%d")
    # 大久保店のURL
    url = f"https://www.studioworcle.com/search/?date={today}&store=6"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # 取得できたか確認用
        print(f"URL access success: {url}")
        
        # 現時点ではファイルが作られることを確認するため、テストデータを保存
        results = {
            "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "store": "Okubo",
            "message": "Scraper is running!"
        }
        
        with open("okubo_status.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        print("Successfully saved okubo_status.json")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_okubo_status()
