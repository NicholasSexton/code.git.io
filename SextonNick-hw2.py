### Nick_Sexton HW_2



# README:
#  * Edit this file where noted to complete exercises.
#  * DO NOT change function names or your code will not pass test cases.
#  * Output must match the reference solution's output EXACTLY, examples of
#    reference solution output will be provided throughout the document.

# Exercise 2-6
# PROMPT(S) (Example user input of '100'):
'''
Enter the amount of the purchase: 100
'''
# OUTPUT:
'''
Purchase Amount: 100.00
State Tax: 5.00
County Tax: 2.50
Total Tax: 7.50
Sale Total: 107.50
'''
def sales_tax():
    # your code here
	amount_p = float(input("Enter the amount of purchase: "))
	ctax = .025
	stax = .05
	dollar_stax = format(float(amount_p) * float(stax), ".2f")
	dollar_ctax = format(float(amount_p) * float(ctax), ".2f")
	total_tax = format(float(dollar_ctax) + float(dollar_stax), ".2f")
	sale_total = format(float(amount_p) + float(total_tax), ".2f")

	print("Purchase Amount: " + str(amount_p))
	print("State Tax: " + str(dollar_stax))
	print("County Tax: " + str(dollar_ctax))
	print("Total Tax: " + str(total_tax))
	print("Sale Total: " + str(sale_total))

# Exercise 2-14
# PROMPT(S) (Example user input of '100', '5', '12', and '10'):
'''
Enter the starting principal: 100
Enter the annual interest rate: 5
How many times per year is the interest compounded? 12
For how many years will the account earn interest? 10
'''
# OUTPUT:
'''
At the end of 10 years you will have $ 164.70
'''
def compound_interest():
	# your code here
	principle = float(input("Enter the starting principal: "))
	apr = float(input("Enter the annual interest rate: "))
	cpy = float(input("How many times per year is the interest compounded? "))
	n_years = float(input("For how many years will the account earn interest? "))

	cash = format(principle * (1 + (apr / cpy)) ** n_years * cpy, ".2f")
	print("At the end of " + str(n_years) + " years you will have $ " + str(cash))


# Exercise 3-10
# PROMPT(S) (Example user input of '100', '5', '10', and '4'):
'''
Enter the number of pennies: 100
Enter the number of nickels: 5
Enter the number of dimes: 10
Enter the number of quarters: 4
'''
# OUTPUT (Less than one dollar):
'''
Sorry, the amount you entered was less than one dollar.
'''
# OUTPUT (More than one dollar):
'''
Sorry, the amount you entered was more than one dollar.
'''
# OUTPUT (Exactly one dollar):
'''
Congratulations!
The amount you entered was exactly one dollar!
You win the game!
'''
def dollar_game():
	# your code here
	p_in = int(input("Enter the number of pennies: "))
	n_in = int(input("Enter the number of nickels: ")) * 5
	d_in = int(input("Enter the number of dimes: ")) * 10
	q_in = int(input("Enter the number of quarters: ")) * 25

	if p_in + n_in + d_in + q_in == 100 : 
		print('''Congratulations! 
The amount you entered was exactly one dollar!
You win the game!''')
	elif p_in + n_in + d_in + q_in > 100 :
		print("Sorry, the amount you entered was more than one dollar.")
	elif p_in + n_in + d_in + q_in < 100 : 
		print("Sorry, the amount you entered was less than one dollar.")
