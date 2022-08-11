
import tkinter as tk

from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x335')
        self.resizable(0,0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        #Atributos de Clase
        self.expresion = ''

        #Caja de texto (input)
        self.entrada = None
        #StringVar lo utilizamos para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        #Creamo0s los componentes
        self._creacion_de_componentes()

    def _creacion_de_componentes(self):
        #Creamos un frame
        frame1 = tk.Frame(self,width=400,height=50,bg='grey')
        frame1.pack(side=tk.TOP)
        #Caja de texto
        entrada = tk.Entry(frame1,font=('arial',18,'bold'),
                           textvariable=self.entrada_texto,width=30,justify=tk.RIGHT)
        entrada.grid(row=0,column=0,ipady=10)
        #Segundo frame
        botones_frame = tk.Frame(self,width=400,height=450,bg='grey')
        botones_frame.pack()
        #Primer reglon
        boton_c = tk.Button(botones_frame,text='C',width=42,height=3,
                            bd=0,bg='#eee',cursor='hand2',command=self._evento_limpiar)
        boton_c.grid(row=0,column=0,columnspan=3,padx=1,pady=1)

        boton_div = tk.Button(botones_frame,text="/",width=9,height=3,bd=0,bg='#eee',cursor='hand2',
                             command=lambda: self._evento_click('/'))
        boton_div.grid(row=0,column=3,padx=1,pady=1)
        #Segundo reglon
        boton_7 = tk.Button(botones_frame,text='7',width=13,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda: self._evento_click(7))
        boton_7.grid(row=1,column=0,padx=1,pady=1)
        boton_8 = tk.Button(botones_frame, text='8', width=13, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(8))
        boton_8.grid(row=1, column=1, padx=1, pady=1)
        boton_9 = tk.Button(botones_frame, text='9', width=13, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(9))
        boton_9.grid(row=1, column=2, padx=1, pady=1)
        boton_multiplicar = tk.Button(botones_frame, text="*", width=9, height=3, bd=0, bg='#eee', cursor='hand2',
                              command=lambda: self._evento_click('*'))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)
        #Tercer reglon
        boton_4 = tk.Button(botones_frame, text='4', width=13, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(4)).grid(row=2, column=0, padx=1, pady=1)
        boton_5 = tk.Button(botones_frame, text='5', width=13, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(5)).grid(row=2, column=1, padx=1, pady=1)
        boton_6 = tk.Button(botones_frame, text='6', width=13, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(6)).grid(row=2, column=2, padx=1, pady=1)
        boton_resta = tk.Button(botones_frame, text="-", width=9, height=3, bd=0, bg='#eee', cursor='hand2',
                              command=lambda: self._evento_click('-'))
        boton_resta.grid(row=2, column=3, padx=1, pady=1)
        #Cuarto reglon
        boton_1 = tk.Button(botones_frame, text='1', width=13, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(1)).grid(row=3, column=0, padx=1, pady=1)
        boton_2 = tk.Button(botones_frame, text='2', width=13, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(2)).grid(row=3, column=1, padx=1, pady=1)
        boton_3 = tk.Button(botones_frame, text='3', width=13, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(3)).grid(row=3, column=2, padx=1, pady=1)
        boton_suma = tk.Button(botones_frame, text="+", width=9, height=3, bd=0, bg='#eee', cursor='hand2',
                              command=lambda: self._evento_click('+'))
        boton_suma.grid(row=3, column=3, padx=1, pady=1)

        #Quinto Reglon
        boton_cero = tk.Button(botones_frame, text="0", width=28, height=3, bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_click('0'))
        boton_cero.grid(row=4, column=0, padx=1, pady=1,columnspan=2)
        boton_punto = tk.Button(botones_frame, text=".", width=14, height=3, bd=0, bg='#eee', cursor='hand2',
                               command=lambda: self._evento_click('.'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)
        boton_evaluar = tk.Button(botones_frame, text="=", width=9, height=3, bd=0, bg='#eee', cursor='hand2',
                               command=self._evento_evaluar)
        boton_evaluar.grid(row=4, column=3, padx=1, pady=1)

    def _evento_evaluar(self):
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error',f'Ocurrio un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''


    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)
    def _evento_click(self,elemento):
        #Concatenacion el nuevo elemento a la expresion
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)



if __name__ == '__main__':
    calculadora1 = Calculadora()
    calculadora1.mainloop()