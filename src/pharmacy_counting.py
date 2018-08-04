
# coding: utf-8

# In[136]:
import sys
print (sys.argv[1])
print (sys.argv[2])

#path='/Users/mehul_ramani/Downloads'
inputfile= sys.argv[1]
outfile = sys.argv[2]

# In[137]:


import pandas as pd


# In[138]: Reading CSV using pandas library


data = pd.read_csv( inputfile , sep=",")


# In[140]: Group by Function and size is couting num of prescribers


grpd=data.groupby(['drug_name','drug_cost']).size().reset_index(name='num_prescriber')
           


# In[141]: Group by Function and sum is couting total_cost of drug


df = grpd.groupby(['drug_name']).sum().reset_index().sort_values('drug_cost', ascending=False)


# In[142]: Rename drug_cost column to total_cost to meet the requirement


df.rename(index=str,columns = {"drug_cost": "total_cost"}, inplace=True)


# In[143]: Re-ordering column order to before export


df= df[['drug_name','num_prescriber','total_cost']]


# In[144]: Writing final output to text file


df.to_csv( outfile, sep="," , index=False)

