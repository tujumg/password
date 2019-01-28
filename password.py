password = 'a123456'
i = 3
i = int(i)
while i > 0: 
	pwd = input('請輸入密碼')
	if pwd == 'password':
		print('登入成功')
		break
	else:
		i = i - 1
		print('輸入錯誤')
		if i > 0:
			print('還有',i,'次機會')

