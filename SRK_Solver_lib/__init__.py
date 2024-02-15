from ctypes import *

lib = cdll.LoadLibrary(r"DLL1.dll")


def levy_flights(dt_sav, t, alpha, dt, eta_a, tau_e):
    result = lib.Levy_Flights(c_double(dt_sav), c_int(t), c_double(alpha), c_double(dt), c_double(eta_a),
                              c_double(tau_e))
    print('Результат моделирования в файле model_Levy_Flights.data')
    return result
