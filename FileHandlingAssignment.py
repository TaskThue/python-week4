#sample file(notes.txt)
sample_content = """Python is fun
File handling is important
execption handlinf makes programs safer
Always write clean code
"""

with open("notes.txt", "w") as f:
  f.write(sample_content)
print("Sample file 'notes.txt created'")

# read the file
with open("notes.txt", "r") as f:
  content = f.read()
  
# #open and read
# try:
#   with open("notes.txt", "r") as f:
#     content=f.read()
#     print("File read successfully.\n")
 
    
#modify content
  modified_content =""
  for i, line in enumerate(content.splitlines(), start=1):
    modified_content +=f"{i}: {line}\n"
    
# write modified content to a new file
  with open("modified_notes.txt","w") as f:
    f.write(modified_content)
  print("Modified content saved as 'modified_notes.txt'")

filename = input("Enter the file name to open (e.g., notes.txt or modified_notes.txt): ")
try:
    with open(filename, "r") as f:
        print("\n📄 File content:")
        print(f.read())
except FileNotFoundError:
  print("File not found.")
except PermissionError:
  print("Permission denaied")
except Exception as e:
  print(f"An unexpected error occured: {e}")
