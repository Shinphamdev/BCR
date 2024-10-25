import random

# Các kết quả có thể xảy ra trong baccarat
outcomes = ['Player', 'Banker', 'Tie']

# Danh sách lưu kết quả các ván trước
history = []

# Hàm mô phỏng kết quả của một ván baccarat
def simulate_round():
    result = random.choice(outcomes)
    history.append(result)
    return result

# Hàm đếm số lần xuất hiện của mỗi kết quả
def count_results():
    player_wins = history.count('Player')
    banker_wins = history.count('Banker')
    ties = history.count('Tie')
    
    return player_wins, banker_wins, ties

# Hàm đưa ra "dự đoán" dựa trên lịch sử (chỉ là ngẫu nhiên ở đây)
def predict_next():
    if len(history) < 5:
        return "Insufficient data to predict."
    
    player_wins, banker_wins, ties = count_results()
    
    # Dự đoán theo xu hướng thắng nhiều nhất
    if player_wins > banker_wins:
        return "Predicted: Player"
    elif banker_wins > player_wins:
        return "Predicted: Banker"
    else:
        return "Predicted: Tie"

# Chạy mô phỏng
for i in range(10):
    result = simulate_round()
    print(f"Round {i+1} result: {result}")
    prediction = predict_next()
    print(prediction)

# Hiển thị thống kê cuối cùng
player_wins, banker_wins, ties = count_results()
print(f"Player wins: {player_wins}, Banker wins: {banker_wins}, Ties: {ties}")
