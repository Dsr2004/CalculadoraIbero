from django.views.generic import View
from django.shortcuts import render

class CalculadoraView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")
    
    def post(self, request, *args, **kwargs):
        tipo = request.POST.get("tipo_operacion", None)
        valor_1 = request.POST.get("valor_1", None)
        valor_2 = request.POST.get("valor_2", None)
        resultado = 0
        errores = []
        if not tipo:
            errores[{"tipo":"Especifique el tipo de la operación."}]
        if not valor_1:
            errores[{"valor_1":"Ingrese el primer valor."}]
        if not valor_2:
            errores[{"valor_2":"Ingrese el segundo valor."}]
        if type(valor_1) != int or type(valor_2) != int:
            errores[{"error_general":"Los valores deben ser números enteros."}]
        
        else:
            if tipo == "suma":
                resultado = int(valor_1) + int(valor_2)
            elif tipo == "resta":
                resultado = int(valor_1) - int(valor_2)
            elif tipo == "multiplicacion":
                resultado = int(valor_1) * int(valor_2)
            elif tipo == "division":
                if valor_2 == 0:
                    errores[{"valor_2":"No se puede dividir por cero."}]
                resultado = int(valor_1) / int(valor_2)
            elif tipo == "potencia":
                resultado = int(valor_1) ** int(valor_2)
            elif tipo == "modulo":
                resultado = int(valor_1) % int(valor_2)
            elif tipo == "raiz_cuadrada":
                resultado = int(valor_1) ** (1/int(valor_2))
        return render(request, "index.html", {"resultado": resultado, "errores": errores})

