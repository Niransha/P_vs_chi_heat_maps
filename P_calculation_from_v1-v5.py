####################################################
### calcualte P from extracted v0 v1  v2 v3 v4 #####
### used with cpptraj.torsion_v1-v5_chi_CU.sh  #####
###   and cpptraj.torsion_v1-v5_chi_AG.sh     ######
####### NRK jun 27 2024 ############################
####################################################
import pandas as pd
import numpy as np

# Define the function to calculate P based on the given formula
def calculate_P(v0, v1, v2, v3, v4):
    numerator = ((v2 + v4) - (v1 + v3))
    denominator = 2 * (v0) * (np.sin(np.radians(36)) + np.sin(np.radians(72)))
    P = np.arctan(numerator / denominator)
    P_degrees = np.degrees(P)

    # ref Altona sundaralingam 1972; note : if v0 < 0 ; should add 180 to calculated P
    if v0 < 0:   
        P_degrees += 180          

    if P_degrees < 0:
        P_degrees += 360     

    return P_degrees

# Read the data from the file
file_path = './custom.dat'  # Replace with your actual file path
data = pd.read_csv(file_path, delim_whitespace=True)

# Extract necessary columns
chi = data['mychi:1']
v0 = data['v0:1']
v1 = data['v1:1']
v2 = data['v2:1']
v3 = data['v3:1']
v4 = data['v4:1']

# Calculate P for each row
P_value = data.apply(lambda row: calculate_P(row['v0:1'], row['v1:1'], row['v2:1'], row['v3:1'], row['v4:1']), axis=1)

#Adjust chi values if they are less than 0
chi_value = np.where(chi < 0, chi + 360, chi)

# Write P vs chi to the file
with open("P_vs_chi.dat", 'w') as file:
    # header
    file.write("P_value \t chi_value \n")

    # Iterate over chi and P_values, and write each pair to the file

    for chi_value, P_value in zip(chi_value, P_value):
        file.write(f"{P_value}\t{chi_value}\n")


