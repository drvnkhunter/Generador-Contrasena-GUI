import tkinter as tk
from tkinter import messagebox
import random
import string

# Función para generar la contraseña
def generar_contrasena_gui():
    try:
        longitud_str = entrada_longitud.get()
        longitud = int(longitud_str)

        if longitud <= 0:
            messagebox.showerror("Error de entrada", "Por favor, ingrese un número positivo.")
            # Borra cualquier contraseña previa si la entrada es inválida
            resultado_contrasena.config(text="Tu contraseña segura aparecerá aquí.") 
            boton_copiar.config(state=tk.DISABLED) # Deshabilita el botón de copiar
            return
        
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena_generada = "".join(random.choice(caracteres) for _ in range(longitud))
        
        # Actualiza la etiqueta con la nueva contraseña
        resultado_contrasena.config(text="Tu contraseña segura es: " + contrasena_generada)
        
        # Habilita el botón de copiar una vez que se genera una contraseña válida
        boton_copiar.config(state=tk.NORMAL)
        
    except ValueError:
        messagebox.showerror("Error de entrada", "Entrada inválida. Por favor, ingrese un número entero usando dígitos (ej. 5, 10).")
        # Borra cualquier contraseña previa y deshabilita el botón de copiar
        resultado_contrasena.config(text="Tu contraseña segura aparecerá aquí.")
        boton_copiar.config(state=tk.DISABLED)

# Función para copiar la contraseña al portapapeles
def copiar_contrasena():
    # Obtiene solo la parte de la contraseña de la etiqueta de resultado
    # Esto asume que el texto siempre comenzará con "Tu contraseña segura es: "
    texto_completo = resultado_contrasena.cget("text")
    prefijo = "Tu contraseña segura es: "
    if texto_completo.startswith(prefijo):
        contrasena_a_copiar = texto_completo[len(prefijo):]
        ventana.clipboard_clear()  # Limpia el portapapeles actual
        ventana.clipboard_append(contrasena_a_copiar) # Añade la contraseña al portapapeles
        ventana.update() # Actualiza el portapapeles (necesario para algunos sistemas)
        messagebox.showinfo("Copiado", "¡Contraseña copiada al portapapeles!")
    else:
        messagebox.showwarning("Advertencia", "No hay una contraseña válida para copiar.")


# Ventana principal de la GUI
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("400x250") # Aumentamos un poco la altura para el nuevo botón
ventana.resizable(False, False)

# Widgets de la GUI

# Etiqueta y Campo de entrada para la longitud
etiqueta_longitud = tk.Label(ventana, text="Ingrese el tamaño de caracteres de tu contraseña:")
etiqueta_longitud.pack(pady=10)

entrada_longitud = tk.Entry(ventana, width=30)
entrada_longitud.pack(pady=5)

# Botón para generar la contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contrasena_gui)
boton_generar.pack(pady=10)

# Etiqueta para mostrar la contraseña generada
resultado_contrasena = tk.Label(ventana, text="Tu contraseña segura aparecerá aquí.")
resultado_contrasena.pack(pady=10)

# Botón para copiar la contraseña 
boton_copiar = tk.Button(ventana, text="Copiar Contraseña", command=copiar_contrasena, state=tk.DISABLED)
boton_copiar.pack(pady=5)

ventana.mainloop()