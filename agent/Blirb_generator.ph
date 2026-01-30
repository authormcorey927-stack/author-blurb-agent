def generate_blurb(book):
    title = book.get("title", "Untitled")
    genre = book.get("genre", "Unknown genre")

    return f"{title} is a gripping {genre} story that pulls readers in from the first page."
