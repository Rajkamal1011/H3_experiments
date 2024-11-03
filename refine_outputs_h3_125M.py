import pandas as pd

# Load the Excel file
df = pd.read_excel("H3_outputs_125M.xlsx")

# Define a function to remove the input prefix from the output
def extract_only_output(row):
    test_string = row["Test_String"]
    output = row["Output"]
    
    # Remove the test_string prefix from output, if it exists
    if output.startswith(test_string):
        return output[len(test_string):].strip()  # Strip leading whitespace after removing the prefix
    else:
        return output  # Return as-is if the prefix isn't found

# Apply the function to each row to create the Only_Output column
df["Only_Output"] = df.apply(extract_only_output, axis=1)

# Save the updated DataFrame to a new Excel file
df.to_excel("H3_outputs_125M_cleaned.xlsx", index=False)

print("Processed file saved as H3_outputs_125M_cleaned.xlsx with Only_Output column.")

