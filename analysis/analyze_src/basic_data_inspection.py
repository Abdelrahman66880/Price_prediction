from abc import ABC, abstractmethod

import pandas as pd

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame) -> pd.DataFrame:
        """Abstract method to inspect the DataFrame."""
        pass
    

class DataTypesInspector(DataInspectionStrategy):
    def inspect(self, df):
        print("\nData Types and Non-Null counts")
        print(df.info())


class SummaryStatisticsInspectionStartegy(DataInspectionStrategy):
    def inspect(self, df):
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["O"]))
        
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initializes the DataInspector with a specific inspection strategy.

        Parameters:
        strategy (DataInspectionStrategy): The strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector.

        Parameters:
        strategy (DataInspectionStrategy): The new strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy
    def execute_inspection(self, df: pd.DataFrame):
        """
        Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Executes the strategy's inspection method.
        """
        self._strategy.inspect(df)
        
