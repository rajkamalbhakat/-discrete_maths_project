import pandas as pd

# Load the original CSV file
input_file = "facebook_edges.csv"

df = pd.read_csv(input_file)

print("========== ORIGINAL DATASET ==========")
print("Rows:", len(df))
print("Columns:", df.shape[1])
print("Column names:", df.columns.tolist())


# Remove completely empty rows
df = df.dropna(how="all")

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

# Remove spaces from column names
df.columns = df.columns.str.strip()


# Check required columns
required_columns = ["ego_network", "source", "target"]

for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Missing required column: {column}")


# Convert node IDs to numbers
df["ego_network"] = pd.to_numeric(df["ego_network"], errors="coerce")
df["source"] = pd.to_numeric(df["source"], errors="coerce")
df["target"] = pd.to_numeric(df["target"], errors="coerce")


# Remove rows containing invalid/missing values
df = df.dropna(subset=["ego_network", "source", "target"])


# Convert IDs to integers
df["ego_network"] = df["ego_network"].astype(int)
df["source"] = df["source"].astype(int)
df["target"] = df["target"].astype(int)


# Remove duplicate edges
before_duplicates = len(df)

df = df.drop_duplicates(
    subset=["ego_network", "source", "target"]
)

duplicates_removed = before_duplicates - len(df)


# Remove self-loops
before_self_loops = len(df)

df = df[df["source"] != df["target"]]

self_loops_removed = before_self_loops - len(df)


# Sort the dataset
df = df.sort_values(
    by=["ego_network", "source", "target"]
).reset_index(drop=True)


# Save cleaned dataset
output_file = "cleaned_facebook_edges.csv"

df.to_csv(output_file, index=False)


# Final report
print("\n========== CLEANING REPORT ==========")
print("Final rows:", len(df))
print("Final columns:", df.shape[1])
print("Duplicate edges removed:", duplicates_removed)
print("Self-loops removed:", self_loops_removed)

print("\nMissing values:")
print(df.isnull().sum())

print("\nUnique ego networks:", df["ego_network"].nunique())
print("Unique source nodes:", df["source"].nunique())
print("Unique target nodes:", df["target"].nunique())

print("\n========== COMPLETE ==========")
print("Cleaned dataset saved as:", output_file)