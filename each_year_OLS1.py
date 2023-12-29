# For regression analysis
import pandas as pd
import statsmodels.api as sm

# For scatter plot
import matplotlib.pyplot as plt
import seaborn as sns

# The year you want to show
year = int(input("Type year you want to show ---> "))

# Read dataset from local csv file
file_path = f"~/csv_files/{year}_DID_TFP.csv"
print(f"This data year is {year}")
df = pd.read_csv(file_path)

# Building the model
model = sm.OLS(df["TFP"], sm.add_constant(df["DID"])).fit()

# Getting the summary of the model
model_summary = model.summary()
print(model_summary)

# Plotting the scatter plot and regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(x="DID", y="TFP", data=df, color="blue", label="Data Points")
sns.regplot(
    x="DID", y="TFP", data=df, scatter=False, color="red", label="Regression Line"
)

# Adding regression line equation and R-squared value to the plot
slope = model.params["DID"]
intercept = model.params["const"]
r_squared = model.rsquared
plt.text(
    5000,
    -0.1,
    f"Y = {intercept:.4f} + {slope:.4e}X\nR-squared = {r_squared:.3f}",
    fontsize=12,
    color="green",
)

# Setting plot title and labels
plt.title(
    f"Scatter Plot of Relative TFP vs. DID Population Density with Regression Line ({year})",
    fontsize=14,
)
plt.xlabel("DID Population Density", fontsize=12)
plt.ylabel("Relative TFP", fontsize=12)
plt.legend()

# Display the plot
plt.show()
