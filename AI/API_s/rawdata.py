import os

# Provide the path to your input raw file
input_file_path = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/AI/API_s/Deeper.mp3'

# Open the input raw file for reading
with open(input_file_path, 'rb') as file:
    # Read the raw data
    raw_data = file.read()

# Calculate the length of the raw data
data_length = len(raw_data)

# Split the raw data into two parts
split_index = data_length // 2
part1 = raw_data[:split_index]
part2 = raw_data[split_index:]

# Determine the output file paths for the two parts
output_file_path1 = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/AI/API_s/Deeper1.raw'
output_file_path2 = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/AI/API_s/Deeper2.raw'

# Write the first part to a file
with open(output_file_path1, 'wb') as file:
    file.write(part1)

# Write the second part to a file
with open(output_file_path2, 'wb') as file:
    file.write(part2)

print("Splitting completed.")
