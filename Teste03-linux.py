
# coding: utf-8

# windows

# In[1]:


#cd D:\Natanael\Fatec\Curso R\Lotofacil 25-05-18


# linux

# cd /media/natanael/Arquivos/Natanael/Fatec/Curso R/Lotofacil 20-05-18

# In[2]:
import sys

# sys.path.insert (0, \users\natanael\anaconda3\lib\site-packages)
sys.path.insert(0, 'c:/users/natanael/anaconda3/lib/site-packages')

from collections import Counter

import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#get_ipython().run_line_magic('matplotlib', 'inline')


# tabela=pd.read_html('D_LOTFAC.HTM')

# tabela

# tabela.to_excel("D_LOTFAC.xlsx", sheet_name='Sheet1', index=False, engine='xlsxwriter')

# In[3]:


xlsx = pd.ExcelFile('D_LOTFAC.xlsx')
df = pd.read_excel(xlsx, 'D_LOTFAC')


# apagando linhas vazias

# In[4]:


df.dropna(inplace=True)


# mostrar tabela

# In[5]:


df.head()


# In[6]:


df.drop('Resultado da Lotofácil',axis = 1)


# In[7]:


df.drop(['Unnamed: 1','Resultado da Lotofácil'],axis = 1)


# In[8]:


df.drop(['Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32'],axis = 1)


# In[9]:


df.drop(['Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32'],axis = 1,inplace=True)


# In[10]:


df.head()


# In[11]:


df.drop(['Resultado da Lotofácil','Unnamed: 1'],axis = 1,inplace=True)


# In[12]:


df.head()


# In[13]:


df.rename(columns={" ":"col"},inplace=True)


# In[14]:


df.head()


# Uma função bastante interessante dos DataFrames é o describe(). O describe calcula estatísticas para cada coluna numérica do DataFrame, como contagem de valores, soma, média, mediana, etc

# In[15]:


print(df.describe())

# mostra a linha 1

# In[16]:


print(df.head(1))


# In[17]:


print(df.groupby('Unnamed: 2').count())


# In[18]:


from collections import Counter


# contou elementos da primeira linha

# In[19]:


print(Counter(df))


# df[['Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15','Unnamed: 16']].plot(figsize=(55, 40), title='lotofacil', grid=True)

# In[20]:


print(df.corr())


# In[21]:


contados=df['Unnamed: 2'and'Unnamed: 3'].value_counts()


# In[22]:


print (contados)


# contagem dos valores

# In[23]:


contados2=pd.value_counts(df.values.flatten())


# In[24]:


print(contados2)


# In[25]:


contados3=pd.value_counts(df.values.flatten()).head(25)


# In[26]:


#contados3


# contados3.rename(columns={"":"Sorteadas","":"Somatoria"})

# contados3.head()

# In[29]:


contados3.describe()


# plt.plot(contados3)

# In[34]:


figura_resultado=contados3.plot.bar()


# In[42]:


fig = plt.figure()
fig=figura_resultado.get_figure()
contados3.to_excel("resultado.xlsx", sheet_name='Sheet1')
fig.savefig('figura_resultado.png')

print ('concluidos')
# In[35]:





# sns.pairplot(contados3)

# sns.distplot(contados3)

# plt.scatter(contados3)

# fig,axes=plt.subplots(figsize=(8,10))
# axes.plot(contados3,'r-',label='x^2')
# 
# axes.set_title('Titulo')
# axes.legend()

# fig, axes = plt.subplots(figsize=(12,3))
# axes.bar(contados3)
# axes.set_title("bar")

# contados3.plot(figsize=(55, 40), title='lotofacil')
