import random

secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

for attempt in range(1, 7):
    guess = int(input(f"Attempt {attempt}/6. Enter your guess: "))
    if guess == secret_number:
        print(f"🎉 Correct! You guessed it in {attempt} tries!")
        break
    print("Too high!" if guess > secret_number else "Too low!")
else:
    print(f"😢 Game over! The number was {secret_number}.")
