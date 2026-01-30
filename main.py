from agent import generate_blurb

book = {
    "title": "The Last Signal",
    "genre": "science fiction",
    "hook": "A dying transmission may be humanity’s final warning."
}

blurb = generate_blurb(book)
print(blurb)
