from sklearn.model_selection import train_test_split
from NJCleaner import NJCleaner
from DecisionTreeClassifier  import DecisionTreeClassifier
import pandas as pd
from sklearn.metrics import accuracy_score


nj = NJCleaner('./2018_03.csv')
nj.prep_df()


col_name = ['stop_sequence' , 'from_id' , 'to_id' , 'status' , 'line' , 'type' , 'day', 'part_of_the_day' , 'delay']
data = pd.read_csv('./data/NJ.csv',skiprows=1, header=None, names=col_name)


X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.2, random_state=41)


classifier = DecisionTreeClassifier(min_samples_split=2, max_depth=4)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))

#1  min_samples_split=1, max_depth=1 --> accuracy: 0.7773333333333333
#2  min_samples_split=1, max_depth=2 --> accuracy: 0.7823333333333333
#3  min_samples_split=1, max_depth=3 --> accuracy: 0.7839166666666667
#4  min_samples_split=1, max_depth=4 --> accuracy: 0.7849166666666667
#5  min_samples_split=2, max_depth=1 --> accuracy: 0.7773333333333333
#6  min_samples_split=2, max_depth=2 --> accuracy: 0.7823333333333333
#7  min_samples_split=2, max_depth=3 --> accuracy: 0.7839166666666667
#8  min_samples_split=2, max_depth=4 --> accuracy: 0.7849166666666667
#9  min_samples_split=3, max_depth=1 --> accuracy: 0.7773333333333333
#10 min_samples_split=3, max_depth=2 --> accuracy: 0.7823333333333333

#Elég sok próbálkozásra volt szükségem magasabb pontosság elérése érdekében.
#NJCleaner megírása könnyen ment.
#Órán nagyjából megértettem, hogy mit is kell csinálni, de itthon nehézségekbe ütköztem a pip-el.  
#A lefuttatott legjobb eredmény, elérte a 0,7849 pontosságot.

