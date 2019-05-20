# Program to display the Fibonacci sequence up to the n-th term where n is provided by the user

# Change this value for a different result
nterms = int(input("Enter a number to calculate up to a max of 100 "))

# uncomment to take input from the user
#nterms = int(input("How many terms?"))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please  enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
        print(n1,end=' , ')
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count = count + 1


    #end of program TREV
