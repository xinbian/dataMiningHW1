#use python 2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import scatter_matrix
from pandas.tools.plotting import radviz
from pandas.tools.plotting import andrews_curves
from pandas.tools.plotting import parallel_coordinates
import seaborn as sns


#read data
data=pd.read_csv('iris.data', sep=',', na_values=".",header=None)

#change column names
data.columns=(['sepal length','sepal width','petal length','petal width','irisclass'])

setosa=pd.DataFrame(data, index=range(50), columns=['sepal length','sepal width','petal length','petal width'])
versi=pd.DataFrame(data, index=range(50,100), columns=['sepal length','sepal width','petal length','petal width'])
verginica=pd.DataFrame(data, index=range(100,150), columns=['sepal length','sepal width','petal length','petal width'])

data.plot()
plt.xlabel('index in dataset')
plt.ylabel('with or length (cm)')
plt.savefig('dataplot.eps', format='eps', dpi=600)


#plot histogram
data.plot.hist(bins=40)
#legend(['sepal length','sepal width','petal length','petal width'])
plt.title('Total data histrogram')
plt.xlabel('with or length (cm)')
plt.savefig('datahist.eps', format='eps', dpi=600)


setosaHisto=pd.DataFrame(setosa, columns=['sepal length','sepal width','petal length','petal width'])
setosaHisto.plot.hist(bins=40)
#legend(['sepal length','sepal width','petal length','petal width'])
plt.title('Iris-setosa histrogram')
plt.xlabel('with or length (cm)')
plt.savefig('setohist.eps', format='eps', dpi=600)

versiHisto=pd.DataFrame(versi, columns=['sepal length','sepal width','petal length','petal width'])
versiHisto.plot.hist(bins=40)
plt.title('Iris-versi histrogram')
plt.xlabel('with or length (cm)')
plt.savefig('versihist.eps', format='eps', dpi=600)

verginicaHisto=pd.DataFrame(verginica, columns=['sepal length','sepal width','petal length','petal width'])
verginicaHisto.plot.hist(bins=40)
plt.title('Iris-verginica histrogram')
plt.xlabel('with or length (cm)')
plt.savefig('vergihist.eps', format='eps', dpi=600)
plt.show()

#calculate mean, median
classlist=[data,setosa,versi,verginica]
for i in range(4):
    if i==0:
        print "Statistics of total data"
    if i==1:
        print "Statistics of setosa"
    if i==2:
        print "Statistics of versi"
    if i==3:
        print "Statistics of verginica"
    print "basic info"
    print classlist[i].describe()
    
#calculate mean, median
classlist=[data, setosa,versi,verginica]
for i in range(4):
    if i==0:
        print "Statistics of total data"
    if i==1:
        print "Statistics of setosa"
    if i==2:
        print "Statistics of versi"
    if i==3:
        print "Statistics of verginica"
    print "correlation"
    print classlist[i].corr(method='pearson', min_periods=1)
    
#plot boxplot

data.boxplot()
plt.title('Iris-total data boxplot')
plt.savefig('databox.eps', format='eps', dpi=600)
plt.show()
setosa.boxplot()
plt.title('Iris-setosa boxplot')
plt.savefig('setobox.eps', format='eps', dpi=600)
plt.show()
versi.boxplot()
plt.title('Iris-versi boxplot')
plt.savefig('versibox.eps', format='eps', dpi=600)
plt.show()
verginica.boxplot()
plt.title('Iris-verginica boxplot')
plt.savefig('verginicabox.eps', format='eps', dpi=600)
plt.show()
    
    


andrews_curves(data,'irisclass').legend(bbox_to_anchor=(0.4, 1))
plt.savefig('andrews_curve.eps', format='eps', dpi=600)
radviz(data,'irisclass').legend(bbox_to_anchor=(1.1, 1))
plt.savefig('radviz.eps', format='eps', dpi=600)
plt.show()

parallel_coordinates(data,'irisclass').legend(bbox_to_anchor=(1, 1))
plt.savefig('paracoor.eps', format='eps', dpi=600)
plt.show()

#plot scatter, correlation 
sns.set(style="ticks")
sns.pairplot(data, hue="irisclass")
plt.savefig('scatermatrix.eps', format='eps', dpi=600)
plt.show()


