
items = ['item1', 'item2', 'item3', 'item4', 'item5']
lottery = LotteryDrawingTool(items)

# 抽出所有項目
while True:
    item = lottery.draw()
    if item is None:
        break
    print(item)

# 重設後再抽一次
lottery.reset()
