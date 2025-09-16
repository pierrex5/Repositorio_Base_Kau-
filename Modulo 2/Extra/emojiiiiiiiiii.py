import emoji
import time

emojis = [":earth_africa:", ":fist_raised:", ":fire:", ":musical_note:", ":sparkles:"]

for e in emojis:
    print(emoji.emojize(e, language='alias'), end=' ', flush=True)
    time.sleep(0.5)

print("\nCultura negra é resistência, arte e força!")
