import pandas as pd

# Phase 1: Define the Raw Data
data = {
    "Student_ID": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 92, 78]
}

# Phase 2: Structural Transformation
df = pd.DataFrame(data)

# Phase 3: Exporting to File
df.to_csv("FILES_VS CODE/students_pandas.csv", index=False)
print("CSV created successfully!")