import pandas as pd
import matplotlib.pyplot as plt

playlist = {
    "Cancion": ["Until sleeps", "revolution", "Wish you Were Here"],
    "Artista": ["Metallica", "The Beatles", "Pink Floyd" ],
    "Duracion": [270, 205, 340]
}

a = pd.DataFrame(playlist)

print(a)

