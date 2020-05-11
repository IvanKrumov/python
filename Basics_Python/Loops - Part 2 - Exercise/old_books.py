book_name = input()
books_count = int(input())
counter = 0

while counter < books_count:
    input_name = input()

    if input_name == book_name:
        input_name = True
        break
    else:
        input_name = False
    counter += 1
if input_name:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
