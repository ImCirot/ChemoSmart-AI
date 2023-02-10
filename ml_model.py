#import librerie necessarie
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

def training_and_testing_models():
    #lettura dataset
    df = pd.read_csv('./dataset.csv')

    #drop delle caratteristiche inutili al modello
    df.drop('PatientId', inplace=True ,axis=1)
    df.drop('sesso', inplace=True ,axis=1)

    #setting delle feature
    features = ['eta', 'indice_inquinamento_ambientale','indice_uso_alcolici',
    'grado_allergia','grado_rischio_lavorativo','indice_fattori_rischio_familiare',
    'indice_malattie_croniche','indice_alimentazione_scorretta','indice_obesita',
    'grado_esposizione_fumo_attivo','grado_esposizione_fumo_passivo','indice_dolori_localizzati',
    'indice_emottisi','indice_astenia','indice_perdita_peso','indice_dispnea',
    'indice_respiro_sibilante','indice_disfagia','stato_dita_di_Ippocrate',
    'stato_immunodepressione','indice_tosse_secca','indice_russamento']
    
    #si trasforma il dataframe in un array per poter eseguire lo split della k-fold validation
    df_array = np.array(df)

    #si salva in X il dataframe sulle sole colonne feature
    X = df[features]

    #setting della variabile da predire 
    y = df['priorita']

    #setup del valore di k per la kfold validation
    kf = KFold(n_splits=10)
    
    #inizializzo i due modelli su cui effettuare training e testing
    clf = DecisionTreeClassifier()
    gnb = GaussianNB()

    #inizializzo contatore utile per identificare iterazione del metodo kfold
    i = 0

    #ciclo per la kfold validation
    for train_index, test_index in kf.split(df_array):
        i = i+1

        #si ottengono gli array di training e test sulla base degli indici ottenuti dall'iterazione k attuale
        X_train, X_test = X.loc[train_index], X.loc[test_index]
        y_train, y_test = y.loc[train_index], y.loc[test_index]

        #si allenano i due moduli tramite il set di training dell'iterazione k attuale
        clf.fit(X_train,y_train)
        gnb.fit(X_train,y_train)

        #stampa dei dataset di training e test
        print(f"Set training: {X_train}")
        print(f"Predict training: {y_train}")
        print(f"Set testing: {X_test}")
        print(f"Predict testing: {y_test}")

#chiamo la funzione iniziale
training_and_testing_models()