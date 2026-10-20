def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))

    if m > n:
        return []

    d = 256
    q = 101

    pattern_hash = 0
    text_hash = 0
    h = pow(d, m - 1, q)

    positions = []

    # Calculate initial hash values
    for i in range(m):
        pattern_hash = (
            d * pattern_hash + ord(pattern[i])
        ) % q

        text_hash = (
            d * text_hash + ord(text[i])
        ) % q

    # Slide the pattern over the text
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                positions.append(i)

        # Calculate the next window's hash
        if i < n - m:
            text_hash = (
                d * (text_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % q

            text_hash = (text_hash + q) % q

    return positions


# Student Details
print("Name: Almash Lakdawala")
print("Enrollment No.: 26PG030052")

# Input text and pattern
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

# Perform Rabin-Karp matching
print("Rabin-Karp:", rabin_karp(text, pattern))