import inp
import imp
import exp
import logg

def start():
    print('controller')
    if inp.mod() == "1":
        info = inp.exp()
        exp.expp(info)
        logg.log_info(info)
    else:
        info = inp.exp()
        imp.impo(info)
        logg.log_info(info)

