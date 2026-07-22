# Listas: Son similares a las variables. Son como una caja donde podemos meter cosas y el .append nos permite abrir esa caja para echar algo más en la lista.
# Fórmula: mylist = []
peces = ["coral", "pez angel"]
# Queremos añadir otro, utilizamos el .append:
peces.append("pez loro")
# Ahora inprimimos la lista:
print(peces)
for pez in peces:
    print(f"Se detectó precencia de {pez}")

# Ahora lo hacemos con laa caja inicial vacía:
bases_nitrogenadas = []
bases_nitrogenadas.append("guanina")
bases_nitrogenadas.append("adenina")
bases_nitrogenadas.append("citocina")
bases_nitrogenadas.append("timina")
print(f"Bases precentadas: {bases_nitrogenadas}")
# La f antes de las comillas es para decir que lo que viene a continuación tiene algo especial y que solo debe imprimir el contenido de las llaves y no a ellas.
for bases in bases_nitrogenadas:
    print(f"Se detectó {bases}")