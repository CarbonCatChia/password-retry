password = "a123456"
i = 3 #剩餘機會
while True:
	pwd = input("請輸入密碼: ")
	if pwd == password:
		print("密碼正確，成功登入")
		break #逃出迴圈
	else:
		i = i-1
		print("密碼錯誤，還剩下", i,"機會")
		if i == 0:
			break
