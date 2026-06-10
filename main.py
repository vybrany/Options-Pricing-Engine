from products import (
    vanilla,
    monte_carlo_product,
    american_product,
    up_and_out_product,
    asian_produit,
    crr_product
)

from models import (
    monte_carlo,
    binomial_crr,
    black_scholes,
    monte_carlo_asian,
    up_and_out,
    american
)

from values import values


def price_option(params, product, model, option_type):
    if option_type not in ["call", "put"]:
        return "Err: option_type must be 'call' or 'put'"

    if product == "vanilla":
        if model == "black_scholes":
            return vanilla(params, black_scholes, option_type)

        elif model == "monte_carlo":
            return monte_carlo_product(params, monte_carlo, option_type)

        elif model == "crr":
            return crr_product(params, binomial_crr, option_type)

        else:
            return "Err: vanilla can be priced with black_scholes, monte_carlo or crr"

    elif product == "american":
        if model != "crr":
            return "Err: american option is priced only with crr"

        elif option_type != "put":
            return "Err: only american put is implemented"

        return american_product(params, american)

    elif product == "asian":
        if model != "monte_carlo":
            return "Err: asian option is priced only with monte_carlo"

        return asian_produit(params, monte_carlo_asian, option_type)

    elif product == "barrier":
        if model != "monte_carlo":
            return "Err: barrier option is priced only with monte_carlo"

        return up_and_out_product(params, up_and_out, option_type)

    else:
        return "Err: unknown product"



params = values()

product = input("Product (vanilla / american / asian / barrier): ")
model = input("Model (black_scholes / monte_carlo / crr): ")
option_type = input("Type (call / put): ")

price = price_option(params, product, model, option_type)

print("Option price:", price)