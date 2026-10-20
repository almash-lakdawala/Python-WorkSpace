def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))

    if m > n:
        return []

    positions = []

    for i in range(n - m + 1):
        j = 0

        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            positions.append(i)

    return positions


# Student Details
print("Name: Almash Lakdawala")
print("Enrollment No.: 26PG030052")

# Input text and pattern
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

# Perform Naive String Matching
print("Naive Matching:", naive_search(text, pattern))