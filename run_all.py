import os
import subprocess

def run_all_python_files(directory):
    # Get all files in the directory
    for filename in os.listdir(directory):
        # Check if the file ends with .py
        if filename.endswith(".py"):
            filepath = os.path.join(directory, filename)
            print(f"Running: {filepath}")
            # Use subprocess to run the python file
            result = subprocess.run(["python", filepath], capture_output=True, text=True)
            print(f"Output of {filename}:")
            print(result.stdout)
            if result.stderr:
                print(f"Errors in {filename}:")
                print(result.stderr)

if __name__ == "__main__":
    directory = input("Enter the directory containing the Python files: ")
    run_all_python_files(directory)
