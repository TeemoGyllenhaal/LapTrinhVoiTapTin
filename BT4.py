def doc_tep_tin_bai_3(x):
    with open(x,'r') as f:
        z = f.read()
        print(z)
        f.close()
doc_tep_tin_bai_3(r'D:\Data\tệp tin.txt')