import subprocess
result=subprocess.run(['echo',"welcome to python"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
print(result.stdout)
