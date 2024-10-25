import requests
import time

# Giả sử URL API của bàn chơi và đầu vào dữ liệu có định dạng { "player_score": int, "banker_score": int }
api_url = "https://api.example.com/baccarat/live_game"  # Đổi URL theo thực tế

# Khởi tạo biến lưu kết quả
results = {"Player": 0, "Banker": 0, "Tie": 0}
total_games = 0

while True:
    # Gửi yêu cầu đến API để lấy dữ liệu bàn chơi hiện tại
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # Phân tích dữ liệu JSON
        game_data = response.json()
        
        # Đọc điểm Player và Banker
        player_score = game_data["player_score"]
        banker_score = game_data["banker_score"]
        
        # Tăng số lượng ván chơi
        total_games += 1
        
        # Cập nhật kết quả dựa vào điểm
        if player_score > banker_score:
            results["Player"] += 1
        elif banker_score > player_score:
            results["Banker"] += 1
        else:
            results["Tie"] += 1

        # Hiển thị xác suất cập nhật
        print("\nKết quả sau", total_games, "ván chơi:")
        for key in results:
            probability = results[key] / total_games * 100
            print(f'{key}: {probability:.2f}%')

    else:
        print("Không thể truy cập dữ liệu. Đang chờ kết nối lại...")
    
    # Tạm dừng 1 giây trước khi lấy kết quả tiếp theo
    time.sleep(1)