# Exercise 3-12
# PROMPT(S) (Example user input of '10'):
'''
Enter the number of packages purchased: 10
'''
# OUTPUT:
'''
Discount Amount: $ 99.00
Total Amount: $ 891.00
'''
def quantity_discount():
	# your code here
	soft = 99
	software_purchase = float(input("Enter the number of packages purchased: "))

	if software_purchase < 10 :
		software_discount = 0
	elif software_purchase >= 10 and software_purchase < 20 :
		software_discount = .10
	elif software_purchase >= 20 and software_purchase < 50 :
		software_discount = .20
	elif software_purchase >= 50 and software_purchase < 100 :
		software_discount = .30
	elif software_purchase >= 100 :
		software_discount = .40

	dollar_discount = soft * software_purchase * software_discount
	soft_total = (soft * software_purchase) - dollar_discount

	print("Discount Amount: $ " + str(format(dollar_discount, ".2f")))
	print("Total Amount: $ " + str(format(soft_total, ".2f")))

# Exercise 3-13
# PROMPT(S) (Example user input of '10'):
'''
Enter the weight of the package: 10
'''
# OUTPUT:
'''
Shipping charge: $ 4.00
'''
def shipping_charge():
	# your code here
	p_weight = float(input("Enter the weight of the package: "))
	
	if p_weight <= 2 :
		ship_fee = 1.50
	elif p_weight > 2 and p_weight <= 6 :
		ship_fee = 3.00
	elif p_weight > 6 and p_weight <= 10 :
		ship_fee = 4.00
	elif p_weight > 10 :
		ship_fee = 4.75

	print("Shipping charge: $ " + str(format(ship_fee, ".2f")))

# Exercise 4-3
# PROMPT(S) (Example user input of '10', '5', and '0'):
'''
Enter amount budgeted for the month: 10
Enter an amount spent(0 to quit): 5
Enter an amount spent(0 to quit): 0
'''
# OUTPUT (Under budget):
'''
Budgeted: $ 10.00
Spent: $ 5.00
You are $ 5.00 under budget. WELL DONE!
'''
# OUTPUT (Matching budget):
'''
Budgeted: $ 10.00
Spent: $ 10.00
Spending matches budget. GOOD PLANNING!
'''
# OUTPUT (Over budget):
'''
Budgeted: $ 10.00
Spent: $ 15.00
You are $ 5.00 over budget. PLAN BETTER NEXT TIME!
'''
def budget_analysis():
	# your code here
	bud = float(input("Enter amount budgeted for the month: "))
	bud_spent = float(input("Enter an amount spent(0 to quit): "))
	total_spent = bud_spent

	while bud_spent != 0 :
		bud_spent = float(input("Enter an amount spent(0 to quit): "))
		total_spent += bud_spent 

	if total_spent == bud :
		print("Budgeted: $ " + str(format(float(bud), ".2f")))
		print("Spent: $ " + str(format(float(total_spent), ".2f")))
		print("Spending matches budget. GOOD PLANNING!")
	elif total_spent > bud :
		print("Budgeted: $ " + str(format(float(bud), ".2f")))
		print("Spent: $ " + str(format(float(total_spent), ".2f")))
		overbud = format(total_spent - bud, ".2f")
		print("You are $ " + str(overbud) + " over budget. PLAN BETTER NEXT TIME!")
	elif total_spent < bud :
		print("Budgeted: $ " + str(format(float(bud), ".2f")))
		print("Spent: $ " + str(format(float(total_spent), ".2f")))
		underbud = format(bud - total_spent, ".2f")
		print("You are $ " + str(underbud) + " under budget. WELL DONE!")
