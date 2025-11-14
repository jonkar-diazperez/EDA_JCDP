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

def graficos_ICA_ZBE_BIO():
    plt.style.use('seaborn-v0_8')

    df_bio_maz_sum = pd.read_csv("../data/48-Bizkaia/ZBE_maz.csv")
    df_bio_mdh_sum = pd.read_csv("../data/48-Bizkaia/ZBE_mdh.csv")
    df_bio_eur_sum = pd.read_csv("../data/48-Bizkaia/ZBE_eur.csv")
    df_bio_um2_sum = pd.read_csv("../data/48-Bizkaia/ZBE_um2.csv")
    df_bio_bas_sum = pd.read_csv("../data/48-Bizkaia/ZBE_bas.csv")
    # GRAFICOS ICA MAZ
    plt.figure()
    fig, ax = plt.subplots()
    ax.set(xlim=("2024-01-01","2025-06-01"), xticks=["2024-01-01", "2024-03-01","2024-06-01","2024-09-01","2025-01-01", "2025-03-01","2025-06-01"]);
    plt.axvline(x="2024-06-15", color='r', linestyle='--', linewidth=2);

    plt.figure()
    ax.stackplot(df_bio_maz_sum["Date"],df_bio_maz_sum["CO (mg/m3)"], linewidth=0.7);
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/MAZ_CO ICA.png", format="png")
    sns.boxplot(data = df_bio_maz_sum[df_bio_maz_sum["Date"] < "2024-06-15"], x = "CO (mg/m3)")  
    fig.savefig(fname="../img/48-Bizkaia/MAZ_CO ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_maz_sum[df_bio_maz_sum["Date"] >= "2024-06-15"], x = "CO (mg/m3)")
    fig.savefig(fname="../img/48-Bizkaia/MAZ_CO ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_maz_sum["Date"],df_bio_maz_sum["NO2"], linewidth=1.5,colors='g')
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/MAZ_NO2 ICA.png", format="png")
    sns.boxplot(data = df_bio_maz_sum[df_bio_maz_sum["Date"] < "2024-06-15"], x = "NO2",color='g')
    fig.savefig(fname="../img/48-Bizkaia/MAZ_NO2 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_maz_sum[df_bio_maz_sum["Date"] >= "2024-06-15"], x = "NO2",color='g')
    fig.savefig(fname="../img/48-Bizkaia/MAZ_NO2 ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_maz_sum["Date"],df_bio_maz_sum["SO2"], linewidth=0.7,colors='y')
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/MAZ_SO2 ICA.png", format="png")
    sns.boxplot(data = df_bio_maz_sum[df_bio_maz_sum["Date"] < "2024-06-15"], x = "SO2",color='y')
    fig.savefig(fname="../img/48-Bizkaia/MAZ_SO2 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_maz_sum[df_bio_maz_sum["Date"] >= "2024-06-15"], x = "SO2",color='y')
    fig.savefig(fname="../img/48-Bizkaia/MAZ_SO2 ICA_boxplot 2025.png", format="png")
 
    plt.figure()
    ax.stackplot(df_bio_maz_sum["Date"],df_bio_maz_sum["PM10"], linewidth=0.7,colors='m');
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/MAZ_PM10 ICA.png", format="png")
    sns.boxplot(data = df_bio_maz_sum[df_bio_maz_sum["Date"] < "2024-06-15"], x = "PM10",color='m')
    fig.savefig(fname="../img/48-Bizkaia/MAZ_PM10 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_maz_sum[df_bio_maz_sum["Date"] >= "2024-06-15"], x = "PM10",color='m')
    fig.savefig(fname="../img/48-Bizkaia/MAZ_PM10 ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_maz_sum["Date"],df_bio_maz_sum["PM2,5"], linewidth=0.7,colors='c');
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/MAZ_PM2-5 ICA.png", format="png")
    sns.boxplot(data = df_bio_maz_sum[df_bio_maz_sum["Date"] < "2024-06-15"], x = "PM2,5",color='c')
    fig.savefig(fname="../img/48-Bizkaia/MAZ_PM2-5 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_maz_sum[df_bio_maz_sum["Date"] >= "2024-06-15"], x = "PM2,5",color='c')
    fig.savefig(fname="../img/48-Bizkaia/MAZ_PM2-5 ICA_boxplot 2025.png", format="png")
    
    # GRAFICOS ICA MDH
    plt.figure()
    fig, ax = plt.subplots()
    ax.set(xlim=("2024-01-01","2025-06-01"), xticks=["2024-01-01", "2024-03-01","2024-06-01","2024-09-01","2025-01-01", "2025-03-01","2025-06-01"]);
    plt.axvline(x="2024-06-15", color='r', linestyle='--', linewidth=2);

    plt.figure()
    ax.stackplot(df_bio_mdh_sum["Date"],df_bio_mdh_sum["CO (mg/m3)"], linewidth=0.7);
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/mdh_CO ICA.png", format="png")
    sns.boxplot(data = df_bio_mdh_sum[df_bio_mdh_sum["Date"] < "2024-06-15"], x = "CO (mg/m3)")  
    fig.savefig(fname="../img/48-Bizkaia/mdh_CO ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_mdh_sum[df_bio_mdh_sum["Date"] >= "2024-06-15"], x = "CO (mg/m3)")
    fig.savefig(fname="../img/48-Bizkaia/mdh_CO ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_mdh_sum["Date"],df_bio_mdh_sum["NO2"], linewidth=1.5,colors='g')
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/mdh_NO2 ICA.png", format="png")
    sns.boxplot(data = df_bio_mdh_sum[df_bio_mdh_sum["Date"] < "2024-06-15"], x = "NO2",color='g')
    fig.savefig(fname="../img/48-Bizkaia/mdh_NO2 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_mdh_sum[df_bio_mdh_sum["Date"] >= "2024-06-15"], x = "NO2",color='g')
    fig.savefig(fname="../img/48-Bizkaia/mdh_NO2 ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_mdh_sum["Date"],df_bio_mdh_sum["SO2"], linewidth=0.7,colors='y')
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/mdh_SO2 ICA.png", format="png")
    sns.boxplot(data = df_bio_mdh_sum[df_bio_mdh_sum["Date"] < "2024-06-15"], x = "SO2",color='y')
    fig.savefig(fname="../img/48-Bizkaia/mdh_SO2 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_mdh_sum[df_bio_mdh_sum["Date"] >= "2024-06-15"], x = "SO2",color='y')
    fig.savefig(fname="../img/48-Bizkaia/mdh_SO2 ICA_boxplot 2025.png", format="png")
 
    plt.figure()
    ax.stackplot(df_bio_mdh_sum["Date"],df_bio_mdh_sum["PM10"], linewidth=0.7,colors='m');
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/mdh_PM10 ICA.png", format="png")
    sns.boxplot(data = df_bio_mdh_sum[df_bio_mdh_sum["Date"] < "2024-06-15"], x = "PM10",color='m')
    fig.savefig(fname="../img/48-Bizkaia/mdh_PM10 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_mdh_sum[df_bio_mdh_sum["Date"] >= "2024-06-15"], x = "PM10",color='m')
    fig.savefig(fname="../img/48-Bizkaia/mdh_PM10 ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_mdh_sum["Date"],df_bio_mdh_sum["PM2,5"], linewidth=0.7,colors='c');
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/mdh_PM2-5 ICA.png", format="png")
    sns.boxplot(data = df_bio_mdh_sum[df_bio_mdh_sum["Date"] < "2024-06-15"], x = "PM2,5",color='c')
    fig.savefig(fname="../img/48-Bizkaia/mdh_PM2-5 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_mdh_sum[df_bio_mdh_sum["Date"] >= "2024-06-15"], x = "PM2,5",color='c')
    fig.savefig(fname="../img/48-Bizkaia/mdh_PM2-5 ICA_boxplot 2025.png", format="png")

    # GRAFICOS ICA EUR
    plt.figure()
    fig, ax = plt.subplots()
    ax.set(xlim=("2024-01-01","2025-06-01"), xticks=["2024-01-01", "2024-03-01","2024-06-01","2024-09-01","2025-01-01", "2025-03-01","2025-06-01"]);
    plt.axvline(x="2024-06-15", color='r', linestyle='--', linewidth=2);

    plt.figure()
    ax.stackplot(df_bio_eur_sum["Date"],df_bio_eur_sum["CO (mg/m3)"], linewidth=0.7);
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/eur_CO ICA.png", format="png")
    sns.boxplot(data = df_bio_eur_sum[df_bio_eur_sum["Date"] < "2024-06-15"], x = "CO (mg/m3)")  
    fig.savefig(fname="../img/48-Bizkaia/eur_CO ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_eur_sum[df_bio_eur_sum["Date"] >= "2024-06-15"], x = "CO (mg/m3)")
    fig.savefig(fname="../img/48-Bizkaia/eur_CO ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_eur_sum["Date"],df_bio_eur_sum["NO2"], linewidth=1.5,colors='g')
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/eur_NO2 ICA.png", format="png")
    sns.boxplot(data = df_bio_eur_sum[df_bio_eur_sum["Date"] < "2024-06-15"], x = "NO2",color='g')
    fig.savefig(fname="../img/48-Bizkaia/eur_NO2 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_eur_sum[df_bio_eur_sum["Date"] >= "2024-06-15"], x = "NO2",color='g')
    fig.savefig(fname="../img/48-Bizkaia/eur_NO2 ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_eur_sum["Date"],df_bio_eur_sum["SO2"], linewidth=0.7,colors='y')
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/eur_SO2 ICA.png", format="png")
    sns.boxplot(data = df_bio_eur_sum[df_bio_eur_sum["Date"] < "2024-06-15"], x = "SO2",color='y')
    fig.savefig(fname="../img/48-Bizkaia/eur_SO2 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_eur_sum[df_bio_eur_sum["Date"] >= "2024-06-15"], x = "SO2",color='y')
    fig.savefig(fname="../img/48-Bizkaia/eur_SO2 ICA_boxplot 2025.png", format="png")
 
    plt.figure()
    ax.stackplot(df_bio_eur_sum["Date"],df_bio_eur_sum["PM10"], linewidth=0.7,colors='m');
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/eur_PM10 ICA.png", format="png")
    sns.boxplot(data = df_bio_eur_sum[df_bio_eur_sum["Date"] < "2024-06-15"], x = "PM10",color='m')
    fig.savefig(fname="../img/48-Bizkaia/eur_PM10 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_eur_sum[df_bio_eur_sum["Date"] >= "2024-06-15"], x = "PM10",color='m')
    fig.savefig(fname="../img/48-Bizkaia/eur_PM10 ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_eur_sum["Date"],df_bio_eur_sum["PM2,5"], linewidth=0.7,colors='c');
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/eur_PM2-5 ICA.png", format="png")
    sns.boxplot(data = df_bio_eur_sum[df_bio_eur_sum["Date"] < "2024-06-15"], x = "PM2,5",color='c')
    fig.savefig(fname="../img/48-Bizkaia/eur_PM2-5 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_eur_sum[df_bio_eur_sum["Date"] >= "2024-06-15"], x = "PM2,5",color='c')
    fig.savefig(fname="../img/48-Bizkaia/eur_PM2-5 ICA_boxplot 2025.png", format="png")
        
    # GRAFICOS ICA UM2
    plt.figure()
    fig, ax = plt.subplots()
    ax.set(xlim=("2024-01-01","2025-06-01"), xticks=["2024-01-01", "2024-03-01","2024-06-01","2024-09-01","2025-01-01", "2025-03-01","2025-06-01"]);
    plt.axvline(x="2024-06-15", color='r', linestyle='--', linewidth=2);

    plt.figure()
    ax.stackplot(df_bio_um2_sum["Date"],df_bio_um2_sum["CO (mg/m3)"], linewidth=0.7);
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/um2_CO ICA.png", format="png")
    sns.boxplot(data = df_bio_um2_sum[df_bio_um2_sum["Date"] < "2024-06-15"], x = "CO (mg/m3)")  
    fig.savefig(fname="../img/48-Bizkaia/um2_CO ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_um2_sum[df_bio_um2_sum["Date"] >= "2024-06-15"], x = "CO (mg/m3)")
    fig.savefig(fname="../img/48-Bizkaia/um2_CO ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_um2_sum["Date"],df_bio_um2_sum["NO2"], linewidth=1.5,colors='g')
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/um2_NO2 ICA.png", format="png")
    sns.boxplot(data = df_bio_um2_sum[df_bio_um2_sum["Date"] < "2024-06-15"], x = "NO2",color='g')
    fig.savefig(fname="../img/48-Bizkaia/um2_NO2 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_um2_sum[df_bio_um2_sum["Date"] >= "2024-06-15"], x = "NO2",color='g')
    fig.savefig(fname="../img/48-Bizkaia/um2_NO2 ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_um2_sum["Date"],df_bio_um2_sum["SO2"], linewidth=0.7,colors='y')
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/um2_SO2 ICA.png", format="png")
    sns.boxplot(data = df_bio_um2_sum[df_bio_um2_sum["Date"] < "2024-06-15"], x = "SO2",color='y')
    fig.savefig(fname="../img/48-Bizkaia/um2_SO2 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_um2_sum[df_bio_um2_sum["Date"] >= "2024-06-15"], x = "SO2",color='y')
    fig.savefig(fname="../img/48-Bizkaia/um2_SO2 ICA_boxplot 2025.png", format="png")
 
    plt.figure()
    ax.stackplot(df_bio_um2_sum["Date"],df_bio_um2_sum["PM10"], linewidth=0.7,colors='m');
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/um2_PM10 ICA.png", format="png")
    sns.boxplot(data = df_bio_um2_sum[df_bio_um2_sum["Date"] < "2024-06-15"], x = "PM10",color='m')
    fig.savefig(fname="../img/48-Bizkaia/um2_PM10 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_um2_sum[df_bio_um2_sum["Date"] >= "2024-06-15"], x = "PM10",color='m')
    fig.savefig(fname="../img/48-Bizkaia/um2_PM10 ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_um2_sum["Date"],df_bio_um2_sum["PM2,5"], linewidth=0.7,colors='c');
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/um2_PM2-5 ICA.png", format="png")
    sns.boxplot(data = df_bio_um2_sum[df_bio_um2_sum["Date"] < "2024-06-15"], x = "PM2,5",color='c')
    fig.savefig(fname="../img/48-Bizkaia/um2_PM2-5 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_um2_sum[df_bio_um2_sum["Date"] >= "2024-06-15"], x = "PM2,5",color='c')
    fig.savefig(fname="../img/48-Bizkaia/um2_PM2-5 ICA_boxplot 2025.png", format="png")
        
    # GRAFICOS ICA BAS    
    plt.figure()
    fig, ax = plt.subplots()
    ax.set(xlim=("2024-01-01","2025-06-01"), xticks=["2024-01-01", "2024-03-01","2024-06-01","2024-09-01","2025-01-01", "2025-03-01","2025-06-01"]);
    plt.axvline(x="2024-06-15", color='r', linestyle='--', linewidth=2);

    plt.figure()
    ax.stackplot(df_bio_bas_sum["Date"],df_bio_bas_sum["CO (mg/m3)"], linewidth=0.7);
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/bas_CO ICA.png", format="png")
    sns.boxplot(data = df_bio_bas_sum[df_bio_bas_sum["Date"] < "2024-06-15"], x = "CO (mg/m3)")  
    fig.savefig(fname="../img/48-Bizkaia/bas_CO ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_bas_sum[df_bio_bas_sum["Date"] >= "2024-06-15"], x = "CO (mg/m3)")
    fig.savefig(fname="../img/48-Bizkaia/bas_CO ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_bas_sum["Date"],df_bio_bas_sum["NO2"], linewidth=1.5,colors='g')
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/bas_NO2 ICA.png", format="png")
    sns.boxplot(data = df_bio_bas_sum[df_bio_bas_sum["Date"] < "2024-06-15"], x = "NO2",color='g')
    fig.savefig(fname="../img/48-Bizkaia/bas_NO2 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_bas_sum[df_bio_bas_sum["Date"] >= "2024-06-15"], x = "NO2",color='g')
    fig.savefig(fname="../img/48-Bizkaia/bas_NO2 ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_bas_sum["Date"],df_bio_bas_sum["SO2"], linewidth=0.7,colors='y')
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/bas_SO2 ICA.png", format="png")
    sns.boxplot(data = df_bio_bas_sum[df_bio_bas_sum["Date"] < "2024-06-15"], x = "SO2",color='y')
    fig.savefig(fname="../img/48-Bizkaia/bas_SO2 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_bas_sum[df_bio_bas_sum["Date"] >= "2024-06-15"], x = "SO2",color='y')
    fig.savefig(fname="../img/48-Bizkaia/bas_SO2 ICA_boxplot 2025.png", format="png")
 
    plt.figure()
    ax.stackplot(df_bio_bas_sum["Date"],df_bio_bas_sum["PM10"], linewidth=0.7,colors='m');
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/bas_PM10 ICA.png", format="png")
    sns.boxplot(data = df_bio_bas_sum[df_bio_bas_sum["Date"] < "2024-06-15"], x = "PM10",color='m')
    fig.savefig(fname="../img/48-Bizkaia/bas_PM10 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_bas_sum[df_bio_bas_sum["Date"] >= "2024-06-15"], x = "PM10",color='m')
    fig.savefig(fname="../img/48-Bizkaia/bas_PM10 ICA_boxplot 2025.png", format="png")
    
    plt.figure()
    ax.stackplot(df_bio_bas_sum["Date"],df_bio_bas_sum["PM2,5"], linewidth=0.7,colors='c');
    plt.show()
    fig.savefig(fname="../img/48-Bizkaia/bas_PM2-5 ICA.png", format="png")
    sns.boxplot(data = df_bio_bas_sum[df_bio_bas_sum["Date"] < "2024-06-15"], x = "PM2,5",color='c')
    fig.savefig(fname="../img/48-Bizkaia/bas_PM2-5 ICA_boxplot 2024.png", format="png")
    sns.boxplot(data = df_bio_bas_sum[df_bio_bas_sum["Date"] >= "2024-06-15"], x = "PM2,5",color='c')
    fig.savefig(fname="../img/48-Bizkaia/bas_PM2-5 ICA_boxplot 2025.png", format="png")
    
    return 