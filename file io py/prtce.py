l1=['Soubhagya',' Ranjan',' Tarai\n']
with open('fil1pr.txt','w+') as f:
    f.writelines(l1)
    f.writelines(l1)
    f.writelines(l1)
    f.writelines(l1)
    f.writelines(l1)
    f.seek(0)
    print(f.readline())