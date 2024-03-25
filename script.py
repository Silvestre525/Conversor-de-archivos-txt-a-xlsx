import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd


def generate_excel():
    file_path = filedialog.askopenfilename(title="Selecciona un archivo de texto", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        data = [line.strip().split(',') for line in lines]

        df = pd.DataFrame(data[1:], columns=data[0])

        excel_file_name = file_path.replace('.txt', '.xlsx')
        df.to_excel(excel_file_name, index=False)

        messagebox.showinfo("Éxito", "El archivo Excel se generó exitosamente.")


root = tk.Tk()
root.config(bg="black")
root.title("Convertir archivo de texto a Excel")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

button = tk.Button(frame, text="Seleccionar archivo", command=generate_excel,bg="green",fg="black")
button.pack()

root.mainloop()
