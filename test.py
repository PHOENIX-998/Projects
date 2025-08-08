from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from oop import Myclass

a,b,c = Myclass.add(100000)

df = pd.DataFrame({"A": a, "B": b, "SUM": c})

x = df[["A", "B"]]
y = df["SUM"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R²:", r2)

newdata = pd.DataFrame({
    "A": [int(input("Enter the first value: "))],
    "B": [int(input("Enter the second value: "))]
})

predict = model.predict(newdata)
print(f"Predicted Sum: {predict[0]:.2f}")