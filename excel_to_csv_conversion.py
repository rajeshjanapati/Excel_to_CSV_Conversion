import pandas as pd

# Define file paths
excel_file = r"C:\Users\rajesh.kumar\Documents\VSCode\Excel_to_CSV_Conversion\Resource Skill Matrix.xlsx"  # Replace with your actual file path

csv_file = "output.csv"  # Desired CSV output path

# Read the Excel file
df = pd.read_excel(excel_file)

# Convert and save as CSV
df.to_csv(csv_file, index=False, encoding='utf-8')

print(f"Excel file successfully converted to CSV: {csv_file}")
