import pandas as pd

# Load CSV file
df = pd.read_csv(r"C:\Users\rajesh.kumar\Downloads\data_table_active_directory_user_details.csv")

# Drop rows where 'UserPrincipalName' is NULL or NaN
df_cleaned = df.dropna(subset=['UserPrincipalName'])

# Save the cleaned file
df_cleaned.to_csv("cleaned_file.csv", index=False)

print("Rows with NULL UserPrincipalName removed successfully!")
