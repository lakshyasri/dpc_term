import sys

def main():
    n = str(sys.argv[1])
    x = str(sys.argv[2])

    f = open(n+".py","w+")
    f.write("sample = "+"'"+x+"'"+"\n")
    f.write("name = '"+n+"'\n")
    f.write("print(sample)\n")
    f.close()

if __name__=="__main__":
    main()