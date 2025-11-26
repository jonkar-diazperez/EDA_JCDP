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

def graficos_ICA_ZBE_DON():
    plt.style.use('seaborn-v0_8')

    df_eas_eas_sum = pd.read_csv("../data/20-Gipuzkoa/ZBE_eas.csv")
    df_eas_puy_sum = pd.read_csv("../data/20-Gipuzkoa/ZBE_puy.csv")
    df_eas_ate_sum = pd.read_csv("../data/20-Gipuzkoa/ZBE_ate.csv")
    df_eas_tol_sum = pd.read_csv("../data/20-Gipuzkoa/ZBE_tol.csv")

    # GRAFICOS ICA EAS
    fig = plt.figure()
    plt.title("EASO - CO")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,1)
    sns.boxplot(data = df_eas_eas_sum[df_eas_eas_sum["Date"] < "2025-01-01"], x = "CO (mg/m3)")
    plt.xlim(0,0.7)
    plt.ylabel("2024")
    plt.xlabel("")
    plt.subplot(2,1,2)
    sns.boxplot(data = df_eas_eas_sum[df_eas_eas_sum["Date"] >= "2025-01-01"], x = "CO (mg/m3)")
    plt.xlim(0,0.7)
    plt.ylabel("2025")
    plt.xlabel("")
    fig.savefig(fname="../img/20-Gipuzkoa/eas_CO ICA.png", format="png")
    

    fig = plt.figure()
    plt.title("EASO - NO2")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,1)
    sns.boxplot(data = df_eas_eas_sum[df_eas_eas_sum["Date"] < "2025-01-01"], x = "NO2",color='g');
    plt.xlim(0,50)
    plt.ylabel("2024")
    plt.xlabel("")
    plt.subplot(2,1,2)
    sns.boxplot(data = df_eas_eas_sum[df_eas_eas_sum["Date"] >= "2025-01-01"], x = "NO2",color='g');
    plt.xlim(0,50)
    plt.ylabel("2025")
    plt.xlabel("")
    fig.savefig(fname="../img/20-Gipuzkoa/eas_NO2 ICA.png", format="png")

    fig = plt.figure()
    plt.title("EASO - SO2")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,1)
    sns.boxplot(data = df_eas_eas_sum[df_eas_eas_sum["Date"] < "2025-01-01"], x = "SO2",color='y')
    plt.xlim(0,10)
    plt.ylabel("2024")
    plt.xlabel("")
    plt.subplot(2,1,2)
    sns.boxplot(data = df_eas_eas_sum[df_eas_eas_sum["Date"] >= "2025-01-01"], x = "SO2",color='y')
    plt.xlim(0,10)
    plt.ylabel("2025")
    plt.xlabel("")
    fig.savefig(fname="../img/20-Gipuzkoa/eas_SO2 ICA.png", format="png")

    fig = plt.figure()
    plt.title("EASO - PM 10")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,1)
    sns.boxplot(data = df_eas_eas_sum[df_eas_eas_sum["Date"] < "2025-01-01"], x = "PM10",color='m')
    plt.xlim(0,40)
    plt.ylabel("2024")
    plt.xlabel("")
    plt.subplot(2,1,2)
    sns.boxplot(data = df_eas_eas_sum[df_eas_eas_sum["Date"] >= "2025-01-01"], x = "PM10",color='m')
    plt.xlim(0,40)
    plt.ylabel("2025")
    plt.xlabel("")
    fig.savefig(fname="../img/20-Gipuzkoa/eas_PM10 ICA.png", format="png")

    fig = plt.figure()
    plt.title("EASO - PM 2,5")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,1)
    sns.boxplot(data = df_eas_eas_sum[df_eas_eas_sum["Date"] < "2025-01-01"], x = "PM2,5",color='c')
    plt.xlim(0,30)
    plt.ylabel("2024")
    plt.xlabel("")
    plt.subplot(2,1,2)
    sns.boxplot(data = df_eas_eas_sum[df_eas_eas_sum["Date"] >= "2025-01-01"], x = "PM2,5",color='c')
    plt.xlim(0,30)
    plt.ylabel("2025")
    plt.xlabel("")
    fig.savefig(fname="../img/20-Gipuzkoa/eas_PM2-5 ICA.png", format="png")

    # GRAFICOS ICA PUYO
    fig = plt.figure()
    plt.title("PUYO - OZONO")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,1)
    sns.boxplot(data = df_eas_puy_sum[df_eas_puy_sum["Date"] < "2025-01-01"], x = "OZONO")
    plt.xlim(0,100)
    plt.ylabel("2024")
    plt.xlabel("")
    plt.subplot(2,1,2)
    sns.boxplot(data = df_eas_puy_sum[df_eas_puy_sum["Date"] >= "2025-01-01"], x = "OZONO")
    plt.xlim(0,100)
    plt.ylabel("2025")
    plt.xlabel("")
    fig.savefig(fname="../img/20-Gipuzkoa/puy_OZONO ICA.png", format="png")
    

    fig = plt.figure()
    plt.title("PUYO - NO2")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,1)
    sns.boxplot(data = df_eas_puy_sum[df_eas_puy_sum["Date"] < "2025-01-01"], x = "NO2",color='g');
    plt.xlim(0,50)
    plt.ylabel("2024")
    plt.xlabel("")
    plt.subplot(2,1,2)
    sns.boxplot(data = df_eas_puy_sum[df_eas_puy_sum["Date"] >= "2025-01-01"], x = "NO2",color='g');
    plt.xlim(0,50)
    plt.ylabel("2025")
    plt.xlabel("")
    fig.savefig(fname="../img/20-Gipuzkoa/puy_NO2 ICA.png", format="png")

    fig = plt.figure()
    plt.title("PUYO - SO2")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,1)
    sns.boxplot(data = df_eas_puy_sum[df_eas_puy_sum["Date"] < "2025-01-01"], x = "SO2",color='y')
    plt.xlim(0,10)
    plt.ylabel("2024")
    plt.xlabel("")
    plt.subplot(2,1,2)
    sns.boxplot(data = df_eas_puy_sum[df_eas_puy_sum["Date"] >= "2025-01-01"], x = "SO2",color='y')
    plt.xlim(0,10)
    plt.ylabel("2025")
    plt.xlabel("")
    fig.savefig(fname="../img/20-Gipuzkoa/puy_SO2 ICA.png", format="png")

    fig = plt.figure()
    plt.title("PUYO - PM 10")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,1)
    sns.boxplot(data = df_eas_puy_sum[df_eas_puy_sum["Date"] < "2025-01-01"], x = "PM10",color='m')
    plt.xlim(0,40)
    plt.ylabel("2024")
    plt.xlabel("")
    plt.subplot(2,1,2)
    sns.boxplot(data = df_eas_puy_sum[df_eas_puy_sum["Date"] >= "2025-01-01"], x = "PM10",color='m')
    plt.xlim(0,40)
    plt.ylabel("2025")
    plt.xlabel("")
    fig.savefig(fname="../img/20-Gipuzkoa/puy_PM10 ICA.png", format="png")

    fig = plt.figure()
    plt.title("PUYO - PM 2,5")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,1)
    sns.boxplot(data = df_eas_puy_sum[df_eas_puy_sum["Date"] < "2025-01-01"], x = "PM2,5",color='c')
    plt.xlim(0,30)
    plt.ylabel("2024")
    plt.xlabel("")
    plt.subplot(2,1,2)
    sns.boxplot(data = df_eas_puy_sum[df_eas_puy_sum["Date"] >= "2025-01-01"], x = "PM2,5",color='c')
    plt.xlim(0,30)
    plt.ylabel("2025")
    plt.xlabel("")
    fig.savefig(fname="../img/20-Gipuzkoa/puy_PM2-5 ICA.png", format="png")  

    # GRAFICOS ICA ATE
        
    # GRAFICOS ICA TOL    
    
    return 