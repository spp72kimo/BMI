# 這是一個輸入身高、體重來計算BMI的程式
height = input('請輸入身高: ')
weight = input('請輸入體重: ')
height = float(height)
weight = float(weight)

height_m = height / 100		# 將身高單位公分轉換為公尺
bmi = weight / height_m ** 2	# 計算BMI的公式
print('BMI =',bmi)

# 顯示BMI是否為正常值
if bmi < 18.5:
	print('體重過輕！')
elif bmi >= 18.5 and bmi < 24:
	print('正常範圍')
elif bmi >= 24 and bmi < 27:
	print('體重過重！')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖！')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖！')
elif bmi >= 35:
	print('重度肥胖！')
else:
	print('***例外錯誤***')