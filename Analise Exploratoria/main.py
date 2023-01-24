import csv
import pandas as pd

CSV_PATH = 'Analise Exploratoria/pokemon_alopez247.csv'


if __name__ == '__main__':

    data_pandas = pd.read_csv(CSV_PATH)

    print(data_pandas[['HP', 'Attack', "Defense", "Sp_Atk", "Sp_Def", "Speed"]].mean())
