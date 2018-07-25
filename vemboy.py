'''


                                            SURVEY



print(" ")
print("Today i'm going to find out what color socks you're wearing")

point_bank = 0

question_1 = input("What's the best form of Economy?: 1) Capitalism 2) Communism 3) No economy ")

question_2 = input("What's the best social media?: 1) Twitter 2) Youtube 3) ID_techcamp ")

question_3 = input("What's the best ice cream?: 1) Vanilla 2) Choco 3) Rainbow ")

questions = []

questions.extend((question_1, question_2, question_3))

print(questions)

x = 0

while(x < 3):
    if(questions[x] == "1"):
        point_bank += 1
    elif(questions[x] == "2"):
        point_bank += 2
    elif(questions[x] == "3"):
        point_bank += 3
    x += 1

if(point_bank >= 3 and point_bank < 5):
    print("You are wearing white socks")
elif(point_bank > 5 and point_bank <= 7):
    print("You are wearing red socks")
elif(point_bank > 7):
    print("You are wearing funky blue socks")
'''



'''


                                    RANDOM PERSON



import random
import string

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

minds = ['Tired','Energetic']

ages = []
ID = []
state_of_mind = []

for x in range(10):
    ages.append(random.randint(1, 60))
    ID.append(id_generator())
    state_of_mind.append(random.choice(minds))

rn = random.randint(0,10)
class Person:
    def __init__(self):
        self.name = ID[rn]
        self.age = ages[rn]
        self.mind = state_of_mind[rn]




a = Person()
print("My name is: " + str(a.name))
print("My age is: " + str(a.age))
print("I am very: " + a.mind)
activity = ""
if (a.mind == 'Tired'):
    activity = "Sit on the couch"
elif (a.mind == 'Energetic'):
    activity = "Do laps in the pool"
print(activity)
'''


'''


                                        STAR TABLE


height = int(input("Number please: "))
width = int(input("Number please: "))


symbol = "*"

x = 0
y = 0
while(x < height):
    while(y < width):
        print(symbol, end='')
        y += 1
    print("\n")
    y = 0
    x += 1
'''


'''


                                        HIGH OR LOW GAME



x = 0

number = int(input("Tell me a number or ill slit your throat: "))

guess = int(input("Guess the number right or your family dies: "))

while(x == 0):
    if(guess == number):
        print("Wait what... you guessed right?!")
        x = 1
    elif(guess < number):
        print("The numbers bigger dumb dumb, now your families dead... ")
        guess = input("Guess the number right or your family dies: ")
    elif(guess > number):
        print("Smaller like yours, feelsbadman")
        guess = input("Guess the number right or your family dies: ")


'''



'''

                                      #  fibonacci position number



fib_list = [0,1]

x = 0

while(x < 100):

    real_num = fib_list[-1] + fib_list[-2]
    fib_list.append(real_num)
    x += 1

pos = int(input("Hey, which position number do you want to find :D?: "))

print("Here you go!: " + str(fib_list[pos]))

print(fib_list)

'''


'''



                                            FACTORIAL <3



def function_factorial(number):
    sum = number
    x = 0
    while(x < number):
        number -= 1
        sum = sum * number
        x += 1
    print(sum)



function_factorial(int(input("Give me a number!: ")))
'''


'''


                        recursion FIB


def function_factorial(number):
    if number < 1:
        return 1
    else:
        returnNumber = number * function_factorial(number - 1)
        print(str(number) + '!= ' + str(returnNumber))
        return returnNumber

function_factorial(int(input("Give me a number!: ")))

'''

