items = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah']
lottery = LotteryDrawingTool(items)

# 抽出 4 名
drawn_names = lottery.draw()
print(f"Drawn names: {drawn_names}")

# 重設後再抽一次
lottery.reset()
drawn_names = lottery.draw()
print(f"Drawn names after reset: {drawn_names}")
