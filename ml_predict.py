#import librerie necessarie
import pandas as pd
import pickle 

def predict():
    #viene deserializzato il modello
    loaded_module = pickle.load(open('trained_model.sav','rb'))

    #viene caricato il csv contenente il paziente da predire
    patient = pd.read_csv('./predict.csv')
    #vengono eliminate dal dataset le colonne inutili alla predizione
    patient.drop(['id','sesso','priorita'], inplace=True, axis=1)

    #predizione e stampa di quest'ultima
    prediction = loaded_module.predict(patient)
    print(prediction[0])

#chiamo la funzione iniziale
predict()