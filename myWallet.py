print "\n\nMY WALLET::1.0 ---- By: Marcos Zlotnik\n\n"
intro = input("PRESS 1 TO CREATE AN ACCOUNT OR PRESS 2 TO SIGN IN: ")
if intro == 1:
	print "\n\nCREATING AN ACCOUNT"
	firstName = raw_input("ENTER YOUR NAME: ")
	firstMoney = input("ENTER THE AMOUNT OF MONEY YOU HAVE: ")
	fileName = open ("name.txt", "w")
	fileName.write(firstName)
	fileName.close()
	fileMoney = open("amount.txt", "w")
	fileMoney.write(firstMoney)
	fileMoney.close()
	print "PLEASE RESTART (My Wallet) to continue"
elif intro == 2:
	print "\n\nSIGN IN"
	name = raw_input("ENTER YOUR NAME: ")
else:
	print "ERROR"
	if name == fileName:
		print "\nWELCOME BACK " + (name)
		print "YOU HAVE "
		fileMoney = open("amount.txt")
		print (fileMoney.readlines())
		fileMoney.close()
		while 3 > 1:
        update = raw_input("\nUPDATE: ")
		    print "YOU HAVE" + (update)
		    getOut = raw_input("GET OUT? ")
		    if getOut == "yes":
		    	break;
		    else:
		    	print "\n"
	else:
		print "ERROR"
