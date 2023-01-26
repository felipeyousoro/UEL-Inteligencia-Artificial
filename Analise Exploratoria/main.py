import csv
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = 'Analise Exploratoria/pokemon_alopez247.csv'

def gen_hp_graph(pd_data):
    pd_data['HP'].plot(kind='hist', title='HP', bins=range(0, 200, 1))
    plt.savefig('Analise Exploratoria/HP.png')
    plt.close()
    
def gen_attack_graph(pd_data):
    pd_data['Attack'].plot(kind='hist', title='Attack', bins=range(0, 200, 5))
    plt.savefig('Analise Exploratoria/Attack.png')
    plt.close()

def gen_weight_graph(pd_data):
    #boxplot ranging from 0 to 500 kg
    pd_data['Weight_kg'].plot(kind='box', title='Weight', vert=False, xlim=(0, 200))
    plt.savefig('Analise Exploratoria/Weight.png')
    plt.close()

def gen_weight_speed_comparison_graph(pd_data):
    pd_data.plot(kind='scatter', x='Weight_kg', y='Speed', title='Weight x Speed')
    plt.savefig('Analise Exploratoria/Weight_Speed.png')
    plt.close()

def gen_height_speed_comparison_graph(pd_data):
    pd_data.plot(kind='scatter', x='Height_m', y='Speed', title='Height x Speed')
    plt.savefig('Analise Exploratoria/Height_Speed.png')
    plt.close()

def gen_weight_total_comparison_graph(pd_data):
    pd_data.plot(kind='scatter', x='Weight_kg', y='Total', title='Weight x Total')
    plt.savefig('Analise Exploratoria/Weight_Total.png')
    plt.close()

def gen_height_total_comparison_graph(pd_data):
    pd_data.plot(kind='scatter', x='Height_m', y='Total', title='Height x Total')
    plt.savefig('Analise Exploratoria/Height_Total.png')
    plt.close()

if __name__ == '__main__':

    data_pandas = pd.read_csv(CSV_PATH)

    gen_hp_graph(data_pandas)
    gen_attack_graph(data_pandas)

    gen_weight_graph(data_pandas)

    gen_weight_speed_comparison_graph(data_pandas)
    gen_weight_total_comparison_graph(data_pandas)

    gen_height_speed_comparison_graph(data_pandas)
    gen_height_total_comparison_graph(data_pandas)