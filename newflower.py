import myclass
def func(): #this function is for getting inputs and appending in list
 
    for i in range(0,23,1):
	 
         x=input('Enter name of flower:')
         y=input('Enter color of flower:')
         z=input('Enter season of flower:')
         for i in range (0,2):
             print('\n')
         print('Thankyou for the inputs!')
         flo=swap.flower(x,y,z)
         print('New Output is\n',flo.name,"--", flo.color, "--",flo.season)
        
func()
        