import pandas as pd

# Input and output file paths
input_file = "Datasets\From_Barabasi\metabolic.edgelist.txt"
output_file = "Datasets\From_Barabasi\metabolic.csv"

# Read the tab-separated text file
df = pd.read_csv(input_file, sep=r"\s+", header=None, names=["Source", "Target"])

# Save as CSV
df.to_csv(output_file, index=False)

print(f"Successfully converted '{input_file}' to '{output_file}'.")