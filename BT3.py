a = str(input("Nhập một chuỗi kí tự từ bàn phím: "))
def ghi_tep_tin(x):
    with open(x,'a') as f:
        f.write('\n')
        f.write(a)
        f.close()
ghi_tep_tin(r'D:\Data\tệp tin.txt')