import numpy as np
def sinh_ngau_nhien_so_nguyen():
    np.random.seed(10001)
    a = np.random.randint(low = -1000, high = 1000, size = 1000)
    return a
def ghi_tep_tin(x,a):
    with open(x,'w') as f:
        for i in range (0,1000,1):
            if i % 10 != 0:
                f.write(str(a[i]))
                f.write(',')
            else:
                f.write('\n')
                f.write(str(a[i]))
                f.write(',')
        f.close()
def main():
    z = sinh_ngau_nhien_so_nguyen()
    print(z)
    ghi_tep_tin(r'D:\Data\1000 số.txt',sinh_ngau_nhien_so_nguyen())
if __name__ == "__main__":
    main()
