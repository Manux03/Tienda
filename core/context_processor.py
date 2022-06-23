def total_carrito(request):
    total = 0
    if request:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    return {"total_carrito": total}

def total_productos(request):
    suma = 0
    if request:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                suma += int(value["cantidad"])
    return {"total_productos": suma}