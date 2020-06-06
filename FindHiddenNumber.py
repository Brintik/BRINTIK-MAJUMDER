#----- GUESS THE HIDDEN NUMBER -----
#BY BRINTIK MAJUMDER

number_of_guess = 9
count = 0
lucky_number = 25
while count <= number_of_guess :
    if count == number_of_guess :
        print("you limit your guessing limit\n\bgame over!\n")
        so = input("If want play again type yes else type no\n>>>\t").lower()
        if so == "yes":
            count = 0
            continue
        elif so == "no":
            break
        else:
            while True:
                so = input("type yes or no\n>>>\t")
                if so == "yes":
                    count = 0
                    break
                elif so == "no":
                    count = 10
                    break

    else:
        guess_number = int(input(print("Guess the number\n>>>\t")))
        print("Checking....\n")
        if guess_number < lucky_number :
            print("Increase the value\n;)\n")
            print("Chances left :\t",(number_of_guess - count-1))
            count = count + 1
            continue

        elif guess_number > lucky_number :
            print("Lower the value\n:p\n")
            print("Chances left :\t",(number_of_guess - count-1))
            count = count+1
            continue

        else:
            print("Wow you got it right boii !\n")
            print("Guesses you made :\t",(count+1))

            so = input("If want play again type yes else type no\n>>>\t").lower()
            if so == "yes":
                count = 0
                continue
            elif so == "no":
                break
            else:
                while True:
                    so = input("type yes or no\n>>>\t")
                    if so == "yes" :
                        count = 0
                        break
                    elif so == "no" :
                        count = 10
                        break
