import pandas
from data_analisis import calculate_stadistics, time_bloxplot, plot_h_variaton

df = pandas.read_csv('tp5-busquedas-locales/4Q-results.csv')
df2 = pandas.read_csv('tp5-busquedas-locales/8Q-results.csv')
df3 = pandas.read_csv('tp5-busquedas-locales/10Q-results.csv')



calculate_stadistics(df,'hillClimbing',4)
calculate_stadistics(df2,'hillClimbing',8)
calculate_stadistics(df3,'hillClimbing',10)
print("------------------------------------------------")
calculate_stadistics(df,'simulatedAnnealing',4)
calculate_stadistics(df2,'simulatedAnnealing',8)
calculate_stadistics(df3,'simulatedAnnealing',10)
print("------------------------------------------------")
calculate_stadistics(df,'genetic',4)
calculate_stadistics(df2,'genetic',8)
calculate_stadistics(df3,'genetic',10)


time_bloxplot(df)
time_bloxplot(df2)
time_bloxplot(df3)

plot_h_variaton(4)
plot_h_variaton(8)
plot_h_variaton(10)