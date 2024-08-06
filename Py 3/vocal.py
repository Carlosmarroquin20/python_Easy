
vocals = ["a", "e", "i", "o", "u"]

def is_vocal(x):
    if x.lower() in vocals:
        return "is a vocal"
    else:
        return "is not a vocal"

x = input("Enter a letter to see if it is a vocal: ")

print(f"Your choice was {x}, so it " + is_vocal(x))
