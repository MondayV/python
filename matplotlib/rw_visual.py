import matplotlib.pyplot as plt
from random_walk import RandomWalk

fig, ax = plt.subplots(figsize=(10, 6))

#只要程序处于活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    #清楚之前的绘图
    ax.clear()

    # 绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    sizes = [max(1, i/100) for i in point_numbers]  #
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, 
               cmap=plt.cm.Blues, s=sizes, edgecolors='none', alpha=0.7)
    
    #突出起点和终点
    ax.scatter(0, 0, c='green', s=100, edgecolors='none', zorder=3)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', zorder=3)

    #
    ax.set_title(f"随机漫步({rw.num_points}步)",fontsize=14)

    #隐藏坐标轴
    ax.axis('off')

    #显示图形
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1) #短暂暂停

    keep_running = input("Make another walk?(y/n):").strip().lower()
    if keep_running == 'n':
        break