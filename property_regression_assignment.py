import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.linalg import lstsq

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ------------------------------------------------------------
# 1. Load dataset
# ------------------------------------------------------------
file_path = "Dataset.csv"
df = pd.read_csv(file_path)

print("=" * 80)
print("DATASET OVERVIEW")
print("=" * 80)
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())


# ------------------------------------------------------------
# 2. Optional sampling for faster execution
# ------------------------------------------------------------
USE_SAMPLE = True
SAMPLE_SIZE = 50000
RANDOM_STATE = 42

if USE_SAMPLE:
    df = df.sample(n=SAMPLE_SIZE, random_state=RANDOM_STATE)

print("\nWorking shape after sampling:", df.shape)


# ------------------------------------------------------------
# 3. Basic cleaning
# ------------------------------------------------------------
# The 'No' column is an identifier and should not be used as a predictor.
if "No" in df.columns:
    df = df.drop(columns=["No"])

target = "Price"

# Separate predictors and target
X = df.drop(columns=[target])
y = df[target]

# Identify numerical and categorical columns
numeric_features = X.select_dtypes(include=np.number).columns.tolist()
categorical_features = X.select_dtypes(exclude=np.number).columns.tolist()

print("\nNumerical features:")
print(numeric_features)
print("\nCategorical features:")
print(categorical_features)


# ------------------------------------------------------------
# 4. Exploratory Data Analysis
# ------------------------------------------------------------
print("\nGenerating EDA plots...")

# Distribution of target variable
plt.figure(figsize=(10, 6))
sns.histplot(df["Price"], bins=40, kde=True)
plt.title("Distribution of Property Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("eda_price_distribution.png")
plt.show()

# Scatter plot: Floor area vs price
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Floor_Area", y="Price", alpha=0.4)
plt.title("Floor Area vs Price")
plt.xlabel("Floor Area")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("eda_floor_area_vs_price.png")
plt.show()

# Box plot: Price by property type
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="Property_Type", y="Price")
plt.title("Price by Property Type")
plt.xlabel("Property Type")
plt.ylabel("Price")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("eda_price_by_property_type.png")
plt.show()

# Heatmap for numerical correlations
numeric_df = df.select_dtypes(include=np.number)
plt.figure(figsize=(14, 10))
sns.heatmap(numeric_df.corr(), cmap="coolwarm", annot=False)
plt.title("Correlation Heatmap of Numerical Variables")
plt.tight_layout()
plt.savefig("eda_correlation_heatmap.png")
plt.show()


# ------------------------------------------------------------
# 5. Train-test split
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE
)


# ------------------------------------------------------------
# 6. Preprocessing
# ------------------------------------------------------------
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ]
)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

print("\nProcessed training shape:", X_train_processed.shape)
print("Processed test shape:", X_test_processed.shape)


# ------------------------------------------------------------
# 7. Implementation 1: Multiple Linear Regression using Scikit-learn
# ------------------------------------------------------------
print("\n" + "=" * 80)
print("SCIKIT-LEARN IMPLEMENTATION")
print("=" * 80)

sklearn_model = LinearRegression()
sklearn_model.fit(X_train_processed, y_train)

y_pred_sklearn = sklearn_model.predict(X_test_processed)

mae_sklearn = mean_absolute_error(y_test, y_pred_sklearn)
mse_sklearn = mean_squared_error(y_test, y_pred_sklearn)
rmse_sklearn = np.sqrt(mse_sklearn)
r2_sklearn = r2_score(y_test, y_pred_sklearn)

print(f"MAE  : {mae_sklearn:.2f}")
print(f"MSE  : {mse_sklearn:.2f}")
print(f"RMSE : {rmse_sklearn:.2f}")
print(f"R²   : {r2_sklearn:.4f}")


# ------------------------------------------------------------
# 8. Implementation 2: Multiple Linear Regression using SciPy
# ------------------------------------------------------------
print("\n" + "=" * 80)
print("SCIPY IMPLEMENTATION")
print("=" * 80)

# Add intercept manually
X_train_bias = np.column_stack([np.ones(X_train_processed.shape[0]), X_train_processed])
X_test_bias = np.column_stack([np.ones(X_test_processed.shape[0]), X_test_processed])

# Least squares solution
coefficients, residuals, rank, singular_values = lstsq(X_train_bias, y_train.to_numpy())

y_pred_scipy = X_test_bias @ coefficients

mae_scipy = mean_absolute_error(y_test, y_pred_scipy)
mse_scipy = mean_squared_error(y_test, y_pred_scipy)
rmse_scipy = np.sqrt(mse_scipy)
r2_scipy = r2_score(y_test, y_pred_scipy)

print(f"MAE  : {mae_scipy:.2f}")
print(f"MSE  : {mse_scipy:.2f}")
print(f"RMSE : {rmse_scipy:.2f}")
print(f"R²   : {r2_scipy:.4f}")


# ------------------------------------------------------------
# 9. Compare the two implementations
# ------------------------------------------------------------
results = pd.DataFrame({
    "Library": ["Scikit-learn", "SciPy"],
    "MAE": [mae_sklearn, mae_scipy],
    "MSE": [mse_sklearn, mse_scipy],
    "RMSE": [rmse_sklearn, rmse_scipy],
    "R2": [r2_sklearn, r2_scipy]
})

print("\n" + "=" * 80)
print("MODEL COMPARISON")
print("=" * 80)
print(results)

results.to_csv("model_comparison_results.csv", index=False)


# ------------------------------------------------------------
# 10. Actual vs predicted plots
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_sklearn, alpha=0.4, label="Scikit-learn")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], linestyle="--")
plt.title("Actual vs Predicted Prices - Scikit-learn")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.legend()
plt.tight_layout()
plt.savefig("actual_vs_predicted_sklearn.png")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_scipy, alpha=0.4, label="SciPy")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], linestyle="--")
plt.title("Actual vs Predicted Prices - SciPy")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.legend()
plt.tight_layout()
plt.savefig("actual_vs_predicted_scipy.png")
plt.show()


# ------------------------------------------------------------
# 11. Identify important coefficients from Scikit-learn model
# ------------------------------------------------------------
feature_names = preprocessor.get_feature_names_out()
coef_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": sklearn_model.coef_
})

coef_df["Absolute_Coefficient"] = coef_df["Coefficient"].abs()
coef_df = coef_df.sort_values(by="Absolute_Coefficient", ascending=False)

print("\nTop 15 coefficients by absolute magnitude:")
print(coef_df.head(15))

coef_df.head(15).to_csv("top_15_coefficients.csv", index=False)


# ------------------------------------------------------------
# 12. Short interpretation notes
# ------------------------------------------------------------
print("\n" + "=" * 80)
print("INTERPRETATION")
print("=" * 80)
print("1. The task is a regression problem because the target variable, Price, is continuous.")
print("2. Mixed data types are handled through median imputation for numerical variables")
print("   and most frequent imputation with one-hot encoding for categorical variables.")
print("3. Scikit-learn and SciPy should produce very similar results because both solve")
print("   the same multiple linear regression problem using least squares.")
print("4. A higher R² and lower MAE or RMSE indicate better predictive performance.")
print("5. The EDA plots help explain variable distributions, relationships, and possible")
print("   patterns between property features and price.")
