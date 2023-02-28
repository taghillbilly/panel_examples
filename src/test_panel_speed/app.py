#!/usr/bin/env python
# coding: utf-8

# In[1]:


##%%px
from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[2]:


import pandas as pd
import numpy as np
import panel as pn
pn.extension('tabulator')
import hvplot.pandas
import holoviews as hv
import time
from bokeh.models import HoverTool, Legend


# In[3]:


# if 'data' in pn.state.cache.keys():
#     del pn.state.cache['data_test_panel_speed']


# In[4]:


# data source: reudced set of https://www.kaggle.com/datasets/thedevastator/adult-language-learning-profile


# In[5]:


# cache data to improve dashboard performance
if 'data_test_panel_speed' not in pn.state.cache.keys():

    # df = pd.read_csv('./data/stex.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/taghillbilly/adult-language-learning-profile/main/data/stex.csv')
    
    pn.state.cache['data_test_panel_speed'] = df.copy()

else: 

    df = pn.state.cache['data_test_panel_speed']


# In[6]:


lst_slider = []
lst_checkbox = []
lst_toggle_group = ['L1','C','L2','Family','Edu.day']


# In[7]:


dict_sliders = {}

lst_widget_slider = []
for item in lst_slider:
    print(item)
    widget = pn.widgets.DiscreteSlider(name=item, options=sorted(list(set(df[item]))), value = list(set(df[item])[0]),width=150)
    #display(widget)
    lst_widget_slider.append(widget)
    dict_sliders[item] = widget

lst_widget_checkbox = []
for item in lst_checkbox:
    print(item)
    widget = pn.widgets.CheckBoxGroup(name=item+' checkbox',  options=sorted(list(set(df[item]))), value = list(set(df[item])), inline=True)
    #display(widget)
    lst_widget_slider.append(widget)
    dict_sliders[item] = widget
    
lst_widget_toggle_group = []
for item in lst_toggle_group:
    print(item)
    widget = pn.widgets.ToggleGroup(name=item + ' togglegroup', options = sorted(list(set(df[item]))), value = list(set(df[item])), button_type='success')
    #display(widget)
    lst_widget_toggle_group.append(widget)
    dict_sliders[item] = widget


# In[8]:


# Make DataFrame Pipeline Interactive
idf = df.interactive()


# In[9]:


execution_string = 'idf_slice =  idf['
for key,value in dict_sliders.items():
    if 'checkbox' in value.name:
        execution_string = execution_string + ' (idf[\"%s\"].isin(dict_sliders[\"%s\"].value))&'%(key,key)
    elif 'togglegroup' in value.name:
        execution_string = execution_string + ' (idf[\"%s\"].isin(dict_sliders[\"%s\"]))&'%(key,key)
    else:
        execution_string = execution_string + ' (idf[\"%s\"] == dict_sliders[\"%s\"])&'%(key,key)
print(execution_string)
print('---------------')
strToReplace = '&'
replacementStr = ''
execution_string = replacementStr.join(execution_string.rsplit(strToReplace, 1))
print(execution_string)
print('---------------')
execution_string = execution_string+']'
print(execution_string)


# In[10]:


#execution_string = "idf_slice =  idf[ (idf[\"L1\"].isin(dict_sliders[\"L1\"]))& (idf[\"C\"].isin(dict_sliders[\"C\"]))& (idf[\"L1L2\"].isin(dict_sliders[\"L1L2\"]))& (idf[\"L2\"].isin(dict_sliders[\"L2\"]))& (idf[\"Family\"].isin(dict_sliders[\"Family\"]))]"


# In[11]:


# list ~10 variables
list_y_var = ['AaA','LoR','new_feat','new_sounds','morph','lex','Enroll','Speaking']


# In[12]:


yaxis = pn.widgets.RadioButtonGroup(
    name='Y axis', 
    options=list_y_var, 
    button_type='success'
)


# In[13]:


start_time = time.time()
exec(execution_string)
lst_groupby = [x for x in dict_sliders.keys()]
lst_groupby = lst_groupby + ['Sex']
pipeline = (idf_slice.groupby(lst_groupby)
    [yaxis].mean().to_frame().reset_index().sort_values(by='Sex').reset_index(drop=True)
)
time_debugging_point_1 = time.time()
print("start to debugging_point_1: --- %s seconds ---" % (time.time() - start_time))

table = pipeline.pipe(pn.widgets.Tabulator, pagination='remote', page_size = 10, sizing_mode='stretch_width')
plot = pipeline.hvplot(x = 'Sex',by=lst_slider+lst_checkbox+lst_toggle_group+['Sex'],                                    y=yaxis,line_width=2, kind='scatter', marker = 'o',                                   frame_width = 450, frame_height = 400, logx=False, grid=True,                                     title="")
#, widget_location='left_top'
time_debugging_point_2 = time.time()
#print("debugging_point_1 to debugging_point_2: --- %s seconds ---" % (time.time() - time_debugging_point_1))

#https://discourse.holoviz.org/t/overlay-plots-with-legend/1172
#noise_plot.opts(legend_position='bottom_right')
# noise_plot.opts(fontsize={'labels': 16})
# 'labels': 14, 'xticks': 6, 'yticks': 12
hover = HoverTool(tooltips=[("data (x,y)", "(@x, @y)")])
TOOLS=[hover,'wheel_zoom','save','reset','box_zoom','pan']
defalt_tools =['box_zoom',hover]
time_debugging_point_3 = time.time()
print("debugging_point_2 to debugging_point_3: --- %s seconds ---" % (time.time() - time_debugging_point_2))
# this plot.ops takes 1 second
plot.opts(tools=["hover"], default_tools=defalt_tools)
time_debugging_point_4 = time.time()
print("debugging_point_3 to debugging_point_4: --- %s seconds ---" % (time.time() - time_debugging_point_3))
#display(plot)
print("Total time: --- %s seconds ---" % (time.time() - start_time))


# In[14]:


#display(plot)


# In[15]:


#Layout using Template
#main = []
#i=0
start_time = time.time()
#for y_var in list_y_var:
    # #for key in dict_sliders:
    # #    main.append(pn.Row(dict_sliders[key]))
    # main.append(pn.Row(pn.Column(lst_plots[i],margin=(0,25))))
    # i = i+1
time_debugging_point_1 = time.time()
print("start to debugging_point_1: --- %s seconds ---" % (time.time() - start_time))

lst_widget_per_row = [pn.Row(pn.Column(key, width=300), dict_sliders[key]) for key in dict_sliders.keys()]

template = pn.template.FastListTemplate(
    title='stex', 
    #sidebar=[dict_sliders[key] for key in dict_sliders],
    #sidebar=pn.Column(*lst_widget_per_row),
    #sidebar_width=700,
    main = [pn.Column(*lst_widget_per_row),
            pn.Row(yaxis),
            pn.Row(pn.Column(plot.panel(),margin=(0,25))), 
            pn.Row(table.panel(),margin=(0,25))
          ],
        #accent_base_color="#88d8b0",
        #header_background="#88d8b0",
)


#display(template)
template.servable()
end_time = time.time()
print("server setup time: %2.1f seconds."%(end_time - time_debugging_point_1))
#pn.Column(plot).servable()

