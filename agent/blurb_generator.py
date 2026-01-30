def generate_blurb(book: dict) -> str:
    """
    Generate a simple, genre-aware book blurb.

    Expected keys in book dict:
    - title
    - genre
    - hook (optional)
    """

    title = book.get("title", "Untitled")
    genre = book.get("genre", "Unknown genre")
    hook = book.get(
        "hook",
        "A story that pulls readers in from the very first page."
    )

    return (
        f"{title} is a gripping {genre} story. "
        f"{hook}"
    )
