# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:39:21 2020

@author: jlms3
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

df = pd.read_excel("A01745419_comidas.xlsx")

#Variables X y y
features =["Carbohidratos (g)", "Lípidos (g)","Proteína (g)","Sodio (mg)"]

X = df[features]

features_sinsodio =["Carbohidratos (g)", "Lípidos (g)","Proteína (g)"]
X_sinsodio =df[features_sinsodio]

# extraemos mpg como nuestra variable dependiente
y = df["Calorias (kcal)"]   

# con machine learning


# separamos nuestra data dos partes para entrenar y para hacer el test.
X_train,X_test,y_train,y_test = train_test_split(X_sinsodio,y,test_size=.3,random_state=0)

model = LinearRegression()  # inciamos el modelo de LinearRegression
model.fit(X_train,y_train)  # entrenamos el modelo con lo obtenido anteriormente

predictions = model.predict(X_test)

# mostramos el puntaje del entrenamiento
print('Puntaje entrenamiento: {}\n'.format(model.score(X_train,y_train)))
print('Puntaje Test: {}\n'.format(model.score(X_test,y_test)))
print('Exactitud modelo: {}\n'.format(r2_score(y_test,predictions)))
print(model.intercept_, model.coef_) 
print('MAE',mean_absolute_error(y_test, predictions))
print('MSE',mean_squared_error(y_test, predictions))


#Una vez optimizado el modelo podemos usar toda la base de datos
model.fit(X,y)
print('MAE',mean_absolute_error(y, model.predict(X)))

def plot(X,y,model):
    
    y_pred = model.predict(X)
    data = pd.DataFrame({'cal actual':y,
                        'cal predecidas':y_pred})
    plt.figure(figsize=(12,8))
    plt.scatter(data.index,data['cal actual'].values,label='cal actual')
    plt.scatter(data.index,data['cal predecidas'].values,label='cal predecidas')
    plt.title('',
             fontsize=16)
    plt.xlabel('')
    plt.ylabel('')
    plt.legend(loc='best')
    plt.show()
    
plot(X,y,model)



#OLS statsmodel
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

X = sm.add_constant(X)
model = sm.OLS(y, X_sinsodio)
results = model.fit()
print(results.summary())
results.mse_resid

def plot2(y,results):
    
    y_pred = results.predict()
    data = pd.DataFrame({'cal actual':y,
                        'cal predecidas':y_pred})
    plt.figure(figsize=(12,8))
    plt.scatter(data.index,data['cal actual'].values,label='cal actual')
    plt.scatter(data.index,data['cal predecidas'].values,label='cal predecidas')
    plt.title('',
             fontsize=16)
    plt.xlabel('')
    plt.ylabel('')
    plt.legend(loc='best')
    plt.show()

plot2(y,results)
print('Parameters: ', results.params)
print('R2: ', results.rsquared)
print('Predicted values: ', results.predict())