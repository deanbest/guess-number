import random

r = random.randint(1, 100) # 注意空格
count = 0 # 放到while true裡的話, 變成每猜一次, 就把計數歸0, 把要變化的放在迴圈內
while True:
	count = count + 1 # 快寫法: count += 1
	num = input('請猜數字: ')
	num = int(num) # 先把猜對的狀況陳列
	if num == r:
		print('猜中了, 好棒棒!')
		print('猜了', count, '次才中, 要加油喔!')
		break # 猜中完就跳出迴圈
	elif num > r:
		print('比答案還大喔')
	elif num < r:
		print('比答案還小呢')
	print('這是你猜的第', count, '次') # 避免重覆寫, 故放在if最外面


