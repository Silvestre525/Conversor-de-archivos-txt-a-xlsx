import pandas as pd


file_name = input("Por favor, ingresa el nombre del archivo de texto (incluyendo la extensión .txt): ")

with open(file_name, 'r') as file:
    lines = file.readlines()

data = [line.strip().split(',') for line in lines]


df = pd.DataFrame(data[1:], columns=data[0])

excel_file_name = file_name.replace('.txt', '.xlsx')
df.to_excel(excel_file_name, index=False)

print("Archivo Excel generado exitosamente.")
