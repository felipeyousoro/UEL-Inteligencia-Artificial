import csv
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = 'Analise Exploratoria/pokemon_alopez247.csv'



if __name__ == '__main__':

    data_pandas = pd.read_csv(CSV_PATH)

    columns_of_stats =  ['Total', 'HP', 'Attack', 
                         'Defense', 'Sp_Atk', 'Sp_Def', 'Speed']

    for column in columns_of_stats:
        data_pandas[column].plot(kind='hist', title=column)
        plt.savefig('Analise Exploratoria/{}.png'.format(column))
        plt.close()
