import numpy as np
from sklearn.linear_model import LinearRegression
# Add Save and Load Training Model data 
# Sample data for sales prediction
advertising_expenditure = np.array([100, 200, 300, 400, 500]).reshape(-1, 1)  # Independent variable
sales = np.array([250, 450, 550, 650, 750])  # Dependent variable

# Print sample data for sales prediction
print("Sales Prediction Sample Data:")
print("------------------------------")
print("| Advertising Expenditure | Sales  |")
print("|-------------------------|--------|")
for expenditure, sale in zip(advertising_expenditure, sales):
    print(f"|         ${expenditure}         | ${sale}  |")
print("------------------------------")
print()

# Create and train the linear regression model for sales prediction
sales_model = LinearRegression()
sales_model.fit(advertising_expenditure, sales)

# Sample data for house price estimation
area = np.array([1000, 1500, 2000, 2500, 3000]).reshape(-1, 1)  # Independent variable
rooms = np.array([2, 3, 4, 3, 4]).reshape(-1, 1)  # Independent variable
house_prices = np.array([300000, 450000, 500000, 550000, 600000])  # Dependent variable

# Print sample data for house price estimation
print("House Price Estimation Sample Data:")
print("----------------------------------")
print("|   Area   | Rooms | House Price |")
print("|----------|-------|-------------|")
for a, r, price in zip(area, rooms, house_prices):
    print(f"|  {a} sqft  |   {r}   |  ${price}   |")
print("----------------------------------")
print()

# Create and train the linear regression model for house price estimation
house_price_model = LinearRegression()
house_price_model.fit(np.concatenate((area, rooms), axis=1), house_prices)

# Make predictions
advertising_expenditure_new = np.array([[600]])  # New advertising expenditure for sales prediction
predicted_sales = sales_model.predict(advertising_expenditure_new)

area_new = np.array([[1800]])  # New area for house price estimation
rooms_new = np.array([[3]])  # New number of rooms for house price estimation
predicted_house_price = house_price_model.predict(np.concatenate((area_new, rooms_new), axis=1))

# Print predictions
print("Predictions:")
print("---------------------------")
print("|      Sales       | Price |")
print("|------------------|-------|")
print(f"|   ${predicted_sales[0]}   |  N/A  |")
print(f"|      N/A       |  ${predicted_house_price[0]}  |")
print("---------------------------")

