from csp import CSP

import time

import pandas
import seaborn as sns
import matplotlib.pyplot as plt


N = [4,8,10,12,15]
backtrackingTimes = []
backtrackingStates = []
forwardChekingTimes = []
forwardChekingStates = []
for n in N:
    #Backtracking
    csp = CSP(n)
    now = time.time()
    backtrackingStates.append(csp.backtracking())
    backtrackingTimes.append(round(time.time() - now, 8))

    #Forward Checking
    csp = CSP(n)
    now = time.time()
    forwardChekingStates.append(csp.forwardChecking())
    forwardChekingTimes.append(round(time.time() - now, 8))
print("Backtracking")
print(backtrackingStates)
print(backtrackingTimes, "\n")

print("Forward Checking")
print(forwardChekingStates)
print(forwardChekingTimes)


statesData = pandas.DataFrame(columns=['algorithm','states'])
timesData = pandas.DataFrame(columns=['algorithm','time'])
for i in range(5):
    statesData=statesData.append(pandas.Series(['Backtracking',backtrackingStates[i]],index=['algorithm','states']),ignore_index=True)
    statesData=statesData.append(pandas.Series(['Forward_Checking',forwardChekingStates[i]],index=['algorithm','states']),ignore_index=True)
    timesData=timesData.append(pandas.Series(['Backtracking',backtrackingTimes[i]],index=['algorithm','time']),ignore_index=True)
    timesData=timesData.append(pandas.Series(['Forward_Checking',forwardChekingTimes[i]],index=['algorithm','time']),ignore_index=True)

print(timesData)

fig,axes = plt.subplots(1,2)

sns.boxplot(ax=axes[0],data=statesData,x='algorithm',y='states')
sns.boxplot(ax=axes[1],data=timesData,x='algorithm',y='time')


plt.show()