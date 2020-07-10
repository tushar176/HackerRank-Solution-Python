def print_formatted(number):
    a=bin(n).replace("0b","")
    space=len(a)
    for i in range(1,n+1):
        print(
        str(i).rjust(space," "),
        oct(i).replace("0o", "").rjust(space," "),
        hex(i).replace("0x", "").rjust(space," ").upper(),
        bin(i).replace("0b","").rjust(space," ")
        )
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)