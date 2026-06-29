import pandas as pd

# Load the dataset
df = pd.read_csv("medical.csv", encoding="latin1")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df = df.dropna()

# Check for duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Rename column names
df.columns = (
    df.columns
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# Standardize text values
df["gender"] = df["gender"].str.strip().str.upper()
df["neighbourhood"] = df["neighbourhood"].str.strip().str.upper()
df["no_show"] = df["no_show"].str.strip().str.title()

# Convert date columns to datetime format
df["scheduledday"] = pd.to_datetime(df["scheduledday"])
df["appointmentday"] = pd.to_datetime(df["appointmentday"])

# Fix data types
df["age"] = df["age"].astype(int)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nDataset cleaned successfully!")