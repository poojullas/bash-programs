import subprocess
result = subprocess.run(["cat","kashvi1.txt"],stderr=subprocess.PIPE, text=True)
print(result.stderr)
