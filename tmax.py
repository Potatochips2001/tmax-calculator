import math

def tmax(absorption, elimination):
    if absorption == elimination:
        return "absorption and elimination cannot be the same"
    ka = math.log(2)/absorption
    ke = math.log(2)/elimination
    lnka = math.log(ka)
    lnke = math.log(ke)
    tmax_ = ((lnka-lnke)/(ka-ke))
    return tmax_
