paragraph="""Python is an interpreted, high-level and general-purpose programming language.
It is an object-oriented language too, which simply means it can model entities in the real world.
"""

length=len(paragraph)
print("Length of the paragraph:",length)

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

# Slice and print 
print("\nPreview (first 50 characters):")
print(paragraph[:50])

paragraph_replaced = paragraph.replace("Python", "PYTHON")
print("\nAfter replacing 'Python' with 'PYTHON':")
print(paragraph_replaced)

# Convert  to lowercase
paragraph_lower = paragraph_replaced.lower()
print("\nLowercase paragraph:")
print(paragraph_lower)

# Remove extra whitespaces from start or end
paragraph_stripped = paragraph_lower.strip()

# Split the paragraph
words = paragraph_stripped.split()
print("\nList of words:")
print(words)

if "course" in words:
    print("\nThe word 'course' is found in the paragraph.")
else:
    print("\nThe word 'course' is not found in the paragraph.")

final_message = "The course description is {} characters long and has {} words.".format(len(paragraph_stripped), len(words))
print("\n" + final_message)


