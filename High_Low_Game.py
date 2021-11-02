low=1
high=1000

print("please think a number between {0} and {1}".format(low,high))
input("press ENTER  to start")

guesses=1
while True:
    print("\tguessing in the range {0} and {1}".format(low,high))
    guess=low+(high-low)//2
    high_low=input("my guess is {}. should i guess higher or lower?"
                   "enter h or l,or c if my guess was correct"
                   .format(guess)).casefold()
    if high_low=="h":
        low=guess+1
    elif high_low=="l":
        high=guess-1
    elif high_low=="c":
        print("i got it in {} guesses".format(guesses))
        break
    else:
        print("please enter h,l or c")
    guesses += 1
