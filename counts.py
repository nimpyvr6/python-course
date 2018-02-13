def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
        
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One ower case"
assert count_upper_case("£$%^") == 0, "Special characters"
assert count_upper_case("A, B, C, G") == 4, "Four upper case characters"

print("All tests passed")