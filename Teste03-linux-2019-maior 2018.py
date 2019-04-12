
# coding: utf-8

# windows

# cd D:\Natanael\Fatec\Curso R\Lotofacil 20-05-18

# linux

# cd /media/natanael/Arquivos/Natanael/Fatec/Curso R/Lotofacil 20-05-18

# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


df=pd.read_html('D_LOTFAC.HTM')


# tabela

# tabela.to_excel("D_LOTFAC.xlsx", sheet_name='Sheet1', index=False, engine='xlsxwriter')

# xlsx = pd.ExcelFile('D_LOTFAC.xlsx')
# df = pd.read_excel(xlsx, 'D_LOTFAC')

# apagando linhas vazias

# sns.heatmap(df.corr())

# In[16]:


df


# In[17]:


dfs=df[0]


# dfss=df[1]

# In[18]:


dfs.head()


# dfs.columns['Concurso','Data Sorteio','Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9',
# 'Bola10','Bola11','Bola12','Bola13','Bola14','Bola15','Arrecadacao_Total','Ganhadores_15_Números',
# 'Cidade','UF','Ganhadores_14_Números','Ganhadores_13_Números','Ganhadores_12_Números','Ganhadores_11_Números',
# 'Valor_Rateio_15_Números','Valor_Rateio_14_Números','Valor_Rateio_13_Números','Valor_Rateio_12_Números',
# 'Valor_Rateio_11_Números','Acumulado_15_Números','Estimativa_Premio','Valor_Acumulado_Especial']

# In[25]:


df1=pd.DataFrame(df[0])


# In[26]:


df1.head()


# In[29]:


df1[1]


# In[30]:


df_na1=df1.dropna()


# In[31]:


df_na1.head()


# In[34]:


df2=df_na1[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]


# In[35]:


df2.head()


# In[41]:


df2=df2.drop([0])


# df2.columns['Data Sorteio','Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9',
# 'Bola10','Bola11','Bola12','Bola13','Bola14','Bola15']

# df1=pd.DataFrame(df[0],columns=['Concurso','Data Sorteio','Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9',
# 'Bola10','Bola11','Bola12','Bola13','Bola14','Bola15','Arrecadacao_Total','Ganhadores_15_Números',
# 'Cidade','UF','Ganhadores_14_Números','Ganhadores_13_Números','Ganhadores_12_Números','Ganhadores_11_Números',
# 'Valor_Rateio_15_Números','Valor_Rateio_14_Números','Valor_Rateio_13_Números','Valor_Rateio_12_Números',
# 'Valor_Rateio_11_Números','Acumulado_15_Números','Estimativa_Premio','Valor_Acumulado_Especial'])

# In[42]:


df2.head()


# In[43]:


df2.tail()


# df2=pd.DataFrame(df1,columns=['Concurso','Data Sorteio','Bola1','Bola2','Bola3','Bola4','Bola5','Bola6','Bola7','Bola8','Bola9',
# 'Bola10','Bola11','Bola12','Bola13','Bola14','Bola15','Arrecadacao_Total','Ganhadores_15_Números',
# 'Cidade','UF','Ganhadores_14_Números','Ganhadores_13_Números','Ganhadores_12_Números','Ganhadores_11_Números',
# 'Valor_Rateio_15_Números','Valor_Rateio_14_Números','Valor_Rateio_13_Números','Valor_Rateio_12_Números',
# 'Valor_Rateio_11_Números','Acumulado_15_Números','Estimativa_Premio','Valor_Acumulado_Especial'])

# df_na[1] = pd.to_datetime(df_na[1])

# In[46]:


df2[1] = pd.to_datetime(df2[1])


# In[47]:


df2.head(5)


# In[50]:


df2[df2[1]>='2018']


# In[53]:


df2=df2[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]


# In[54]:


contados=pd.value_counts(df2.values.flatten())


# In[55]:


contados


# In[56]:


figura_resultado=contados.plot.bar()


# In[58]:


fig = plt.figure()
fig=figura_resultado.get_figure()
contados.to_excel("resultado_maior_2018.xlsx", sheet_name='Sheet1')
contados.to_string("resultado_maior_2018.txt")
fig.savefig('figura_resultado_2018.png')

