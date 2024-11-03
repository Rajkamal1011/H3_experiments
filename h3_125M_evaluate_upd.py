import pandas as pd

# Load the generated responses from H3_outputs_125M_cleaned.xlsx
df = pd.read_excel("H3_outputs_125M_cleaned.xlsx")

# Initialize counters and a list to store correctness of each prediction
correct_count = 0
total_samples = len(df)
prediction_results = []  # Stores 1 for correct, 0 for incorrect

# Function to extract the first non-empty character
def extract_first_character(text):
    # Iterate over each character to find the first non-space character
    for char in text:
        if char.strip():  # Check for non-space character
            return char
    return ""  # Return empty string if no valid character found

# Loop through each response and check if the first character is "1"
for idx, row in df.iterrows():
    response = row["Only_Output"]
    first_character = extract_first_character(response)
    
    # Check if the first extracted character is "1"
    if first_character == "1":
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

