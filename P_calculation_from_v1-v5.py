import pandas as pd
import numpy as np

# Define the function to calculate P based on the given formula
def calculate_P(v0, v1, v2, v3, v4):
    numerator = (v2 + v4) - (v1 + v3)
    denominator = 2 * v0 * (np.sin(np.radians(36)) + np.sin(np.radians(72)))
    P = np.arctan(numerator / denominator)
    P_degrees = np.degrees(P)
    P_degrees = np.where(P_degrees < 0, P_degrees + 360, P_degrees)
    return P_degrees
        

# Read the data from the file
file_path = '/mnt/rna/home/nkumarachchi2019/dev_1d_ABGEZ_benckmark_systems/ABGEZ_newv1v3chi_betacomb4/monomers/C/combine/custom.dat'  # Replace with your actual file path
data = pd.read_csv(file_path, delim_whitespace=True)

# Extract necessary columns
#mychi:1         v1:1         v2:1         v3:1         v4:1         v5:1
chi = data['mychi:1']
v0 = data['v1:1']
v1 = data['v2:1']
v2 = data['v3:1']
v3 = data['v4:1']
v4 = data['v5:1']

# Calculate P for each row
P_values = calculate_P(v0, v1, v2, v3, v4)

chi = np.where(chi < 0, chi + 360, chi)


# Print P vs chi
#for chi_value, P_value in zip(chi, P_values):
#    print(f"{P_value}\t{chi_value}")

    
with open("P_vs_chi.dat", 'w') as file:
    # Write the header if necessary

    file.write("P_value\tchi_value\n")
    # Iterate over chi and P_values, and write each pair to the file

    for chi_value, P_value in zip(chi, P_values):
        file.write(f"{P_value}\t{chi_value}\n")
        

        
            