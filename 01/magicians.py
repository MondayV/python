magicians = ['alice','david','carolina']
for magicians in magicians:
    print(magicians.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magicians.title() + ".\n")  #首行缩进与循环行一致，会循环三次
print("Thank you, everyone.That was a great magic show!")   #首行缩进与循环主体一致，会循环一次