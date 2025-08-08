# main.py
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from oop import Myclass

# Generate data
a, b, c = Myclass.multiply(150)

df = pd.DataFrame({"A": a, "B": b, "PRODUCT": c})

x = df[["A", "B"]]
y = df["PRODUCT"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

model = RandomForestRegressor()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")

newdata = pd.DataFrame({
    "A": [int(input("Enter the first value: "))],
    "B": [int(input("Enter the second value: "))]
})

predict = model.predict(newdata)
print(f"Predicted Product: {predict[0]:.0f}")
