print "\n\nMY WALLET::1.5 ---- By: Marcos Zlotnik\n\n"
intro = input("PRESS 1 TO CREATE AN ACCOUNT OR PRESS 2 TO SIGN IN: ")
if intro == 1:
        print "\n\nCREATING AN ACCOUNT"
        firstName = raw_input("ENTER YOUR NAME: ")
        firstMoney = raw_input("ENTER THE AMOUNT OF MONEY YOU HAVE: ")
        fileName = open ("name.txt", "w")
        fileName.write(firstName)
        fileName.close()
        fileMoney = open("amount.txt", "w")
        fileMoney.write(firstMoney)
        fileMoney.close()
        print "PLEASE RESTART (My Wallet) to continue"
elif intro == 2:
        print "\n\nSIGN IN"
        fileName = open ("name.txt", "r")
        fileNameVar = fileName.readline()
        fileName.close()
        name = raw_input("ENTER YOUR NAME: ")
        if name == fileNameVar:
                print "\nWELCOME BACK %s" % (name)
                print "\nYOU HAVE "
                fileMoney = open("amount.txt")
                fileMoneyVar = fileMoney.readline()
                fileMoney.close()
                print fileMoneyVar
                updating = input("\nUPDATE: ")
                plusMoney = float(fileMoneyVar) + updating
                print "\nYOU HAVE %s" % (plusMoney)
                fileMoney = open ("amount.txt", "w")
                fileMoney.write(str(plusMoney))
                fileMoney.close()
        else:
                print "ERROR"
else:
        print "ERROR"
