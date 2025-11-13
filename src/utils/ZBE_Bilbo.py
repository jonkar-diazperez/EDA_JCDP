import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import funciones as f

 
def cargar_datos_ZBE_BIO():
    # DATOS ESTACIONES BILBAO
    df_bio_2024_maz = pd.read_csv("../data/48-Bizkaia/2024/MAZARREDO.csv", sep=';',encoding='latin_1')
    df_bio_2025_maz = pd.read_csv("../data/48-Bizkaia/2025/MAZARREDO.csv", sep=';',encoding='latin_1')

    df_bio_2024_mdh = pd.read_csv("../data/48-Bizkaia/2024/M_DIAZ_HARO.csv", sep=';',encoding='latin_1')
    df_bio_2025_mdh = pd.read_csv("../data/48-Bizkaia/2025/M_DIAZ_HARO.csv", sep=';',encoding='latin_1')

    df_bio_2024_eur = pd.read_csv("../data/48-Bizkaia/2024/EUROPA.csv", sep=';',encoding='latin_1')
    df_bio_2025_eur = pd.read_csv("../data/48-Bizkaia/2025/EUROPA.csv", sep=';',encoding='latin_1')

    df_bio_2024_um2 = pd.read_csv("../data/48-Bizkaia/2024/UNIDAD_MOVIL_2.csv", sep=';',encoding='latin_1')
    df_bio_2025_um2 = pd.read_csv("../data/48-Bizkaia/2025/UNIDAD_MOVIL_2.csv", sep=';',encoding='latin_1')

    df_bio_2024_bas = pd.read_csv("../data/48-Bizkaia/2024/BASAURI.csv", sep=';',encoding='latin_1')
    df_bio_2025_bas = pd.read_csv("../data/48-Bizkaia/2025/BASAURI.csv", sep=';',encoding='latin_1')

    df_bio_maz = pd.concat([df_bio_2025_maz,df_bio_2024_maz])
    df_bio_mdh = pd.concat([df_bio_2025_mdh,df_bio_2024_mdh])
    df_bio_eur = pd.concat([df_bio_2025_eur,df_bio_2024_eur])
    df_bio_um2 = pd.concat([df_bio_2025_um2,df_bio_2024_um2])
    df_bio_bas = pd.concat([df_bio_2025_bas,df_bio_2024_bas])
    #Tratamiento datasets
    print("Comienza proceso datasets estaciones Bilbo")
    print("Estación Mazarredo")
    df_bio_maz_sum = f.convertir_ICA(df_bio_maz)
    print("Estación Mª Díaz de HARO")
    df_bio_mdh_sum = f.convertir_ICA(df_bio_mdh)
    print("Estación EUROPA")
    df_bio_eur_sum = f.convertir_ICA(df_bio_eur)
    print("Estación Unidad Móvil 2")
    df_bio_um2_sum = f.convertir_ICA(df_bio_um2)
    print("Estación BASAURI")
    df_bio_bas_sum = f.convertir_ICA(df_bio_bas)
    print("Fin proceso datasets estaciones Bilbo")

    print("Exportamos a CSV")
    df_bio_maz_sum.to_csv("../data/48-Bizkaia/ZBE_maz.csv")
    df_bio_mdh_sum.to_csv("../data/48-Bizkaia/ZBE_mdh.csv")
    df_bio_eur_sum.to_csv("../data/48-Bizkaia/ZBE_eur.csv")
    df_bio_um2_sum.to_csv("../data/48-Bizkaia/ZBE_um2.csv")
    df_bio_bas_sum.to_csv("../data/48-Bizkaia/ZBE_bas.csv")
    
    return