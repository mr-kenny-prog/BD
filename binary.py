import pickle

FILENAME = "layer.bin"

name1 = "0"
name2 = "0"

with open(FILENAME, "wb") as file:
    pickle.dump(name1, file)
    pickle.dump(name2, file)