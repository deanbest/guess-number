import random

r = random.randint(1, 100) # 注意空格
while True:
	num = input('請猜數字: ')
	num = int(num) # 先把猜對的狀況陳列
	if num == r:
		print('猜中了, 好棒棒!')
		break # 猜中完就跳出迴圈
	elif num > r:
		print('比答案大喔')
	elif num < r:
		print('比答案小啦')


