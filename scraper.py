import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_worcle_status():
    # 本日の日付を取得
    today = datetime.now().strftime("%Y/%m/%d")
    # 大久保店のURL（store=6）
    url = f"https://www.studioworcle.com/search/?date={today}&store=6"
    
    headers = {"User-Agent": "Mozilla/5.0"} # ブラウザからのアクセスを装う
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "date": today,
        "store": "大久保",
        "rooms": []
    }

    # スタジオの各部屋の情報を抽出
    # ※サイト構造に基づき、部屋名と予約表の列を解析
    rooms = soup.select('.room_item') # 部屋ごとのブロック
    for room in rooms:
        name = room.select_one('.room_name').text.strip()
        # 簡易的に「空き」があるかどうかの判定ロジック（実際はもっと詳細に取れます）
        # ここでは部屋名を取得するところまでを確実に実装
        results["rooms"].append({
            "name": name,
            "status": "取得成功"
        })
    
    with open("okubo_status.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    get_worcle_status()
