import pandas as pd

# Load the generated responses from H3_outputs_125M.xlsx
df = pd.read_excel("H3_outputs_125M.xlsx")

# Initialize counters and a list to store correctness of each prediction
correct_count = 0
total_samples = len(df)
prediction_results = []  # Stores 1 for correct, 0 for incorrect

# Function to extract the first non-empty substring (number)
def extract_first_number(text):
    # Split text by whitespace and find the first non-empty substring
    parts = text.split()
    for part in parts:
        if part.strip():  # Check for non-empty substring
            return part
    return ""  # Return empty string if no valid substring found

# Loop through each response and check if the first substring is "1"
for idx, row in df.iterrows():
    response = row["Output"]
    first_number = extract_first_number(response)
    
    # Check if the first extracted number is "1"
    if first_number == "1":
        prediction_results.append(1)  # Correct prediction
        correct_count += 1
    else:
        prediction_results.append(0)  # Incorrect prediction

# Calculate accuracy
accuracy = correct_count / total_samples * 100

# Report results
print(f"Total samples: {total_samples}")
print(f"Correct predictions: {correct_count}")
print(f"Accuracy: {accuracy:.2f}%")
print("Prediction Results (1 = Correct, 0 = Incorrect):")
print(prediction_results)

