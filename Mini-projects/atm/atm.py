import re



acc_balance = 0
pattern = r"([DW]|[dw])\s?([0-9]+)"

for i in range(2):
	user = input('')
	test = re.findall(pattern, user)
	if (test[0][0] == 'D') or (test[0][0] == 'd'):
		acc_balance +=int(test[0][1])
	elif (test[0][0] == 'W') or (test[0][0] == 'w'):
		acc_balance -=int(test[0][1])
	else:
		print('Invalid action')


print(acc_balance)













# stan konta
#caly program loop/while
#cyfry jako regex 
#D - Deposit, W - Withdraw
