import math
def main():
	print("select the correct option: \n" "1. select 1 for RIV>> start PRB and total PRB conversion \n" "2. select 2 for start PRB and total PRB >> RIV calculation \n" "3. select 3 for SLIV >> start symbol and consecutive number of symbols \n" "4. select 4 for start and consecutive symbols >> SLIV \n ")
	option=int(input("Enter the option: "))
	N_Size_BWP= 275

	def RIV_to_total_RB():
		RIV=int(input("enter the location and bandwidth > "))
		if (((RIV/N_Size_BWP)+(RIV%N_Size_BWP))< N_Size_BWP):
			RBstart= RIV%N_Size_BWP
			Lrb= (RIV/N_Size_BWP) + 1
			print ("the total number of PRB > %r" % math.ceil(Lrb))
			print ("The start PRB is > %r" %RBstart)
		else:
			RBstart=N_Size_BWP-(RIV%N_Size_BWP)-1
			Lrb=N_Size_BWP-(RIV/N_Size_BWP)+1
			print ("the total number of PRB > %r" % math.ceil(Lrb))
			print ("The start PRB is > %r" % RBstart)


	def total_RB_to_RIV():
		RBstart=int(input("enter the RB start: "))
		Lrb=int(input("enter the total PRBs: "))
		if ((Lrb-1)<=(N_Size_BWP/2)):
			RIV=(N_Size_BWP*(Lrb-1)) + RBstart
			print("The location and Banwidth is > %r" % RIV)

		else:
			RIV=N_Size_BWP*(N_Size_BWP-Lrb+1)+(N_Size_BWP-1-RBstart)
			
			print("The location and Banwidth is > %r" % RIV)

	def sliv_to_symbols():
		SLIV=int(input("enter the SLIV "))
		if(int(SLIV / 14) + int(SLIV % 14) < 14):
			consecutive_symbols=int((SLIV/14)+1)
			start_symbol_index=int(SLIV%14)
		else:
			consecutive_symbols=int(14-(SLIV/14)+1)
			start_symbol_index=int(14-(SLIV%14)-1)
		if (0<consecutive_symbols<= 14-start_symbol_index and SLIV<=104):
			print("consecutive number of symbol Length (L) is "f"{consecutive_symbols}")
			print("start symbol index is (S) "f"{start_symbol_index}")
		else:
			print("Invalid Value")


	def symbols_to_sliv():
		start_symbol_index = int(input("Please enter the Start symbol index (S) Value> "))
		consecutive_symbols = int(input("Please enter the consecutive symbol Length (L) Value> "))
		if (0 < consecutive_symbols <= 14-start_symbol_index):
			if consecutive_symbols-1 <=7:
				SLIV = 14*(consecutive_symbols-1)+start_symbol_index
				print ("\nThe SLIV is %r" %SLIV)
				
			else:
				SLIV = 14*(14-consecutive_symbols+1)+(14-1-start_symbol_index)
				print ("\nThe SLIV is %r" %SLIV)
		else:
			print("Invalid Value")







	if (option==1):
		RIV_to_total_RB()
	elif(option==2):
		total_RB_to_RIV()
	elif (option==3):
		SLIV_to_symbols()
	else:
		symbols_to_sliv()


if __name__ == '__main__':  
    main()

repeat=input("Do you want to continue ? Y or N > ").upper()
while (repeat=="Y"):

	if  (repeat=="N"):
		break
	main()
	repeat=input("Do you want to continue ? Y or N > ").upper()



		


