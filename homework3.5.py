#start
#at the beginning it printed me the 2 lines for 15 - "fizz" + "fizz fuzz" so i wrote a new progrem:

number: int = int(input("please enter a number:"))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is Fizz Fuzz.")

elif number % 5 == 0:
    print(f"{number} is Fizz.")
elif number % 3 == 0:
    print(f"{number} is Fuzz.")


#end
