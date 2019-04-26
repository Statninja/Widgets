
# coding: utf-8

# **[Ipywidgets](https://https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20Basics.html)**

# In[3]:


import ipywidgets as widgets


# In[4]:


widgets.IntSlider()


# In[5]:


from IPython.display import display
w = widgets.IntSlider()
display(w)


# In[9]:


import ipywidgets as widgets
from IPython.display import display

z = widgets.IntSlider()

display(z)


# In[10]:


widgets.Text(value='Hello World!', disabled=True)


# Linking two similar **widgets** **
# **

# In[11]:


a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))


# In[12]:


b.value

