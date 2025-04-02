# Author: ArkenShazon (Hibob555556 : https://github.com/Hibob555556)
# Last Update: 4-2-25

# import needed deps
import sys
import re

# read in file from args
file = ""
try:
    file = sys.argv[1]
except:
    print("Please specify a file name")

# try read in file contents
file_content = ""
try:
    with open(file, 'r') as f:
        file_content = f.read()
except FileNotFoundError:
    print(f"{file} is not a valid file path")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# replace extra spaces
file_content = re.sub(" {2,1000}", "", file_content)

# parse new name from passed path
new_name = f"{(file.split("/")[len(file.split("/")) - 1]).split('.')[0]}_min.css"

# remove the file name from the file path and assign it to a variable
op = (file.split("/")[0:len(file.split("/")) - 1])
original_path = "" 
for segment in op:
  original_path += f"{segment}/"

# try to create a new minified version of the css file
try:
    with open(f"{original_path}{new_name}", 'w+') as f:
        for line in file_content.split(","):
            f.write(line.replace("\n", " "))
except FileNotFoundError:
    print(f"{file} is not a valid file path")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    