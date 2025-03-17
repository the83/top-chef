import pandas as pd
import pyreadr

INPUT_FILES = [
    'challengedescriptions',
    'challengewins',
    'chefdetails',
    'episodeinfo',
    'judges',
    'rewards',
]

for file in INPUT_FILES:
    result = pyreadr.read_r(f'topChef/data/{file}.rda')
    result[file].to_csv(f'output/{file}.csv')
