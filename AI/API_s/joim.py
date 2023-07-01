# Provide the paths to the input raw files
input_file_path1 = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/AI/API_s/Deeper1.raw'
input_file_path2 = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/AI/API_s/Deeper2.raw'

# Open the first input raw file for reading
with open(input_file_path1, 'rb') as file1:
    # Read the raw data from the first file
    raw_data1 = file1.read()

# Open the second input raw file for reading
with open(input_file_path2, 'rb') as file2:
    # Read the raw data from the second file
    raw_data2 = file2.read()

# Concatenate the raw data from the two files
joined_raw_data = raw_data1 + raw_data2

# Provide the path to the output raw file
output_file_path = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/AI/API_s/Deeper.raw'

# Write the joined raw data to the output file
with open(output_file_path, 'wb') as file:
    file.write(joined_raw_data)

print("Joining completed.")
