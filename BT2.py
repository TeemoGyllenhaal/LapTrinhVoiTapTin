def doc_tep_tin(x):
    with open(x,'r') as f:
        z = f.read()
        print(z)
        f.close()
doc_tep_tin(r'D:\Data\tệp tin.txt')