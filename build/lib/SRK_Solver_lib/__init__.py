from ctypes import *
import pandas as pd

lib = cdll.LoadLibrary(r"DLL1.dll")


def levy_flights(dt_sav, t, alpha, dt, eta_a, tau_e):
    result = lib.Levy_Flights(c_double(dt_sav), c_int(t), c_double(alpha), c_double(dt), c_double(eta_a),
                              c_double(tau_e))
    print('Результат моделирования сохранены в файле model_Levy_Flights.data')
    file = open('model_Levy_Flights.data', 'r')
    t = []
    X = []
    Y = []
    f = 0
    for line in file:
        if f == 0:
            f = 1
        else:
            temp = line.split(';')
            t.append(temp[0])
            X.append(temp[1])
            Y.append(temp[2])
    df = pd.DataFrame({"time": t,
                       "X[1]": X,
                       "Y[1]": Y})
    df['time'] = df['time'].astype(float)
    df['X[1]'] = df['X[1]'].astype(float)
    df['Y[1]'] = df['Y[1]'].astype(float)
    return df
