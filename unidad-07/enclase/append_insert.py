

# append(valor) -> Agregar un elemento al final de la lista

# insert(indice, valor) -> Agregar un elemento en una posición específica de la lista

energias_renovables = ['solar', 'eólica', 'mareomotriz', 'geotérmica', 'hidroeléctrica']

print("Las energías renovables son: ")
print(energias_renovables)

print("Agregar al final de la lista la energía biogas")
energias_renovables.append("biogas")

print("Las energías renovables son: ")
print(energias_renovables)


print("Agrego algunas al principio de la lista")
energias_renovables.insert(0, 'energía del movimiento')
energias_renovables.insert(0, 'energía de la biomasa')

print("Las energías renovables son: ")
print(energias_renovables)

