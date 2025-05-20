import random

def lottery(participants, num_winners=1):
    # 移除重複參加者
    participants = list(set(participants))
    
    # 隨機抽出得獎者
    winners = random.sample(participants, num_winners)
    
    return winners

# 範例使用
participants = ["Alice", "Bob", "Charlie", "David", "Eve"]
num_winners = 2

winners = lottery(participants, num_winners)
print(f"得獎者是: {winners}")