# Exercise 4-5
# PROMPT(S) (Example user input of '1', '1', '2', '3', '4', '5', '6', '7',
# 	'8', '9', '10', '11', '12'):
'''
Enter the number of years: 1
For year  1 :
Enter the rainfall amount for the month: 1
Enter the rainfall amount for the month: 2
Enter the rainfall amount for the month: 3
Enter the rainfall amount for the month: 4
Enter the rainfall amount for the month: 5
Enter the rainfall amount for the month: 6
Enter the rainfall amount for the month: 7
Enter the rainfall amount for the month: 8
Enter the rainfall amount for the month: 9
Enter the rainfall amount for the month: 10
Enter the rainfall amount for the month: 11
Enter the rainfall amount for the month: 12
'''
# OUTPUT:
'''
For  12 months
Total rainfall:  78.00 inches
Average monthly rainfall:  6.50 inches
'''
def average_rainfall():
	# your code here
	num_year = int(input("Enter the number of years: "))
	#month_rain = int(input("Enter the rainfall amount for the month: "))
	total_rain = float(0)
	first_year = int(1)
	for i in range(first_year, (num_year + 1)) :
		print("For year  " + str(i) + " :")
		for j in range(1,13) :
			month_rain = float(input("Enter the rainfall amount for the month: "))
			total_rain = total_rain + month_rain
		first_year += 1

	total_months = num_year * 12
	avg_rain = total_rain / total_months

	total_rain = format(float(total_rain),'.2f')
	avg_rain = format(float(avg_rain),'.2f')


	print("For  " + str(total_months) + " months")
	print("Total rainfall:  " + str(total_rain) + " inches")
	print("Average monthly rainfall:  " + str(avg_rain) + " inches")


# Exercise 4-12
# PROMPT(S) (Example user input of '10'):
'''
Enter a nonnegative integer: 10
'''
# OUTPUT:
'''
The factoral of 10 is 3628800
'''
def factorial():
	# your code here
	#ASK IF NEED IF STATEMENT FOR NEGATIVE INTEGER NUMBER
	user_int = int(input("Enter a nonnegative integer: "))
	fact = 1
	if user_int < 0:
		quit()
	for i in range(1, user_int + 1) :
		fact = i * fact
	print("The factoral of " + str(user_int) + " is " + str(fact))

# Exercise 4-12
# PROMPT(S) (Example user input of 'python'):
'''
Enter the string to be converted to Morse code: python
'''
# OUTPUT:
'''
--.-,--..,..-,..,.--.,---,
'''
def morse_code():
	# your code here
	user_string = input("Enter the string to be converted to Morse code: ")

	code_list = {'A': '.-',     'B': '-...',   'C': '-.-.', 
				'D': '-..',    'E': '.',      'F': '..-.',
				'G': '--.',    'H': '....',   'I': '..',
				'J': '.---',   'K': '-.-',    'L': '.-..',
				'M': '--',     'N': '-.',     'O': '---',
				'P': '.--.',   'Q': '--.-',   'R': '.-.',
				'S': '...',    'T': '-',      'U': '..-',
				'V': '...-',   'W': '.--',    'X': '-..-',
				'Y': '-.--',   'Z': '--..',

				'a': '.-',     'b': '-...',   'c': '-.-.', 
				'd': '-..',    'e': '.',      'f': '..-.',
				'g': '--.',    'h': '....',   'i': '..',
				'j': '.---',   'k': '-.-',    'l': '.-..',
				'm': '--',     'n': '-.',     'o': '---',
				'p': '.--.',   'q': '--.-',   'r': '.-.',
				's': '...',    't': '-',      'u': '..-',
				'v': '...-',   'w': '.--',    'x': '-..-',
				'y': '-.--',   'z': '--..',

				'0': '-----',  '1': '.----',  '2': '..---',
				'3': '...--',  '4': '....-',  '5': '.....',
				'6': '-....',  '7': '--...',  '8': '---..',
				'9': '----.', 

				' ': ' ',      ',': '--..--', '.': '.-.-.-',
				'?': '..--..',}

	for x in user_string:
		if x != " ":
			print(code_list[x] + ",", end="")
		else:
			print(" ", end="")

			print("\n", end="")

# *** DO NOT EDIT BELOW THIS POINT ***
# This part of the file is for testing purposes.
# Your code WILL FAIL the test cases if this is edited.
def main():
	 #run each exercise
	sales_tax()
	compound_interest()
	dollar_game()
	quantity_discount()
	shipping_charge()
	budget_analysis()
	average_rainfall()
	factorial()
	morse_code()

if __name__=="__main__":
	main()