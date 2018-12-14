import random
start = input('請輸入開始值: ')
end = input('請輸入結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了! ')
		break
	elif num > r:
		print('太大囉')
	elif num < r:
		print('太小囉')
	
print('這是你猜的第', count, '次')	


# 能顯示出幾到幾


