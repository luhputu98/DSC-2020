#!/usr/bin/env python
# coding: utf-8

# In[47]:


var_1=[1,2,3,4]


# In[48]:


type(var_1)


# In[11]:


len(var_1)


# In[50]:


first=[11.25, 18.0, 20.0]
second = [10.75, 9.50]
variabelfull=(first+second)
print(variabelfull)


# In[51]:


full_sorted=(sorted(variabelfull))
print(full_sorted)


# In[53]:


area=[11.25,18.0,20.0,10.75,9.50]


# In[55]:


print(area.index(20.0))


# In[56]:


print(area[2])


# In[57]:


print(area.count(14.5))


# In[58]:


area.append(24.5)
area.append(15.45)


# In[59]:


print(area)


# In[61]:


sorted(area,reverse=True)


# In[180]:


print(sorted(area))


# In[64]:


r=float(input("jari-jari lingkaran:"))


# In[65]:


phi=3.14


# In[66]:


keliling=2*phi*r


# In[175]:


print (keliling)


# In[176]:


luas=phi*(r*r)


# In[177]:


print (luas)


# In[166]:


area_3 = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0, "bedroom", 10.75, "bathroom", 10.50, "poolhouse", 24.5, "garage", 15.45]


# In[171]:


del (area_3[10:13])


# In[172]:


print(area_3)


# In[133]:


area_4 = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]


# In[134]:


print(area_4)


# In[135]:


print(area_4[9])


# In[136]:


area_4[9]=10.8


# In[137]:


print(area_4)


# In[138]:


print(area_4.index("living room"))


# In[139]:


area_4[4]="ruang tamu"


# In[140]:


print(area_4)

