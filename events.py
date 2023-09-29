import random

class events:
    def __init__(self):
        pass

    @staticmethod
    def talk():
        pass

    @staticmethod
    def roll():
        print(random.randint(1,6))


    introduction = {
        "non_list_elements": 2,
        "title": "What are you going to do?",
        "Talk to a character": talk,
        "Roll a dice": roll
    }

    def __str__(self):
        print("Loaded events")