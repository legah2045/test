Determining variable type with type()
You can check what type of object is assigned to a variable using Python's built-in type() function. Common data types include:

int (for integer)
float
str (for string)
list
tuple
dict (for dictionary)
set
bool (for Boolean True/False)

Numbers:
print(444+444)
print(444*4)
print(4**4)
print(2+3**2/9)
print((100-90)/(-2-200))

from fractions import Fraction
print(Fraction(10, 30))

print(Fraction(10-7, 30-7))

print(Fraction(17-8, 18+4))


#variables:
x = 5

print(x)

# sloop between 2 points = (y1-y2)/(x1-x2)
x1 = -1
x2 = 7
y1 = 2/7
y2 = -8
 
z = (y1-y2)/(x1-x2)
print('The sloop is equal to:' + str(z))
print(z)


# working with strings

Print("I'M LEARNING PYTHON")

X = cat 
y = dog 
print(x + y)
print(x+" "+y)

z = x+" "+y

print(z)
print(z[0])
print(z[0:3])
print(z[:])
# z[stop,start,step]
print(z[::2])
print('This is python')
print('This\n is \n python') 
print('This\t is \t python')
print(len('This\t is \t python'))

Project List :
Create a Jupyter notebook titled:
 “Project Section 3”.

Define the variable x as a frog and the variable y as a mouse. 
Concatenate these two variables using +,
 then use an index slice to print out only the letters “ous”.

Project Link :

# Dictionary key: value

my_dict = {'key1':'cat','key2':'dog','key3':'fish'}

print(my_dict['key1'])
my_dict['key1']

costs = {'cats':100,'dogs':150,'fishs':200}
print(cost["fish"])

avd = {'k1':17.217, 'k2':'fish','k3':[1,2,3], 'k4':{'inside':'wow!'}}

print(avd['k2'])
print(avd['k3'[2]])
print(avd['k3'][-1])

print(avd['k4']['inside'])


# List
list1 = [0,1,2,3]
print(list1)
list2 = ['cat','fish','dog','frog']
print(list1+list2)
list3 = list1+list2 
list3.append('ant')
list3.pop(1) 

l1 = [25,4,7,9]
l1.sort(reverse = False)
l1.sort()
l2 = ['a', 'g', 'this']
l3 = [1,2,3,4,4]
l4 = l3.copy()
l4.sort(reverse = False)

d = {'k1':5.21,
	'k2':[4,5,7],
	'k3':'cat',
	'k4':'dog',
	'k5':100
}
print(d['k4'])
print(d['k2'][:])


# Print formatting
x=5
print('cat')
print('cat' + x)

print('cat'+ '' +str(x))

print('This boy is {}'.format('awesome'))

print('This boy is {}, {}, {}'.format('cool','awesome','great'))

res = 717/99
print('the answer is {}'.format(res)) 
print('The answer is {r:1.2f}'.format(r = res))


# Files I/O

%%writefile new.txt
This is a text file
Here is another line
More information
new = open('new.txt')
type(new)
print(new.read())
print(new.seek(0))

##
%%writefile new.txt
This is a text file
Here is another line
More information
with open('text') as file2:
    this = file2.readlines()

# r = read, w = write, a = append,
# r+=wr, w+ = writing & reading 

with open('text', mode = 'a') as file2:
    file2.write('\nOur new stuff')  

with open('text', mode = 'r') as file2:
   print(file2.read())  


with open('text', mode = 'w') as guess:
   guess.write('Jesus is Lord')
with open('text', mode = 'r') as guess:
   print(guess.read())   


# Project 5

print{'The Bear ran {} {} {}'.format['through' 'very','quickly']}

print('The Bear ran {} {} {}'.format('through', 'very','quickly'))

section 6 Loading Data

import pandas as pd  # Excel files and csv
import numpy  as np  # maths
import seaborn as sns # useful data

df1 = pd.read_csv('C:/Users/LandmarkTechnology/Desktop/p1/dm1.csv')

df2 = pd.read_excel('C:/Users/LandmarkTechnology/Desktop/p1/dm1.xlsx')

# https:/github.com/mwaskom/seaborn-data
# Great seaborn data sets
df_tips=sns.load_dataset("tips")
df_diamonds=sns.load_dataset("diamonds")

type(df_tips)

===========================
6.2 Creating and transforming data

vehicules = {'type':['cars','suv','bike']
              'cost:['500','800','300']}

df = pd.DataFrame(vehicules, columns = ['types', 'cost'])

df 

df_flip = df.T 

df_flip = df_flip.rename(columns = {
	df_flip.columns[0]:'Option 1',
	df_flip.columns[1]:'Option 2',
	df_flip.columns[2]:'Option 3',
	df_flip.columns[3]:'Option 4',
	df_flip.columns[4]:'Option 5',
	})

df_flip

df_next = df_flip.T 
df_next

df_next = df_next.reset_index()

df_next


df_next = df_next.rename(columns = {
	df_next.columns[0]:'Option 1', })
df_next

25% discount on all options

df_next['sale price'] = df_next['cost'] * 0.75

type(df_next)

df_next['cost'] = df_next['cost'].astype(float)

df_next 

==================================

import pandas as pd  # Excel files and csv
import numpy  as np  # maths
import seaborn as sns # useful data
df_tips=sns.load_dataset("tips")
df_diamonds=sns.load_dataset("diamonds")

df_tips 
df_tips.head()
df_tips.head(3) 
df_tips.tail(3)


tip_by_sex = df_tips.groupby(['sex'])['tip'].mean()
tip_by_sex 
type(tip_by_sex )

tip_by_sex = tip_by_sex.reset_index()
tip_by_sex

tip_by_sex = tip_by_sex.rename(columns = {
	tip_by_sex.columns[1]: 'Average Tip'
	})

tip_by_sex = df_tips.groupby(['sex','smoker'])['tip'].mean()
tip_by_sex 

tip_by_sex = tip_by_sex.reset_index()
tip_by_sex


tip_by_sex = tip_by_sex.rename(columns = {
	tip_by_sex.columns[2]: 'Average Tip'
	})
==============================================
# cross tabulation
df_tips.head()

this = pd.crosstab(columns = df_tips['sex'], 
	index = df_tips['smoker'])
this 

this = pd.crosstab(columns = df_tips['sex'], 
	index = [df_tips['smoker'], 
	df_tips['day'], df_tips['time']])
this

this = pd.crosstab(columns = df_tips['sex'], 
	index = [df_tips['smoker'], 
	df_tips['day'], df_tips['time']]).rename_axis(None, axis=1)
this
===============================================
project 6
df_iris=sns.load_dataset("iris")
df_iris
dd = df_iris.head(3) 
dd = dd.reset_index()




Create a Jupyter notebook titled: “Project Section 6”
Project List :
Create a Jupyter notebook titled: “Project Section 6”.
From the seaborn library, read in the “iris” data frame. Use a transposition to achieve:














Strings
Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

This idea of a sequence is an important one in Python and we will touch upon it later on in the future.

In this lecture we'll learn about the following:

1.) Creating Strings
2.) Printing Strings
3.) String Indexing and Slicing
4.) String Properties
5.) String Methods
6.) Print Formatting
Creating a String
To create a string in Python you need to use either single quotes or double quotes. For example