import subprocess
result=subprocess.run(["cat","test2.txt"],stderr=subprocess.PIPE, text=True)
print(result.stderr)
