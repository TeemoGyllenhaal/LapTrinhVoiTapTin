a = str(input("Nhập một chuỗi kí tự từ bàn phím: "))
def luu_tep_tin(x):
    with open(x,'w') as f:
        f.write(a)
        f.close()
luu_tep_tin(r'D:\Data\tệp tin.txt')