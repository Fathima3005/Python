try:
       
  book_title = input("Enter title of the book: ")
  pub_year = input("Enter publication year: ")

  if not book_title.replace(" ", "").isalpha():
        raise ValueError("Book title must have only letters and spaces.")    

  if not (pub_year.isdigit() and len(pub_year) == 4 and (pub_year.startswith("19") or pub_year.startswith("20"))):
        raise ValueError("Year must be 4 digits and start with 19 or 20.")

  print(f"\nBook added successfully!")
  print(f"Title: {book_title}")
  print(f"Publication Year: {pub_year}")

except ValueError as e:
    print(e)

finally:
    print("\nProcess completed.")

