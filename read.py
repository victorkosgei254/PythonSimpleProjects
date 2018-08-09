#this is a python program to read numericals and convert them to words

numbers = {
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	10:"ten",
	0:"."
}

numbers_ten ={

	1:"teen",
	2:"twenty",
	3:"thrity",
	4:"fourty",
	5:"fift",
	6:"sixty",
	7:"seventy",
	8:"eighty",
	9:"ninety",
	
	
}

count_det ={
	0:"hundred",
	1:"thousand",
	2:"million",
	3:"billion",
	4:"trillion",
	5:"zillion"

}

def readNumber(number):
	#getting the length of the number
	
	list_number = list(str(number))
	digits = len(list_number)
	#finding the number of times to be looped through
	counter = int(digits/3)
	#finding the remainder 
	counter2 = digits % 3
	#looping through the counter 2 loop will show thousands, zero hundreds,
	name = []
	name_msb = []
	if digits > 3:
		#perform looping using counters
		count = digits
		count_del = count - 3
		for i in range(0,counter):
			list_check = list_number[count_del:count]
			num_gen = list_check[0]
			for i in range(1,len(list_check)):
				num_gen = num_gen + list_check[i]


			
			name.append(Hundred(int(num_gen)))


			count = count -3
		
			count_del = count_del -3
		if  counter2 == 2:
			#read the two digits
			x = list_number[0] + list_number[1]
			Tens(int(x))
		else:
			#read the one digit
			x = list_number[0]
			Tens(int(x))

		name_msb.insert(0,Tens(int(x)))
	else :
		#call the hundred function
		number_check = number
		Hundred(number_check)
	
	
	# for i in range(0,len(name)):
	# 	message = 
	
	print (name_msb[0]+ " "+count_det[len(name)]+", "+name[len(name)-1] +", " +count_det[len(name)-1]+" "+name[len(name)-2])

def Hundred(number):
	num_list = list(str(number))
	if num_list[1] == '0':
		if num_list[2] == '0':
			messge = (numbers[int(num_list[0])] + " hundred"+ numbers[int(num_list[2])]  )
		else:
			messge = (numbers[int(num_list[0])] + " hundred and "+ numbers[int(num_list[2])]  )
	else :
		if num_list[1] == '1':
			messge = (numbers[int(num_list[0])] + " hundred and "+ numbers[int(num_list[2])]+numbers_ten[int(num_list[1])] )
		else:
			messge = (numbers[int(num_list[0])] + " hundred and "+numbers_ten[int(num_list[1])]+" "+ numbers[int(num_list[2])]  )

	return messge


def Tens(number):
	num_list = list(str(number))
	if len(num_list) > 1:
		if num_list[0] != '0' and num_list[1] != '0':
			message = (numbers_ten[int(num_list[0])]+ " "+numbers[int(num_list[1])])
		elif  num_list[0] == '1' and num_list[1] == '0':
			x = num_list[0]+num_list[1]
			message = (numbers[int(x)])
		else:
			message = (numbers[int(num_list[1])]+numbers_ten[int(num_list[0])])

	else:
		message = (numbers[int(num_list[0])])

	return message



def main():
		state = "ON"
		while (state):
			number = input(">")
			if number != "exit":
				readNumber(number)
			else:
				break;



main()