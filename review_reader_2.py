data = []
i = 0 # i = counts
with open('reviews.txt', 'r') as f:
	for message in f:
		data.append(message.strip())
		i += 1
		if i % 1000 == 0: # %: 求餘數指令，寫入這行等於讀取1000筆印一次
			print(len(data)) # 在每個loop裡面都print出索引總數，可以知道進度，不過多了print指令也會讓loop時間變長
print('The total number of the review is: ', len(data))