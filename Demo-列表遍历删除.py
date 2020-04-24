# 列表遍历删除

words = ['hello','goods','gooo','world','digot','alphago']
w = 'go'
i = 0
while i < len(words):
	if w in words[i]:
		del words[i]
		continue
	# print(words[i])
	i += 1

print(words)
