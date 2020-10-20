import myclass

#a = {'name' : ['lotus','sunflower'],'color':['pink','orange',],'season':['all','summer']}
#print(a)
a=[]

f=open('flowers.txt','w+',encoding='utf-8')


def fun(): #this function is for getting inputs and appending in list
    

    for i in range(0,23,1):
	 
        x = input('Enter name of flower:')
        f.write('Enter name of flower:%s\n'%x)
        y = input('Enter color of flower:')
        f.write('Enter color of flower:%s\n'%y)
        z = input('Enter season of flower:')
        f.write('Enter season of flower:%s\n'%z)
        for i in range (0,1):
            print('\n')
        print('Thank you for the inputs!')
        f.write('Thank you for the inputs!')
        flo = myclass.flower(x,y,z)
        print([flo.name],"--", [flo.color],"--", [flo.season])
        p=(flo.name +' is a flower. It has '+flo.color+' color. It blooms in '+flo.season+' season.')
        print(p)
        f.write('%s'%p)
    

        for i in range(0,1):
            print('\n')
            
        #a['name'].append(flo.name)
        #a['color'].append(flo.color)
        #a['season'].append(flo.season)
        a.append(flo.show())
        
        print('New Output is\n')
        print(a)
        
        for i in range(0,1):
        
        
            print('\n')
            
        s = input('Do you want to add more flower?[y/n]\n')
        if s == 'y':
            fun()
            
        else:
            print('Thank You')
            exit()
            
        
fun()
