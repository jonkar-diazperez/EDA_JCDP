import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Función para tratar ficheros de datos de estaciones una vez concatenados.
def convertir_ICA(df):
    # Borrado de registros con nulos
    df = df.dropna()
    # incluimos columna con código de la estación del usuario
    est = input("Introduce las siglas de la estación medidora que estamos procesando: ")
    df.insert(2,'Estación',est)
    # reordenamos y reseteamos índice
    df.sort_values(by= ["Date","Hour  (GMT)"]).reset_index(drop=True)
    #Convertimos columnas de datos a float64 y date para agrupar
    if "Benceno (µg/m3)" in df.columns:
        df["Benceno (µg/m3)"] = df["Benceno (µg/m3)"].str.replace(',','.',)
        df["Benceno (µg/m3)"] = df["Benceno (µg/m3)"].astype(np.float64)
    if "CO (mg/m3)" in df.columns:
        df["CO (mg/m3)"] = df["CO (mg/m3)"].str.replace(',','.',)
        df["CO (mg/m3)"] = df["CO (mg/m3)"].astype(np.float64)
    if "CO 8h (mg/m3)" in df.columns:
        df["CO 8h (mg/m3)"] = df["CO 8h (mg/m3)"].str.replace(',','.',)
        df["CO 8h (mg/m3)"] = df["CO 8h (mg/m3)"].astype(np.float64)
    if "Etilbenceno (µg/m3)" in df.columns:
        df["Etilbenceno (µg/m3)"] = df["Etilbenceno (µg/m3)"].str.replace(',','.',)
        df["Etilbenceno (µg/m3)"] = df["Etilbenceno (µg/m3)"].astype(np.float64)
    if "Ortoxileno (µg/m3)" in df.columns:
        df["Ortoxileno (µg/m3)"] = df["Ortoxileno (µg/m3)"].str.replace(',','.',)
        df["Ortoxileno (µg/m3)"] = df["Ortoxileno (µg/m3)"].astype(np.float64)
    if "PM10" in df.columns:
        df["PM10"] = df["PM10"].str.replace(',','.',)
        df["PM10"] = df["PM10"].astype(np.float64)
    if "PM2,5" in df.columns:
        df["PM2,5"] = df["PM2,5"].str.replace(',','.',)
        df["PM2,5"] = df["PM2,5"].astype(np.float64)
    if "Tolueno (µg/m3)" in df.columns:
        df["Tolueno (µg/m3)"] = df["Tolueno (µg/m3)"].str.replace(',','.',)
        df["Tolueno (µg/m3)"] = df["Tolueno (µg/m3)"].astype(np.float64)

    df["Date"] = pd.to_datetime(df["Date"], format='%d/%m/%Y')
    #agrupamos por Date
    df = df.groupby("Date").mean(numeric_only= True).round(2).sort_index()
        
    return df
