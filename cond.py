if True: 
	print('Get some sleep')

if False:
	Print('Go to work')

if tired: 
	print('Get some sleep')
else:
	print('Learn python')

if 1>2:
	Print('Thanks')

tired = input('Are you tired? True or False')
if tired: 
	print('Get some sleep')
else:
	print('Learn python')

tired = input('Are you tired? True,  False, Ask Later')
if tired in ('True','t', 'true') : 
	print('Get some sleep')
elif tired == 'Ask Later':
	print('okay bye')

else:
	print('Learn python')


tired = input('Are you tired? True,  False, Ask Later')
if tired in ('True','t', 'true') : 
	print('Get some sleep')
elif tired == ('Ask Later','ask later'):
	print('okay bye')

else:
	print('Learn python')

=================================
modular arithmetic
list1 = [0,1,2,3,4,5,6,7,8,9,10]
tpye(list1)
# number %2 ==o a3%2 == 1 ..6 total with 1 left over

lis2 = ['Even' if x%2 == 0 else 'Odd' for x in list1]


Create a Jupyter notebook titled: “Project Section 7”
Project List :
Create a Jupyter notebook titled: “Project Section 7”.

Create an if/elif/else cell block that allows user input to determine the output.

Project Link :


For Loops


l1 = [0,1,2,3,4,5,6,7,8,9]

for x in l1:
	print(x)

for x in l1:
	print('apples')


for x in l1:
	print(x+2)

for x in l1:
	if x%2==0:
		print(x+2)
	else:
		print('Odd = {}'.format(x))

for x in l1:
	if x % 2 == 0:
		print('Even = {}'.format(2+x))
	else:
		print('Odd = {}'.format(x))

for x in 'apples':
	print(x)


fruits = ['apple','banana','grape','orange']

for x in fruits:
	print(x)
	if x == 'grape'
		break

for x in range(11):
    print(x)
else:
    print('finised counting')

des  = ['red','yellow', 'purple', 'green']


# while loops


Functions

def hello():
    print('welcome')
    print('home')
    print('boy')

def welcome_you(name):
def welcome_you(name = 'Guest'):
    print('welcome home {}'.format(name))


welcome_you('simon') or  welcome_you()

def add_nums(x,y):
	return x+y 

add_nums(4,5)

add_nums(4,5)**2 
==========================

def fancy_math(x,y,z):
	return (x+y) ** z

fancy_math(4,5,3)

==============================
# Only works with numeric values
def num_check(number):
	x = number % 2 
	if x == 0:
		print('Even number')
    else: 
    	print('Odd number')

num_check(7)

==========================
Lambda
doube = lambda x:x*2
print(double(17))
double(17)
type(double)

#or
def  doubleX(x):
	return x*2 

doubleX(17)
==========================
list1 = [0,1,2,3,4,5,6,7,8,9,10]
final_list = list(map(lambda x:x*4, list1))
final_list 

==================================
def even_list_maker(number_list):
	even_nums = []
	for x in number_list: 
		even_nums.append(x*2)
	return even_nums 
even_list_maker(list1)
==================================
project 9 
Create a Jupyter notebook titled: “Project Section 9”
Project List :
Create a Jupyter notebook titled: “Project Section 9”.

Create a lambda function, then a separate def function that both do the following thing. Take variables x, y, and z as input, then return the output value of:

(x / z) + y

Project Link :

==========================

ss = [x,y,z]
list2 = list(map(lambda x:(x/z) + y)
list2 

def nums(x,y,z): 
	return (x / z) + y 

=======================
from import ipywidgets import interact, interactive, fixed
import ipwidgets as widgets 
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

def f(x):
	return x**3
interact(f, x = 10)

interact(f, x = True)

interact(f, x = False)
======================
@interact(x=True, y = 7.0)

def h(x,y):
	return (x,y*3)
=============================
interact(f, x = widgets.IntSlider(min = -20, max = 20, step = 4))
---------------------
# style
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets 
from IPython.display import display

slide = widgets.IntSlider()
display(slide)
slide 
slide.layout.margin = 'auto' 
slide.layout.height = '100px'
------------------------------------
slide1 = widgets.IntSlider(value = 50, min = 5, max = 100, description = 'Better slider')
display(slide1)
slide1.layout.margin = 'auto' 
slide1.layout.height = '100px'
slide1
------------------
# adding styles with color 'blue'
slide1 = widgets.IntSlider(value = 50, min = 5, max = 100, description = 'Better slider')
slide1.style.handle_color = 'Blue'
display(slide1)
slide1.layout.margin = 'auto' 
slide1.layout.height = '100px'
################
widgets.Button(description = "PayNow", button_style = 'info')
widgets.Button(description = "PayNow", button_style = 'success')
widgets.Button(description = "PayNow", button_style = 'warning')
widgets.Button(description = "PayNow", button_style = 'danger')
-------------------------------
# applications of widgets
print(dir(widgets))

slider = widgets.IntSlider()
text = widgets.IntText()
display (slider, text)
-------------------------
bt = widgets.Button(description = 'Meduim')
display(bt) 
def bt_event(obj):
	print('Hello from the {} '.format(obj.description))
bt.on_click(bt_event)
-----------------------
import seaborn as sns 
tips = sns.load_dataset('tips')
tips.head(7)












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


Create a Jupyter notebook titled: “Project Section 2”
Project List :
Create a Jupyter notebook titled: “Project Section 2”. In this notebook, calculate each of the following in its own cell/block:

2+7

19-48

19**2

43/5

(17-8) / (18+4)

Project Link :