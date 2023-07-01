import subprocess

def convert_mkv_to_mp4(input_file, output_file):
    command = ['ffmpeg', '-i', input_file, '-codec', 'copy', output_file]
    subprocess.run(command)

# Example usage
input_file = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/Projects/Yuri.mkv'
output_file = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/Projects/Toko.mp4'

convert_mkv_to_mp4(input_file, output_file)
