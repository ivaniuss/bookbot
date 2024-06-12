def get_content(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def main():
    path = "../books/frankenstein.txt"
    content = get_content(path)
    print(content)

if __name__ == '__main__':
    main()