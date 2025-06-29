import os 
import zipfile
from abc import ABC, abstractmethod
import pandas as pd


class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        pass
    

class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        if not file_path.endswith(".zip"):
            raise ValueError("The provide file is not in the correct format")

        
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall("extracted_data")
            
        extracted_files = os.listdir("extracted_data")
        csv_files = [file for file in extracted_files if file.endswith(".csv")]
        
        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV files found in the extracted folder")
        if len(csv_files) > 1:
            raise ValueError("There are more than one csv file")
        
        
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)
        
        return df

class DataIngestorFactory(DataIngestor):
    @staticmethod    
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Returns the appropriate DataIngestor based on file extension."""
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No ingestor available for file extension: {file_extension}")
        
if __name__ == "__main__":
    # Example usage
    file_path = "data/archive.zip"  # Replace with your zip file path
    file_extension = os.path.splitext(file_path)[1]
    
    ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    df = ingestor.ingest(file_path)
    
    print(df.head())