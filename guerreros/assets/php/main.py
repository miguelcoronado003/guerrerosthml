# Definir las razas
razas = {
    "Humano": {"Salud": 10, "Ataque": 5, "Defensa": 3},
    "Elfo": {"Salud": 8, "Ataque": 7, "Defensa": 4},
    "Orco": {"Salud": 12, "Ataque": 6, "Defensa": 5},
}

# Definir los tipos de guerreros
tipos = {
    "Guerrero": {"Salud": 5, "Ataque": 4, "Defensa": 2},
    "Arquero": {"Salud": 3, "Ataque": 6, "Defensa": 3},
    "Mago": {"Salud": 2, "Ataque": 8, "Defensa": 1},
}

# Definir los poderes
poderes = [
    {"Nombre": "Fuego", "Daño": 10, "Descripción": "Ataque de fuego que quema al enemigo."},
    {"Nombre": "Hielo", "Daño": 8, "Descripción": "Congela al enemigo reduciendo su velocidad."},
    {"Nombre": "Rayo", "Daño": 12, "Descripción": "Electrocuta al enemigo causando daño adicional."},
]

# Generar datos aleatorios para los guerreros
nombres_guerreros = ["Thor", "Artemis", "Merlin", "Ares", "Loki"]
guerreros = []

for _ in range(5):
    nombre = random.choice(nombres_guerreros)
    nombres_guerreros.remove(nombre)
    raza = random.choice(list(razas.keys()))
    tipo = random.choice(list(tipos.keys()))

    salud = random.randint(50, 100) + razas[raza]["Salud"] + tipos[tipo]["Salud"]
    ataque = random.randint(10, 20) + razas[raza]["Ataque"] + tipos[tipo]["Ataque"]
    defensa = random.randint(5, 15) + razas[raza]["Defensa"] + tipos[tipo]["Defensa"]

    poderes_seleccionados = random.sample(poderes, 3)

    guerrero = {
        "Nombre": nombre,
        "Raza": raza,
        "Tipo": tipo,
        "Salud": salud,
        "Ataque": ataque,
        "Defensa": defensa,
        "Poderes": poderes_seleccionados,
        "Bonificadores Raza": razas[raza],
        "Bonificadores Tipo": tipos[tipo],
    }

    guerreros.append(guerrero)

# Mostrar los datos
for guerrero in guerreros:
    print(f"Guerrero: {guerrero['Nombre']}")
    print(f"  Raza: {guerrero['Raza']}")
    print(f"  Tipo: {guerrero['Tipo']}")
    print(f"  Salud: {guerrero['Salud']}")
    print(f"  Ataque: {guerrero['Ataque']}")
    print(f"  Defensa: {guerrero['Defensa']}")
    print("  Poderes:")
    for poder in guerrero["Poderes"]:
        print(f"    - {poder['Nombre']}: {poder['Daño']} daño, {poder['Descripción']}")
    print("  Bonificadores Raza:")
    for k, v in guerrero["Bonificadores Raza"].items():
        print(f"    {k}: {v}")
    print("  Bonificadores Tipo:")
    for k, v in guerrero["Bonificadores Tipo"].items():
        print(f"    {k}: {v}")
    print()