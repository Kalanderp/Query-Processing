import pandas as pd
df = pd.DataFrame({
    'Name':['Anil Kumar','Ravi Kumar','Priya Sharma','Rahul Kumar']
})
df['Index_Position'] = df['Name'].str.find('Kumar')
print(df)
