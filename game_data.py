class game_data:
    def __init__(self):
        pass

    characters = {
        "catter": {
            "name": "Catter",
            "description": "Just a cute cat!",
            "species": "Cat",
            "tags": ["fuzzy", "fluffy", "cute"],
            "age": 23
        },
        "ramiel": {
            "name": "Ramiel",
            "description": "An angel coming from the heavens. He just fell accidentally.",
            "species": "Angel",
            "tags": ["cute"],
            "age": "Unknown"
        },
        "blobbers": {
            "name": "Blobbers",
            "description": "Embodiment of darkness itself. Diabolical.",
            "species": "Blob",
            "tags": ["evil"],
            "age": 2789354
        },
        "loafer": {
            "name": "Loafer",
            "description": "A cute loaf.",
            "species": "Loaf",
            "tags": [],
            "age": 2
        },
        "nyatasha": {
            "name": "Nyatasha",
            "description": "Princess of the Evil Kingdom. She is often seen around wearing gothic frilly dresses. She is also half cat.",
            "species": "Human, cat",
            "tags": ["evil"],
            "age": 26
        }



    }

    def __str__(self):
        print("Loaded characters")