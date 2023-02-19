from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
import typing as tp


class YouTube:
    def __init__(self, path_to_df: str = "RUvideos_short.csv"):
        self.df = pd.read_csv(path_to_df)
        self.df['trending_date'] = pd.to_datetime(self.df['trending_date'], format='%y.%d.%m')

    def task1(self) -> pd.DataFrame:
        return self.df

    def task2(self) -> pd.DataFrame:
        self.df = self.df[["trending_date", "category_id", "views", "likes", "dislikes", "comment_count"]]
        self.df["trending_date"] = self.df["trending_date"].apply(lambda x: x.day)
        return self.df

    def task3(self) -> Figure:
        fig, ax = plt.subplots(figsize=(15, 7))
        sns.boxplot(x=self.df['trending_date'].dt.day, y="views", data=self.df, ax=ax)
        ax.grid(True)
        ax.tick_params(axis='x', labelsize=20)
        ax.tick_params(axis='y', labelsize=20)

        ax.set_title("Количество просмотров видео по дням ноября 2017 года", fontsize=20)
        ax.set_ylabel('Миллионы просмотров', fontsize=20)
        ax.set_xlabel('Дни', fontsize=20)
        plt.savefig('amount_of_views_on_every_day_incorrect')
        return fig

    def task4(self) -> Figure:
        fig, ax = plt.subplots(figsize=(15, 7))
        sns.boxplot(x=self.df['trending_date'].dt.day, y="views", data=self.df, ax=ax)
        ax.grid(True)
        plt.ylim([0, 475000])
        ax.tick_params(axis='x', labelsize=20)
        ax.tick_params(axis='y', labelsize=20)

        ax.set_title("Количество просмотров видео по дням ноября 2017 года", fontsize=20)
        ax.set_ylabel('Просмотры', fontsize=20)
        ax.set_xlabel('Дни', fontsize=20)
        plt.savefig('amount_of_views_on_every_day_correct')
        return fig

    def task5(self) -> Figure:
        fig = sns.jointplot(x="views", y="likes", data=self.df, height=15, alpha=0.3)
        fig.fig.suptitle("Диаграмма рассеяния: просмотры vs лайки", fontsize=30)
        ax = fig.ax_joint

        ax.tick_params(axis='x', labelsize=20)
        ax.tick_params(axis='y', labelsize=18)

        ax.set_ylabel('Лайки', fontsize=20)
        ax.set_xlabel('Миллионы просмотров', fontsize=20)

        fig.fig.tight_layout()
        plt.savefig('scattering_diagram_incorrect')
        return fig.fig

    def task6(self) -> Figure:
        self.df = self.df[(self.df['views'] < 200000) & (self.df['likes'] < 10000)]

        fig = sns.jointplot(x="views", y="likes", data=self.df, height=15, alpha=0.3)
        fig.fig.suptitle("Диаграмма рассеяния: просмотры vs лайки", fontsize=30)
        ax = fig.ax_joint

        ax.tick_params(axis='x', labelsize=20)
        ax.tick_params(axis='y', labelsize=20)

        ax.set_ylabel('Лайки', fontsize=20)
        ax.set_xlabel('Просмотры', fontsize=20)

        fig.fig.tight_layout()
        plt.savefig('scattering_diagram_correct')
        return fig.fig

youtube = YouTube()
print(youtube.task3().show())
print(youtube.task4().show())
print(youtube.task5().show())
print(youtube.task6().show())

