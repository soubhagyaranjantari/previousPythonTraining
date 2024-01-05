from pathlib import Path
file_path = Path("D:\\text.txt")
f = open(file_path,'r')
f1=f.read()
print(f1)
f.close()