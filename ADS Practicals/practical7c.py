def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))

    if m > n:
        return []

    lps = compute_lps(pattern)
    positions = []

    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            positions.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions


# Student Details
print("Name: Almash Lakdawala")
print("Enrollment No.: 26PG030052")

# Input text and pattern
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

# Perform KMP matching
print("KMP Matching:", kmp_search(text, pattern))