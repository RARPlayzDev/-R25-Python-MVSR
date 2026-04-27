s = "123AB1CD2"
total = 0

for ch in s:
    if ch.isdigit():
        total += int(ch)

print(total)
