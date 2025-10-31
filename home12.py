try:

    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")


    if not name:
        raise ValueError("Name cannot be empty!")
    if not feedback:
        raise ValueError("Feedback cannot be empty!")

except ValueError as e:
    print("Error:", e)

else:
    print("\nThank you for your feedback!")
    print(f"Name: {name}")
    print(f"Feedback: {feedback}")

finally:
    print("\n--- Feedback process complete ---")