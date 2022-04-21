def merge_the_tools(astring, k):
    # your code goes here
    chunks = [astring[i:i+k] for i in range(0, len(astring), k)]
    print("\n".join(["".join(list(dict.fromkeys(i))) for i in chunks]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
