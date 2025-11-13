import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import funciones as f

 
def cargar_datos_ZBE_GAS():
    # DATOS ESTACIONES GASTEIZ
    """
    df_vit_2024_3dm = pd.read_csv("../data/01-Araba/2024/3_DE_MARZO.csv", sep=';',encoding='latin_1')
    df_vit_2025_3dm = pd.read_csv("../data/01-Araba/2025/3_DE_MARZO.csv", sep=';',encoding='latin_1')

    df_vit_2024_gas = pd.read_csv("../data/01-Araba/2024/AV_GASTEIZ.csv", sep=';',encoding='latin_1')
    df_vit_2025_gas = pd.read_csv("../data/01-Araba/2025/AV_GASTEIZ.csv", sep=';',encoding='latin_1')

    df_vit_2024_her = pd.read_csv("../data/01-Araba/2024/LOS_HERRAN.csv", sep=';',encoding='latin_1')
    df_vit_2025_her = pd.read_csv("../data/01-Araba/2025/LOS_HERRAN.csv", sep=';',encoding='latin_1')

    df_vit_2024_far = pd.read_csv("../data/01-Araba/2024/FARMACIA.csv", sep=';',encoding='latin_1')
    df_vit_2025_far = pd.read_csv("../data/01-Araba/2025/FARMACIA.csv", sep=';',encoding='latin_1')
    """
    df_vit_3dm = pd.read_csv("../data/01-Araba/2025/3_DE_MARZO.csv", sep=';',encoding='latin_1')
    df_vit_gas = pd.read_csv("../data/01-Araba/2025/AV_GASTEIZ.csv", sep=';',encoding='latin_1')
    df_vit_her = pd.read_csv("../data/01-Araba/2025/LOS_HERRAN.csv", sep=';',encoding='latin_1')
    df_vit_far = pd.read_csv("../data/01-Araba/2025/FARMACIA.csv", sep=';',encoding='latin_1')
    
    #Tratamiento datasets
    print("Comienza proceso datasets estaciones Gasteiz")
    print("Estación 3 DE MARZO")
    df_vit_3dm_sum = f.convertir_ICA(df_vit_3dm)
    print("Estación AVDA GASTEIZ")
    df_vit_gas_sum = f.convertir_ICA(df_vit_gas)
    print("Estación LOS HERRÁN")
    df_vit_her_sum = f.convertir_ICA(df_vit_her)
    print("Estación FARMACIA")
    df_vit_far_sum = f.convertir_ICA(df_vit_far)
   
    print("Fin proceso datasets estaciones Gasteiz")

    print("Exportamos a CSV")
    df_vit_3dm_sum.to_csv("../data/01-Araba/ZBE_3dm.csv")
    df_vit_gas_sum.to_csv("../data/01-Araba/ZBE_gas.csv")
    df_vit_her_sum.to_csv("../data/01-Araba/ZBE_her.csv")
    df_vit_far_sum.to_csv("../data/01-Araba/ZBE_far.csv")
 
    return