from models import monte_carlo, binomial_crr, black_scholes, monte_carlo_asian, up_and_out, american
from values import values





def vanilla(values, model, call_or_put):
    call, put = model(values)

    if call_or_put == "call":
        return call
    elif call_or_put == "put":
        return put
    else:
        return "Err"


def monte_carlo_product(values,model,call_or_put):
    call, put , S = model(values)

    if call_or_put == "call":
        return call
    elif call_or_put == "put":
        return put
    else:
        return "Err"


def crr_product(values,model,call_or_put):
    call, put  = model(values)

    if call_or_put == "call":
        return call
    elif call_or_put == "put":
        return put
    else:
        return "Err"

def american_product(values, model):
    put = model(values)
    return put


def asian_produit(values, model,call_or_put):
    call, put = model(values)

    if call_or_put == "call":
        return call
    elif call_or_put == "put":
        return put
    else:
        return "Err"
    
    
def up_and_out_product(values, model ,call_or_put):
    call, put = model(values)

    if call_or_put == "call":
        return call
    elif call_or_put == "put":
        return put
    else:
        return "Err"
    
