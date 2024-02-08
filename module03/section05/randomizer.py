
import random

def get_random_number():
    number = random.randrange(1, 1000) # Get random number between [1 and 1000)
    return number


print(f"2 {__name__}")


if __name__ == "__main__":
    res = get_random_number()
    print(res)

    def test_scope():
        print("asdasd")