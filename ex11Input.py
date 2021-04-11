print("How old are you?", end = ' ') # first question
age = input() # this is the answer from the user
print("How tall are you?" , end = ' ') #second question
height = input()
print("How much so you wheigh" , end = ' ') # the end = ' ' tells print not to end the line with a newline character and go to the next line
weight = input() 
print(f"So, you're {age} old, {height} tall and {weight} heavy")
