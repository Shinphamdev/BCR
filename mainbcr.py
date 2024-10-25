import requests
import json

# Hàm gọi API lấy dữ liệu từ một endpoint baccarat giả định
def fetch_baccarat_data(api_url, api_key):
    headers = {
        'Authorization': f'Bearer {api_key}',  # Nếu API yêu cầu khóa truy cập
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()  # Giả sử API trả về dữ liệu dưới dạng JSON
            return data
        else:
            print(f"Error: Unable to fetch data (Status code: {response.status_code})")
            return None
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

# Hàm xử lý dữ liệu baccarat và hiển thị thống kê đơn giản
def process_baccarat_data(data):
    if not data:
        return
    
    player_wins = sum(1 for game in data if game['outcome'] == 'Player')
    banker_wins = sum(1 for game in data if game['outcome'] == 'Banker')
    ties = sum(1 for game in data if game['outcome'] == 'Tie')
    
    print(f"Player wins: {player_wins}")
    print(f"Banker wins: {banker_wins}")
    print(f"Ties: {ties}")
    
    # Dự đoán xu hướng tiếp theo dựa trên kết quả
    if player_wins > banker_wins:
        print("Prediction: Player will win next")
    elif banker_wins > player_wins:
        print("Prediction: Banker will win next")
    else:
        print("Prediction: Tie might happen next")

# URL API giả định cung cấp kết quả baccarat
api_url = "https://11lucky.fun/baccarat/results"
api_key = "your_api_key_here"  # Nếu API yêu cầu khóa truy cập

# Lấy dữ liệu từ API
data = fetch_baccarat_data(api_url, api_key)

# Xử lý dữ liệu
process_baccarat_data(data)
