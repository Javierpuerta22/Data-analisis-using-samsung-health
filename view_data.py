import matplotlib.pyplot as plt
import pandas as pd


class Visualizer:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        
        # Add year and month columns
        self.data['year'] = self.data['date'].dt.year
        self.data['month'] = self.data['date'].dt.month
        
        #eliminamos las filas que contienen algun 0
        self.data = self.data[(self.data.T != 0).all()]
        

    def plot_by_year(self, year: int):
        data = self.data[self.data['year'] == year]
        data.drop(columns=["year", "month", "id", "time", "date"], axis=1, inplace=True)
        
        
        plt.figure(figsize=(12, 6))
        for i in range(data.shape[0]):
            plt.plot(data.columns, data.iloc[i], label=f'Serie {i}')



        plt.xlabel('Segundos')
        plt.ylabel('Valores')
        plt.title('Series Temporales')
        plt.legend()
        plt.show()
        
    def plot_all_years(self):
        
        years = self.data['year'].unique()
        
        # creamos un plot que contenga tantos plots como años haya y iteramos sobre ellos para mostrar los datos
        fig, axs = plt.subplots(2, 2, figsize=(12, 6*len(years)))
        axs = axs.flatten()
        for i, year in enumerate(years):
            data = self.data[self.data['year'] == year]
            data.drop(columns=["year", "month", "id", "time", "date"], axis=1, inplace=True)
            for j in range(data.shape[0]):
                axs[i].plot(data.columns, data.iloc[j], label=f'Serie {j}')
            axs[i].set_title(f'Año {year}')
            axs[i].set_ylabel('heart_rate')
        
        plt.show()
        
        
        

if __name__ == "__main__":
    data = pd.read_csv("./data_resumed/personal_data/heart_rate.csv")
    data['date'] = pd.to_datetime(data['date'])
    visualizer = Visualizer(data)
    visualizer.plot_all_years()
        