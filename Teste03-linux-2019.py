
# coding: utf-8

# windows

# cd D:\Natanael\Fatec\Curso R\Lotofacil 20-05-18

# linux

# cd /media/natanael/Arquivos/Natanael/Fatec/Curso R/Lotofacil 20-05-18

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_html('D_LOTFAC.HTM')


# tabela

# tabela.to_excel("D_LOTFAC.xlsx", sheet_name='Sheet1', index=False, engine='xlsxwriter')

# xlsx = pd.ExcelFile('D_LOTFAC.xlsx')
# df = pd.read_excel(xlsx, 'D_LOTFAC')

# apagando linhas vazias

# sns.heatmap(df.corr())

# In[3]:


df


# In[4]:


dfs=df[0]


# dfss=df[1]

# In[5]:


dfs


# dfs.dropna(inplace=True)

# mostrar tabela

# In[6]:


dfs.head()


# In[7]:


dfs.tail()


# In[8]:


dfs.index


# In[9]:


dfs[16].head()


# In[10]:


dfs[2].head()


# In[11]:


df2=dfs[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]


# In[12]:


df2.head()


# In[13]:


df2.tail()


# df2.drop([0,1]) 

# In[14]:


df2.info()


# In[15]:


df2.shape


# In[16]:


conta=pd.value_counts(df2.values.flatten())


# contar=df2.value_counts()

# In[17]:


conta.head(30)


# print(conta)

# In[18]:


conta=conta.head(40)


# In[19]:


print(conta)


# In[20]:


print(conta.index[0:20])


# In[21]:


print(conta.head(18))


# In[22]:


figura_resultado=conta[:25].plot.bar()


# In[23]:


fig = plt.figure()
fig=figura_resultado.get_figure()
conta.to_excel("resultado1.xlsx", sheet_name='Sheet1')
conta.to_string("resultado1.txt")
fig.savefig('figura_resultado1.png')


# In[24]:


#print(conta)
combinacao= conta.index[0:16]
print(combinacao)
combinacao2=[]
combinacao3=[]
for i in combinacao:
    combinacao2.append(i)
print (combinacao2)
import itertools
result= itertools.combinations(combinacao2, 15)

for i in result:
    combinacao3.append(i)
#combinacao3.to_string('combinacao1.txt')
arq = open('combinacao.txt', 'w')
#arq.writelines(combinacao3)
arq.write(str(combinacao3))
arq.close()


# In[25]:


comb = pd.read_csv('combinacao.txt',sep=" ", header = None)


# In[26]:


comb.head()


# In[27]:


print(comb[0:5])


# sns.heatmap(conta.corr())

# print(df2.corr())

# sns.heatmap(df2.corr())

# In[28]:


df2.head()


# sns.heatmap(df2.corr())

# In[29]:


df2.columns


# In[30]:


df2.index


# type(df[ 1].iloc[1])

# df.drop('Resultado da Lotofácil',axis = 1)

# In[31]:


df.index


# In[32]:


dfs[1].head()


# dfs.drop(df.index[1])

# df.drop(['Unnamed: 1','Resultado da Lotofácil'],axis = 1)

# dfs.drop(['Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32'],axis = 1)

# df.drop(['Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20','Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32'],axis = 1,inplace=True)

# df.head()

# df.drop(['Resultado da Lotofácil','Unnamed: 1'],axis = 1,inplace=True)

# df.head()

# df.rename(columns={" ":"col"},inplace=True)

# df.head()

# Uma função bastante interessante dos DataFrames é o describe(). O describe calcula estatísticas para cada coluna numérica do DataFrame, como contagem de valores, soma, média, mediana, etc

# In[33]:


print(dfs.describe())


# mostra a linha 1

# In[34]:


print(dfs.head(1))


# In[35]:


print(dfs.groupby(2).count())


# In[36]:


from collections import Counter


# contou elementos da primeira linha

# In[37]:


print(Counter(dfs))


# df[['Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15','Unnamed: 16']].plot(figsize=(55, 40), title='lotofacil', grid=True)

# In[38]:


print(dfs.corr())


# sns.heatmap(df.corr())

# In[39]:


contados=dfs[2 and 3].value_counts()


# In[40]:


print (contados)


# contagem dos valores

# In[41]:


contados2=pd.value_counts(dfs.values.flatten())


# In[42]:


print(contados2)


# In[43]:


contados3=pd.value_counts(dfs.values.flatten()).head(26)


# In[44]:


contados3


# contados3.rename(columns={"":"Sorteadas","":"Somatoria"})

# contados3.head()

# In[45]:


contados3.describe()


# contados3.columns = ['numeros', 'total']

# In[46]:


contados3.head(20)


# contados3["numeros"].head()

# plt.plot(contados3)

# In[47]:


figura_resultado=contados3[2:-1].plot.bar()


# In[48]:


fig = plt.figure()
fig=figura_resultado.get_figure()
contados3.to_excel("resultado.xlsx", sheet_name='Sheet1')
contados3[1:].to_string("resultado.txt")
fig.savefig('figura_resultado.png')


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

# In[49]:


dfs.head()


# In[50]:


dfs.index


# In[51]:


dfs.columns


# In[52]:


dfs[1]>'01/01/2018'


# In[61]:


df_na=dfs.dropna()


# In[64]:


df_na[df_na[1]>'2018']


# In[55]:


df3=df_na[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]


# In[56]:


df3.head()


# In[57]:


contados4=pd.value_counts(df3.values.flatten())


# In[58]:


contados4


# In[59]:


figura_resultado=contados4[:-15].plot.bar()


# In[60]:


fig = plt.figure()
fig=figura_resultado.get_figure()
contados4.to_excel("resultado_2018.xlsx", sheet_name='Sheet1')
contados4.to_string("resultado_2018.txt")
fig.savefig('figura_resultado_2018.png')

