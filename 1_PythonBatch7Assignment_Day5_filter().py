#!/usr/bin/env python
# coding: utf-8

# In[6]:


#program to filter Prime Numbers from 1-2500 using filter()

def isPrime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True

fltr=filter(isPrime, range(1,2500))
print ('Prime numbers between 1-10:', list(fltr))


# In[ ]:




