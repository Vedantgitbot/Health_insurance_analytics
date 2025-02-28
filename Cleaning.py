import pandas as pd

def clean_data(file_path, output_path):
    """
    Load, clean, and preprocess the insurance dataset.
    Args:
        file_path (str): Path to the raw dataset.
        output_path (str): Path to save the cleaned dataset.
    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    
    data = pd.read_csv(file_path)

    
    data = data.dropna()

    
    data['sex'] = data['sex'].map({'male': 0, 'female': 1})  
    data['smoker'] = data['smoker'].map({'no': 0, 'yes': 1})  
    data['region'] = data['region'].astype('category').cat.codes  

    
    data = data.rename(columns={
        'age': 'Age',
        'sex': 'Sex',
        'bmi': 'BMI',
        'children': 'Children',
        'smoker': 'Smoker',
        'region': 'Region',
        'charges': 'Charges'
    })

   
    data.to_csv(output_path, index=False)
    print(f"Data cleaning complete. Cleaned data saved to '{output_path}'.")

    return data

if __name__ == "__main__":
    # File paths
    raw_data_path = "/Users/vedantbrahmbhatt/Desktop/Health_Insurance_analytics/Health_insurance.csv"  
    cleaned_data_path = "cleaned_insurance_data.csv"

    # Clean the data and save it
    cleaned_data = clean_data(raw_data_path, cleaned_data_path)
import pandas as pd

def clean_data(file_path, output_path):
    """
    Load, clean, and preprocess the insurance dataset.
    Args:
        file_path (str): Path to the raw dataset.
        output_path (str): Path to save the cleaned dataset.
    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    
    data = pd.read_csv(file_path)

    data = data.dropna()

   
    data['sex'] = data['sex'].map({'male': 0, 'female': 1})  
    data['smoker'] = data['smoker'].map({'no': 0, 'yes': 1})  
    data['region'] = data['region'].astype('category').cat.codes  

    
    data = data.rename(columns={
        'age': 'Age',
        'sex': 'Sex',
        'bmi': 'BMI',
        'children': 'Children',
        'smoker': 'Smoker',
        'region': 'Region',
        'charges': 'Charges'
    })

    
    data.to_csv(output_path, index=False)
    print(f"Data cleaning complete. Cleaned data saved to '{output_path}'.")

    return data

if __name__ == "__main__":
    
    raw_data_path = "/Users/vedantbrahmbhatt/Desktop/Health_Insurance_analytics/Health_insurance.csv" 
    cleaned_data_path = "cleaned_insurance_data.csv"

    cleaned_data = clean_data(raw_data_path, cleaned_data_path)
