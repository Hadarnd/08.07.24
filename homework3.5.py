#start

number: int = int(input("please type a number:"))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is Fizz Fuzz.")

elif number % 5 == 0:
    print(f"{number} is Fizz.")
elif number % 3 == 0:
    print(f"{number} is Fuzz.")


#end
