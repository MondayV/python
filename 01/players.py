players = ['charles','martina','florence','eli']
print(players[0:3])  #前三个元素
print(players[1:4])  #后三个元素
print(players[:4])   #从头开始输出四个
print(players[2:])   #从后开始输出两个
print(players[-3:])  #输出最后三个
 
 #遍历列表的所有元素
print("\nHere are the first players on my team:")
for player in players[:4]:
    print(player.title())