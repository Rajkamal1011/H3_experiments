import pandas as pd
import subprocess
import os

# Load the test set from CW_testset.xlsx
input_file = "CW_testset.xlsx"
df = pd.read_excel(input_file)
testset = df["Test_String"].tolist()

# Prepare a list to store the outputs
outputs = []

# Define parameters
put_loc = "/home/user"  # Directory where the command should be run
script_path = os.path.join(put_loc, "H3/examples/generate_text_h3.py")
ckpt_path = "H3-125M/model.pt"
dmodel = 768
nlayer = 12
attn_layer_idx = 6
nheads = 12

# Iterate over each test string in the test set
for idx, prompt in enumerate(testset):
    # Format the command to include the current prompt
    command = [
        "PYTHONPATH=$(pwd)/H3", "python", script_path,
        "--ckpt", ckpt_path,
        "--prompt", f'"{prompt}"',
        "--dmodel", str(dmodel),
        "--nlayer", str(nlayer),
        "--attn-layer-idx", str(attn_layer_idx),
        "--nheads", str(nheads)
    ]
    
    try:
        # Execute the command in the specified directory and capture the output
        result = subprocess.run(
            " ".join(command),
            shell=True,
            cwd=put_loc,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Append the model output to the list
        outputs.append(result.stdout.strip())
        print(f"Processed sample {idx + 1}/{len(testset)}")
        
    except subprocess.CalledProcessError as e:
        # If there is an error, store the error message and continue
        print(f"Error processing sample {idx + 1}: {e}")
        outputs.append(f"Error: {e}")

# Save the outputs to a new Excel file
output_df = pd.DataFrame({"Test_String": testset, "Output": outputs})
output_df.to_excel("H3_outputs_125M.xlsx", index=False)

print("All outputs have been saved to H3_outputs_125M.xlsx")

