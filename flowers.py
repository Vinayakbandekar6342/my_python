a={'name' : ['lotus','sunflower'], 'colour':['pink','orange'] ,'season': ['All','summer']} #predefined dictionary

for i in range (0,2):
      print('\n')

print(a)

for i in range (0,2):
      print('\n')	


def func(): #this function is for getting inputs and appending in list
 
 for i in range(0,23,1):
	 
     x=input('Enter name of flower:')
     y=input('Enter colour of flower:')
     z=input('Enter season of flower:')
     for i in range (0,2):
         print('\n')
     print('Thankyou for the inputs!')

	#add in list
     a['name'].append(x)
     a['colour'].append(y)
     a['season'].append(z)
     
     print('New Output is\n',a)
	#print(a)
     n=input('\n Do you want to add more flowers ?[y/n]\n')
     while n:   #this will ensure even if there is an invalid input the loop will run and ask to give a valid input
         if n=='y':
             func()
         if n=='n':
             print('Thankyou for using the program, Bye!!')
             exit()
             
         else:
             print('Please provide valid input')
             n=input('Do you want to add more flowers ?[y/n]\n')
func()
