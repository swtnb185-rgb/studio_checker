import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_okubo_status():
    # 大久保店のIDは '6'、日付は実行時の今日に設定
    today = datetime.now().strftime("%Y/%m/%d")
    url = f"https://www.studioworcle.com/search/?date={today}&store=6"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 検索結果のスタジオ一覧を取得（クラス名はサイトの構造に合わせて調整）
    studios = soup.find_all('div', class_='room-item') # 仮のクラス名です
    
    results = []
    for studio in studios:
        name = studio.find('h3').text.strip()
        # 空室状況（◯や×など）を抽出
        status = studio.find('div', class_='status').text.strip()
        results.append({"room": name, "status": status})
    
    return results

# 実行テスト
if __name__ == "__main__":
    data = get_okubo_status()
    print(data)
