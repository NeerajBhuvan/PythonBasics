prefixes = ["Hello", "Hi", "Dear"]
names = ["Neeraj", "Anu", "Varsha"]

# break
for prefix in prefixes:
    for name in names:
        print(prefix, name)
        if prefix == "Hi" and name == "Neeraj":
            break  # break the loop and goes to next prefix iteration
        print("Inner Loop")
    print("Outer Loop")
print("Outside the loop")

# continue
for prefix in prefixes:
    for name in names:
        print(prefix, name)
        if prefix == "Dear" and name == "Neeraj":
            continue  # skips the below code and goes to next names iteration
        print("Inner Loop")
    print("Outer Loop")
print("Outside the loop")

# pass
for prefix in prefixes:
    for name in names:
        print(prefix, name)
        if prefix == "Dear" and name == "Neeraj":
            pass  # won't do anything, use it later or placeholder
        print("Inner Loop")
    print("Outer Loop")
print("Outside the loop")
