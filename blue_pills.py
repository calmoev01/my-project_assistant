from time import sleep

def typewriter(text, delay=0.17):
    for char in text:
        print(char, end="", flush=True)
        sleep(delay)
    print()

lyrics = [
    ("I'm stuck up in the matrix baby", 0.10, 0  ),
    ("Poppin' blue pills can't wake up", 0.08, 2.3 ),
    ("But everything we built don't mean shit", 0.06, 2.8 ),
    ("Yea, everything you say don't mean it", 0.05, 0.5 ),
    ("Yea, not the situation I needed", 0.07, 0.7),
    ("I don't need to be here", 0.04, 0.1),
    ("Why do I believe you", 0.06, 0.3),
    ("For you, you, you, I cannot go", 0.08, 1.5),
    ("But you, you, you can't let me go", 0.09, 1.8),
]

for line, speed, pause in lyrics:
    sleep(pause)
    typewriter(line, speed)
