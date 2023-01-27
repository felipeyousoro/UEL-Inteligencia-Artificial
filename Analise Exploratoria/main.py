import csv
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = 'Analise Exploratoria/pokemon_alopez247.csv'

## Exercicio 2 - Analise individual

def gen_hp_graph(pd_data):
    pd_data['HP'].plot(kind='hist', title='HP', bins=range(0, 200, 1))
    plt.savefig('Analise Exploratoria/HP.png')
    plt.close()
    
def gen_attack_graph(pd_data):
    pd_data['Attack'].plot(kind='hist', title='Attack', bins=range(0, 200, 5))
    plt.savefig('Analise Exploratoria/Attack.png')
    plt.close()

def gen_weight_graph(pd_data):
    pd_data['Weight_kg'].plot(kind='box', title='Weight', vert=False, xlim=(0, 200))
    plt.savefig('Analise Exploratoria/Weight.png')
    plt.close()

def gen_no_pokemon_by_generation(pd_data):
    pd_data.groupby('Generation')['Name'].count().plot(kind='bar', title='No. Pokemon by Generation')
    plt.savefig('Analise Exploratoria/No_Pokemon_Generation.png')
    plt.close()

def gen_no_pokemon_by_first_type(pd_data):
    pd_data.groupby('Type_1')['Name'].count().plot(kind='bar', title='No. Pokemon by First Type')
    plt.savefig('Analise Exploratoria/No_Pokemon_First_Type.png')
    plt.close()

def gen_no_pokemon_by_second_type(pd_data):
    pd_data.groupby('Type_2')['Name'].count().plot(kind='bar', title='No. Pokemon by Second Type')
    plt.savefig('Analise Exploratoria/No_Pokemon_Second_Type.png')
    plt.close()
    pd_data['Type_2'].fillna('None', inplace=True)
    pd_data.groupby('Type_2')['Name'].count().plot(kind='bar', title='No. Pokemon by Second Type')
    plt.savefig('Analise Exploratoria/No_Pokemon_Second_Type_None_Included.png')
    plt.close()


## Exercicio 3 - Relacionando variaveis

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

def gen_avg_total_for_generation(pd_data):
    pd_data.groupby('Generation')['Total'].mean().plot(kind='line', title='Average Total by Generation')
    plt.savefig('Analise Exploratoria/Avg_Total_Generation.png')
    plt.close()

def gen_no_pokemon_by_type(pd_data):
    no_pokemon_by_type_1 = pd_data.groupby('Type_1').count()[['Name']]
    no_pokemon_by_type_2 = pd_data.groupby('Type_2').count()[['Name']]
    no_pokemon_by_type = no_pokemon_by_type_1.add(no_pokemon_by_type_2, fill_value=0)
    no_pokemon_by_type.rename(columns={'Count': 'No. Pokemon'}, inplace=True)
    no_pokemon_by_type['Name'].plot(kind='bar', title='No. Pokemon by Type')

    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.savefig('Analise Exploratoria/No_Pokemon_Type.png')
    plt.close()

def gen_most_common_type_combination(pd_data):
    pd_data['Type_2'].fillna('None', inplace=True)
    pd_data = pd_data[pd_data['Type_2'] != 'None']
    pd_data.groupby(['Type_1', 'Type_2'])['Name'].count().sort_values(ascending=False).head(10).plot(kind='bar', title='Most Common Type Combination')

    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.xticks(rotation=45)
    plt.savefig('Analise Exploratoria/Most_Common_Type_Combination.png')
    plt.close()

if __name__ == '__main__':

    data_pandas = pd.read_csv(CSV_PATH)

##### Ex 2


    # gen_hp_graph(data_pandas)
    # gen_attack_graph(data_pandas)

    # gen_weight_graph(data_pandas)

    # gen_no_pokemon_by_generation(data_pandas)
    # gen_no_pokemon_by_first_type(data_pandas)
    # gen_no_pokemon_by_second_type(data_pandas)

##### Ex 3

    # gen_weight_speed_comparison_graph(data_pandas)
    # gen_weight_total_comparison_graph(data_pandas)

    # gen_height_speed_comparison_graph(data_pandas)
    # gen_height_total_comparison_graph(data_pandas)

    # gen_avg_total_for_generation(data_pandas)

    #gen_most_common_type_combination(data_pandas)
    gen_no_pokemon_by_type(data_pandas)