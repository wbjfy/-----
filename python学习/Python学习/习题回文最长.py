
s = 'cbbd'


t = '#'.join(f'^{s}&')
n, center, right, r = len(t), 0, 0, [0] * len(t)

for i in range(1, n - 1):
    r[i] = min(right - i, r[2 * center - i]) if i < right else 0
    a = r[i]
    while t[i - r[i] - 1] == t[i + r[i] + 1]: r[i] += 1
    b = r[i]
    if i + r[i] > right: center, right = i, i + r[i]

max_r, center = max((v, i) for i, v in enumerate(r))
start = (center - max_r) // 2
print(s[start: start + max_r])