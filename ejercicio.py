import pandas as pd
df=pd.read_csv("C:/Users/didie/Documents/retoAnalitica/arteDeLaAnalitica/avocado_full.csv") 
newyork = df[df['region'] == "NewYork"] 
nysize=len(newyork)
total_value_ny=newyork.sum().iloc[6]
small_bags_ny=newyork.sum().iloc[7]
medium_bags_ny=newyork.sum().iloc[8]
large_bags_ny=newyork.sum().iloc[9]
average_ny=total_value_ny/nysize
porcentaje_small_ny=(small_bags_ny*100)/total_value_ny
porcentaje_medium_ny=(medium_bags_ny*100)/total_value_ny
porcentaje_large_ny=(large_bags_ny*100)/total_value_ny
total_bags_ny=newyork.loc[:,"Total Bags"]
stddeviation_ny=total_bags_ny.std()


cali = df[df['region'] == "California"] 
calisize=len(cali)
total_value_cali=cali.sum().iloc[6]
small_bags_cali=cali.sum().iloc[7]
medium_bags_cali=cali.sum().iloc[8]
large_bags_cali=cali.sum().iloc[9]
average_cali=total_value_cali/calisize
porcentaje_small_cali=(small_bags_cali*100)/total_value_cali
porcentaje_medium_cali=(medium_bags_cali*100)/total_value_cali
porcentaje_large_cali=(large_bags_cali*100)/total_value_cali
total_bags_cali=cali.loc[:,"Total Bags"]
stddeviation_cali=total_bags_cali.std()

charlotte = df[df['region'] == "Charlotte"] 
charlottesize=len(charlotte)
total_value_charlotte=charlotte.sum().iloc[6]
small_bags_charlotte=charlotte.sum().iloc[7]
medium_bags_charlotte=charlotte.sum().iloc[8]
large_bags_charlotte=charlotte.sum().iloc[9]
average_charlotte=total_value_charlotte/charlottesize
porcentaje_small_charlotte=(small_bags_charlotte*100)/total_value_charlotte
porcentaje_medium_charlotte=(medium_bags_charlotte*100)/total_value_charlotte
porcentaje_large_charlotte=(large_bags_charlotte*100)/total_value_charlotte
total_bags_charlotte=charlotte.loc[:,"Total Bags"]
stddeviation_charlotte=total_bags_charlotte.std()

print(f'Produccion Total:\nNew York: {total_value_ny}\nCalifornia: {total_value_cali}\nCharlotte: {total_value_charlotte}\n')
print(f'Promedio:\nNew York: {average_ny}\nCalifornia: {average_cali}\nCharlotte: {average_charlotte}\n')
print(f'Porcentaje Bolsas Chicas:\nNew York: {porcentaje_small_ny}\nCalifornia: {porcentaje_small_cali}\nCharlotte: {porcentaje_small_charlotte}\n')
print(f'Porcentaje Bolsas Medianas:\nNew York: {porcentaje_medium_ny}\nCalifornia: {porcentaje_medium_cali}\nCharlotte: {porcentaje_medium_charlotte}\n')
print(f'Porcentaje Bolsas Grandes:\nNew York: {porcentaje_large_ny}\nCalifornia: {porcentaje_large_cali}\nCharlotte: {porcentaje_large_charlotte}\n')
print(f'Desviacion Estandar:\nNew York: {stddeviation_ny}\nCalifornia: {stddeviation_cali}\nCharlotte: {stddeviation_charlotte}\n')



