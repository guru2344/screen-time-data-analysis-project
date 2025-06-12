# Screen time analysis project
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as gp
data=pd.read_csv('Screentime2.csv')
# print(data.to_string())
# print(data.isnull().sum())
# print(data.describe())

# to analyze usage of the apps
figure=px.bar(data_frame=data,x="date",y="Usage",color="app",title="Usage Graph")
figure.show()

# # to analyze how many notifications recived
# figure=px.bar(data_frame=data,x="date",y="notification",color="app",title="Notification Graph")
# figure.show()

# # to analyze how many time opened
# figure=px.bar(data_frame=data,x="date",y=" Times open",color="app",title="Graph by guru")
# figure.show()


# figure=px.scatter(data_frame=data,x="notification",y="Usage",size="notification",title="Relationship between no.of notification and amount of usage")
# figure.show()
