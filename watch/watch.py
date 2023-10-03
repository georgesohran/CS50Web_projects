import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    mat = re.search(r"^\<iframe .*?src\=\"(.{0-42})\".*$",s)
    if mat:
        return mat.group(1)



if __name__ == "__main__":
    main()