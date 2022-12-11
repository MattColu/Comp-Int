import pickle

infile = "./agent"
with open(infile, "rb") as fp:
    loaded = pickle.load(fp)
for l in loaded:
    print(l)