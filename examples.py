###
# 9. Writing your own functions
def hello(name):
  print('Howdy ' + name)
  print(name + ' has ' + str(len(name)) + ' letters in it.')

hello('Alice')
hello('Bob')

print('Hi')
print('World')
print('Hello', end='**')
print('World')
print('dog', 'cat', 'mouse', sep='XYZ')

###
# 10. Global and Local scope

def spam():
  eggs=99
  bacon()
  print(eggs)
  
def bacon():
  ham = 101
  eggs = 0

spam()
# print(eggs) # error local scope var

print('Some code here.')
print('some other code.')

###
# 11. Try and except statements

def div42by(divideBy):
  try:
    return 42 / divideBy
  except ZeroDivisionError:
    print('Error. You tried to divide by zero')
  
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


print('How many cats do you have?')
numCats = input()

try:
  if (int(numCats)) >= 4:
    print("That's a great amount of cats")
  else:
    print("That's not too many cats")
except ValueError:
  print('You must enter a number of cats.')
except:
  print('Only positive number of cats, please.')
    
  
#12. writing a "guess your number" program

print('Hello. What is your name?')
name = input()
secretnumber = random.randint(1,20)    
print('Hello ' + name + '. Can you guess a the number that I am thinking ? (Between 1 and 20) ' )

for 

    