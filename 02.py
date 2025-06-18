print("hello")

library = []

for i in range(5):
    title = input("title: ")
    author = input("author: ")
    genre = input("genre: ")
    year = input("year: ")

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "year": year
    }

    library.append(book)  

unique_genre = {book["genre"] for book in library}
print("Unique Genres:", unique_genre)

unique_authors = {book["author"] for book in library}
print("Unique Authors:", unique_authors)

unique_years = {book["year"] for book in library}
print("Publication Years:", unique_years)

new = {
    "title": input("New book title: "),
    "author": input("New book author: "),
    "genre": input("New book genre: "),
    "year": input("New book year: ")
}
library.append(new)

library = [book for book in library if book["title"].lower() != "bheem"]

print("\nFinal Library:")
for book in library:
    print(book)

