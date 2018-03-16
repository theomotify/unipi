import collections
import matplotlib.pyplot as plt
import pandas as pd

yearList = []


with open('/Volumes/MacintoshHD/theomotify/Downloads/dblp.xml') as  myfile:
    for line in myfile:
        if "<year>" in line:
            start = line.find('<year>') + 6
            end = line.find('</year>', start)
            yearString = line[start:end]
            yearList.append(yearString)

#just a print ot check everything is ok
print(yearList)

#sorting the list from past to future
yearList.sort()

#from strings to intergers
yearList = list(map(int, yearList))

#printing a dictionary with the year and the times it appears on the xml file
#even thow the list above has been sorted, the year do NOT appear is a past to future manner
#because the sorting now depends on the appearance!!!
print("Counter Start")
countList = collections.Counter(yearList)
print(countList)

#print oreder dictionary byt a Past to Future fashion
#and not the appearance time of each year
print("Counter Sort")
dictList = collections.OrderedDict(sorted(countList.items()))
print(dictList)
print("Counter End")

#plotting from the list...
#plt.bar(range(len(dictList)), list(dictList.values()), align='center')
#plt.xticks(range(len(dictList)), list(dictList.keys()), rotation=90)
#plt.show()

#create series from ordered dictionary for better data manipulation
#and print a bar plot from it

dataframe = pd.Series(dictList, name='value')
dataframe.index.name='Year'
#dataframe.reset_index()
#dataframe.plot()
#dataframe.plot.bar()
#plt.show()

#with dataframe form the series
new_df=pd.DataFrame({'year':dataframe.index, 'values':dataframe.values})
new_df.plot.bar(x='year', y='values')
plt.show()

print("the end")