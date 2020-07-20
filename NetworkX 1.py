#!/usr/bin/env python
# coding: utf-8

# In[1]:


from platform import python_version  #check to see the exact python version you have installed

print(python_version())


# # Intro to NetworkX 

# In[77]:


import networkx as nx       #import networkX


# In[78]:


G = nx.Graph()              #create empty graph (0 nodes 0 vertices)


# In[79]:


G.add_node(1)               #adds new node to the graph
G.add_node(2)
G.add_node(3)


# In[80]:


G.nodes()                   #displays all nodes


# In[81]:


G.add_node(4)


# In[82]:


G.nodes()        


# In[83]:


G.add_edge(1,2)             #adds edges to make connections
G.add_edge(1,3)
G.add_edge(2,3)


# In[84]:


G.edges()                   #displays all edges


# In[85]:


G.add_edge(3,4)


# In[86]:


G.edges()


# In[87]:


G.add_edge('x',6)            #apparently you do not need existing nodes to create edges. adding edges will create new nodes
G.edges()


# In[88]:


import matplotlib.pyplot as plt


# In[89]:


nx.draw(G)                 #show graph


# In[90]:


nx.draw(G, with_labels = 1) #show graph with labeled nodes


# In[41]:


A = nx.complete_graph(5)    #Creates complete graph (all nodes connected to each other) with num of nodes given


# In[42]:


nx.draw(A)


# In[43]:


A.order()                #Print num of nodes


# In[44]:


A.size()                 #Print num of edges


# In[45]:


nx.draw(A, with_labels=True)


# In[48]:


X= nx.complete_graph(20)
nx.draw(X)


# In[59]:


#creates a graph (given num of nodes) with random edges
X = nx.gnp_random_graph(20, 0.2) #20 nodes probability of edge creation 0.2


# In[60]:


nx.draw(X)


# In[99]:


X = nx.gnp_random_graph(20, 0.4)
nx.draw(X)


# In[96]:


X = nx.gnp_random_graph(20, 0.5)
nx.draw(X)


# In[63]:


X = nx.gnp_random_graph(20, 0.8)
nx.draw(X)


# In[ ]:




