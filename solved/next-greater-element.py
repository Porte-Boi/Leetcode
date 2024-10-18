def solve():
    n = int(input().strip())
    v = list(map(int, input().strip().split()))

    ans = 0

    for i in range(n - 1):
        p = v[i] + v[n - 1]
        ans = max(ans, p)
    print(ans)

def main():
    t = int(input().strip())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()