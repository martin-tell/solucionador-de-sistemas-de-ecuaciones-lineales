from tkinter import Tk, Frame, Label, Text, Button, END
from tkinter.ttk import Combobox
from numpy import size
from metodos_resolucion import eliminacion_gaussiana, pivoteo_escalado_columna, pivoteo_maximo_columnas, matriz_a_cadena

class Interfaz:

    def __init__(self) -> None:
        self.metodos = (eliminacion_gaussiana, pivoteo_maximo_columnas, pivoteo_escalado_columna)
        self.solucion = ""
        self.ventana = Tk()
        self.ventana.title("Sistemas de Ecuaciones Lineales")
        self.ventana.resizable(0, 0)

        self.panel_base = Frame()
        self.panel_base.pack()

        Label(self.panel_base, text="Ingrese las ecuaciones").grid(row=0, column=0, columnspan=5)
        self.entrada_ecuaciones = Text(self.panel_base, height=10)
        self.entrada_ecuaciones.grid(row=1, column=0, columnspan=5, padx=10)

        Label(self.panel_base, text="Proceso y Soluciones").grid(row=2, column=0, columnspan=5)
        self.resultados = Text(self.panel_base, height=15)
        self.resultados.grid(row=3, column=0, columnspan=5, padx=10)

        Label(self.panel_base, text="Método: ").grid(row=4, column=0)
        self.lista_metodos = Combobox(self.panel_base)
        self.lista_metodos['values'] = ("Eliminación Gaussiana con sustitución hacia atrás",
                                "Eliminación Gaussiana con Pivoteo Máximo de Columnas",
                                "Eliminación Gaussiana con Pivoteo Escalado de Columna")
        self.lista_metodos.config(width=50)
        self.lista_metodos.current(0)
        self.lista_metodos.grid(row=4, column=1)

        self.boton_solucionar = Button(self.panel_base, text="Solucionar", command=self.solucionar)
        self.boton_solucionar.grid(row=4, column=4, pady=10)

        self.ventana.mainloop()

    def construye_matriz(self):
        matriz = list()
        cadena_entrada = self.entrada_ecuaciones.get(1.0, "end-1c")
        ecuaciones = cadena_entrada.split('\n')
        negativo = False
        for ecuacion in ecuaciones:
            fila = list()
            elementos = ecuacion.split(' ')
            for x in elementos:
                try:
                    numero = float(x)
                    if negativo:
                        numero *= -1
                        negativo = False
                    fila.append(numero)
                except (Exception,):
                    if x == '-':
                        negativo = True
            matriz.append(fila)
        return matriz

    def solucionar(self):
        self.solucion = ""
        self.resultados.delete("1.0", END)
        m = self.metodos[self.lista_metodos.current()]
        matriz = self.construye_matriz()        
        soluciones, proceso = m(len(matriz), matriz)
        if size(soluciones) != 0:
            soluciones = "".join(str(s)+'\t' for s in soluciones)
        else:
            soluciones = "No hay solución unica"
        for m in proceso:
            self.solucion += matriz_a_cadena(m)
        self.solucion += soluciones
        self.resultados.insert("end", self.solucion)

if __name__ == "__main__":
    Interfaz()