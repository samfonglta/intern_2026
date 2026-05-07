import os

folder = "dataset"
for filename in os.listdir(folder):
    open(f"dataset/{filename}","w").write("Hello world")

print("All done")
