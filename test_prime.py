
from math import sqrt

counter = 0

l = list()

for x in range(1000):

    counter_prev = counter
    counter = 0;

    i = 2
    while(i <= int(sqrt(x)) + 1):
        k=0
        if(x%i==0):
            j=1
            while(j<=i):
                if(i%j==0):
                    k=k+1
                j=j+1
            if(k==2):
                counter += 1
        i=i+1
        
    l.append({x, counter})
        

print (l)       
    