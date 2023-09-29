# Game stuff
import game_data
import events

events = events.events()

def exec_event(event):

    for key in event.keys():
        if not key.islower():
            print(key)

    action = input()
    # Understand it
    list(event.values())[int(action) + event["non_list_elements"] - 1]()


def game_loop():
    print("What are you going to do?\n\n")
    action = exec_event(events.introduction)

    # print(list(events.introduction)[int(action)])

    #print(events.introduction.keys())
    #implement error checking for action

game_loop()
