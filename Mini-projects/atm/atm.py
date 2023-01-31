import re
import os
import time

class Invalid_User_Action(Exception):
	pass


def clearing():
	return os.system('clear')

acc_balance = 0
pattern = r"([DW])\s?([0-9]+)"
stop_atm = False
while stop_atm == False:
	
	user = input('D - Deposit\nW - Withdraw\nHow much:').upper()
	test = re.findall(pattern, user)
	clearing()
	try:	
		if len(test) == 0:
			raise IndexError

		elif (test[0][0] != 'D') and (test[0][0] != 'W'):
			raise Invalid_User_Action

		else:
			if (test[0][0] == 'D'):
				acc_balance +=int(test[0][1])

			elif (test[0][0] == 'W'):
				acc_balance -=int(test[0][1])

	except Invalid_User_Action:
			print('test')
	except IndexError:
		print('Insert action/amount of cash')

	print(f'Account balance:{acc_balance}')
	time.sleep(1)
	stop_atm = bool(int(input('0 - To continue\n1 - To exit\nInsert Number:')))
	clearing()

	