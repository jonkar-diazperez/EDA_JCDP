import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import funciones as f

 
def cargar_datos_ZBE_DON():
    # DATOS ESTACIONES DONOSTIA
    df_eas_2024_eas = pd.read_csv("../data/20-Gipuzkoa/2024/EASO.csv", sep=';',encoding='latin_1')
    df_eas_2025_eas = pd.read_csv("../data/20-Gipuzkoa/2025/EASO.csv", sep=';',encoding='latin_1')

    df_eas_2024_puy = pd.read_csv("../data/20-Gipuzkoa/2024/PUYO.csv", sep=';',encoding='latin_1')
    df_eas_2025_puy = pd.read_csv("../data/20-Gipuzkoa/2025/PUYO.csv", sep=';',encoding='latin_1')

    df_eas_2024_ate = pd.read_csv("../data/20-Gipuzkoa/2024/ATEGORRIETA.csv", sep=';',encoding='latin_1')
    df_eas_2025_ate = pd.read_csv("../data/20-Gipuzkoa/2025/ATEGORRIETA.csv", sep=';',encoding='latin_1')

    df_eas_2024_tol = pd.read_csv("../data/20-Gipuzkoa/2024/AVDA_TOLOSA.csv", sep=';',encoding='latin_1')
    df_eas_2025_tol = pd.read_csv("../data/20-Gipuzkoa/2025/AVDA_TOLOSA.csv", sep=';',encoding='latin_1')

    df_eas_eas = pd.concat([df_eas_2025_eas,df_eas_2024_eas])
    df_eas_puy = pd.concat([df_eas_2025_puy,df_eas_2024_puy])
    df_eas_ate = pd.concat([df_eas_2025_ate,df_eas_2024_ate])
    df_eas_tol = pd.concat([df_eas_2025_tol,df_eas_2024_tol])
    
    #Tratamiento datasets
    print("Comienza proceso datasets estaciones Donostia")
    print("Estación EASO")
    df_eas_eas_sum = f.convertir_ICA(df_eas_eas)
    print("Estación PUYO")
    df_eas_puy_sum = f.convertir_ICA(df_eas_puy)
    print("Estación ATEGORRIETA")
    df_eas_ate_sum = f.convertir_ICA(df_eas_ate)
    print("Estación AVDA TOLOSA")
    df_eas_tol_sum = f.convertir_ICA(df_eas_tol)
   
    print("Fin proceso datasets estaciones Donostia")

    print("Exportamos a CSV")
    df_eas_eas_sum.to_csv("../data/20-Gipuzkoa/ZBE_eas.csv")
    df_eas_puy_sum.to_csv("../data/20-Gipuzkoa/ZBE_puy.csv")
    df_eas_ate_sum.to_csv("../data/20-Gipuzkoa/ZBE_ate.csv")
    df_eas_tol_sum.to_csv("../data/20-Gipuzkoa/ZBE_tol.csv")
 
    return