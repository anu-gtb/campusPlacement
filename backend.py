import pandas as pd
import pickle

# Load Standardization parameters
with open('scaler.pkl','rb') as f:
   scaler=pickle.load(f)
   
# Load the model
with open('model.pkl','rb') as file:
   model=pickle.load(file)

# Store inputs inside a dataframe
def store_data(inp1,inp2,inp3,inp4,inp5,inp6,inp7):
    df=pd.DataFrame()
    df['hsc_p']=[inp1]
    df['etest_p']=[inp2]
    df['ssc_b_Others']=[inp3]
    df['hsc_s_Science']=[inp4]
    df['degree_t_Others']=[inp5]
    df['workex_Yes']=[inp6]
    df['specialisation_Mkt&HR']=[inp7]
    return df

# Preprocess the inputs
def preprocess_data(df):
    df=df.replace({'Yes':1,'No':0})#OneHotEncoding
    scaled_data=pd.DataFrame(scaler.transform(df))#Standardization
    return scaled_data

# Prediction
def predict(df):
    pred=model.predict(df)
    return pred
