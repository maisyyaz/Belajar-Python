if __name__ == '__main__':
    n = int(input())
    string1 = ""
# for (x = 1; x < n+1; x = x - 1)
    for x in range(1, n+1):
        string1 += str(x)

print(string1)
