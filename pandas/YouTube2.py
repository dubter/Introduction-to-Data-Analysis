import json
import typing as tp

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from matplotlib.figure import Figure


class YouTube2:
    def __init__( # task0
        self,
        trends_df_path: str="RUvideos_short.csv",
        categories_df_path: str="RU_category_id.json"
    ):
        self.trends_df = pd.read_csv(trends_df_path)
        self.trends_df['trending_date'] = pd.to_datetime(self.trends_df['trending_date'], format='%y.%d.%m')

        with open(categories_df_path) as json_file:
            json_data = json.load(json_file)

        self.categories_df = pd.DataFrame(columns=['id', 'name'])

        for item in json_data['items']:
            self.categories_df = self.categories_df.append(
                {'id': int(item['id']),
                 'name': item['snippet']['title']},
                ignore_index=True
            )

        self.categories_df['id'] = self.categories_df['id'].astype(int)

    def task1(self) -> pd.DataFrame:
        return pd.merge(self.trends_df, self.categories_df, left_on='category_id', right_on='id')


    def task2(self) -> pd.DataFrame:
        df = self.task1()
        return pd.pivot_table(df, values='views', index='name', columns='trending_date', aggfunc=np.sum)

    def task3(self) -> Figure:
        df = self.task2()
        fig, ax = plt.subplots(figsize=(20, 15))
        sns.heatmap(df / 10 ** 6, annot=True, fmt='.3f', cmap='coolwarm', ax=ax)
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=20)

        ax.set_xticklabels(df.columns.strftime('%Y-%m-%d'), rotation=50)
        ax.set_title('Количество миллионов просмотров по датам для каждой категории', fontsize=35)
        ax.set_xlabel('Дата', fontsize=25)
        ax.set_ylabel('Категории', fontsize=25)

        ax.tick_params(axis='x', labelsize=20)
        ax.tick_params(axis='y', labelsize=20)

        fig.tight_layout()
        plt.savefig('heatmap')
        return fig

    def task4(self) -> pd.DataFrame:
        df = self.task1()
        return pd.pivot_table(df, values='views', index='name', columns='trending_date', aggfunc=np.sum, margins=True, margins_name='2000-01-01')

    def task5(self) -> Figure:
        df = self.task4()
        fig, ax = plt.subplots(figsize=(20, 15))

        new_index = df.index.tolist()
        new_index[-1] = 'Всего просмотров'
        df.index = new_index

        sns.heatmap(df / 10 ** 6, annot=True, fmt='.3f', cmap='coolwarm', ax=ax, vmax=13)
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=20)

        buff1 = df.columns.strftime('%Y-%m-%d').tolist()
        buff1[-1] = 'Всего просмотров'
        buff1 = df.set_axis(buff1, axis=1)

        ax.set_xticklabels(buff1, rotation=50)

        ax.set_title('Количество миллионов просмотров по датам для каждой категории', fontsize=35)
        ax.set_xlabel('Дата', fontsize=25)
        ax.set_ylabel('Категории', fontsize=25)

        ax.tick_params(axis='x', labelsize=20)
        ax.tick_params(axis='y', labelsize=20)

        fig.tight_layout()
        plt.savefig('heatmap_with_all_cols')
        return fig

u = YouTube2()
print(u.task5().show())