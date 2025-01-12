import matplotlib.pyplot as plt
import math
z = 3  # zona
s = 2  # tipo de suelo
C = 3  # categoría de edificio
r = 8  # Coefi ciente Básico de Reducción R0 (*) __X
r2= 3  # Coefi ciente Básico de Reducción R0 (*) __Y
Ia= 1  # Irregularidad en altura__X
Ip= 1  # Irregularidad en planta__X
Ia2=1  # Irregularidad en altura__Y
Ip2=1  # Irregularidad en planta__Y
Ct= 60 #ct Período Fundamental de Vibración__X
H = 20 #altura de edificacion en metros__Y
Cty= 60 #ct Período Fundamental de Vibración__Y
H2 = 20 #altura de edificacion en metros__Y


# Determinación del valor de la zona
zonas = {1: 0.10, 2: 0.25, 3: 0.35, 4: 0.45}
zona = zonas.get(z, 0)
print("--------------------------------------------------")
print(f"Z= {z} es: {zona} g ")

# Determinación de las características del suelo
caracteristicas_suelo = {
    0: {"vs": ">1500", "n60": "-", "su": "-"},
    1: {"vs": "500 m/s a 1500 m/s", "n60": "> 50", "su": ">100 kPa"},
    2: {"vs": "180 m/s a 500 m/s", "n60": "15 a 50", "su": "50 kPa a 100 kPa"},
    3: {"vs": "< 180 m/s", "n60": "< 15", "su": "25 kPa a 50 kPa"},
    4: {"vs": "Clasificación basada en el EMS", "n60": "Clasificación basada en el EMS", "su": "Clasificación basada en el EMS"},
}
suelo = caracteristicas_suelo.get(s, {"vs": "-", "n60": "-", "su": "-"})
print(f"VS = {suelo['vs']}")
print(f"n60= {suelo['n60']}")
print(f"Su= {suelo['su']}")

# Determinación del Factor de Suelo "S"
factor_suelo = {
    1: [0.80, 1.00, 1.60, 2.00],  # Z1
    2: [0.80, 1.00, 1.20, 1.40],  # Z2
    3: [0.80, 1.00, 1.15, 1.20],  # Z3
    4: [0.80, 1.00, 1.05, 1.10]   # Z4
}

if z in factor_suelo and 0 <= s < len(factor_suelo[z]):
    factor_s = factor_suelo[z][s]
    print(f"Factor de suelo S para Z{z} y S{s} = {factor_s}")
else:
    print("Combinación de zona y tipo de suelo no válida.")

# Determinación de los períodos "TP" y "TL"
periodos_tp_tl = {
    "TP": [0.3, 0.4, 0.6, 1.0],
    "TL": [3.0, 2.5, 2.0, 1.6]
}

tp = periodos_tp_tl["TP"][s] if s < len(periodos_tp_tl["TP"]) else None
tl = periodos_tp_tl["TL"][s] if s < len(periodos_tp_tl["TL"]) else None

if tp is not None and tl is not None:
    print(f"TP (s) para S{s} = {tp}")
    print(f"TL (s) para S{s} = {tl}")
else:
    print("Tipo de suelo no válido para determinar TP y TL.")

# Determinación del factor U
factores_u = {0: 1.7, 1: 1.5, 2: 1.3, 3: 1.0}
U = factores_u.get(C, 0)
print(f"Factor U = {U}")

print("--------------------------------------------------")
# SISTEMA ESTRUCTURAL
sistema_estructural = {
    0: {4: "A0", 3: "A0", 2: "A1", 1: "A1"},
    1: {4: "A2", 3: "A2", 2: "A2", 1: "A4"},
    2: {4: "A5", 3: "A5", 2: "A5", 1: "A4"},
    3: {4: "A4", 3: "A4", 2: "A4", 1: "A4"},
}

sistemas = {
    "A0":"""Aislamiento Sísmico con cualquier sistema
estructural.""",
    "A1": """Estructuras de acero tipo SCBF, OCBF y EBF.
Estructuras de concreto: Sistema Dual,
Muros de Concreto Armado. Albañilería Armada o Confiada.""",
    "A2": """Estructuras de acero tipo SCBF, OCBF y EBF.
Estructuras de concreto: Sistema Dual,
Muros de Concreto Armado. Albañilería Armada o Confiada.""",
    "A3": """Estructuras de acero tipo SCBF, OCBF y EBF.
Estructuras de concreto: Sistema Dual,
Muros de Concreto Armado. Albañilería Armada o Confiada.""",
    "A4": "Cualquier sistema.",
    "A5": """Estructuras de acero tipo SMF, IMF, SCBF, OCBF y EBF.
Estructuras de concreto: Pórticos, Sistema Dual,
Muros de Concreto Armado. Albañilería Armada o Confiada.
Estructuras de madera.""",
    "Aislamiento Sísmico con cualquier sistema estructural": """Aislamiento Sísmico con cualquier sistema estructural."""
}

# Lógica para determinar el sistema estructural
sistema = sistema_estructural.get(C, {}).get(z, "Sistema no definido")
print("Sistema estructural:")
print(sistemas.get(sistema, "Información del sistema no disponible."))

print("--------------------------------------------------")
# CATEGORÍA Y REGULARIDAD DE LAS EDIFICACIONES

regularidad= {
    0: {4: "B0", 3: "B0", 2: "B0", 1: "B1"},
    1: {4: "B0", 3: "B0", 2: "B0", 1: "B1"},
    2: {4: "B1", 3: "B1", 2: "B1", 1: "B2"},
    3: {4: "B1", 3: "B1", 2: "B3", 1: "B2"},
}

sistemas = {
    "B0":"""No se permiten irregularidades""",
    "B1": """No se permiten irregularidades extremas""",
    "B2": """ Sin restricciones""",
    "B3": """No se permiten irregularidades extremas
excepto en edifi cios de hasta 2 pisos u 8 m
de altura total""",
   
}

# Determinación de la categoría y regularidad
regularidad_categoria = regularidad.get(C, {}).get(z, "Categoría no definida")
print("Regularidad de la edificación:")
print(sistemas.get(regularidad_categoria, "Información de regularidad no disponible."))
print("--------------------------------------------------")


#Coeficiente de Reducción de las Fuerzas Sísmicas, R
print("Coeficiente de Reducción de las Fuerzas Sísmicas, R")
R1= r * Ia * Ip  # x
R2= r2 * Ia2 * Ip2  # Y
print(f'RX = {R1}')
print(f'RY = {R2}')
print("--------------------------------------------------")

#Período Fundamental de Vibración
print("Período Fundamental de Vibración:")
TX=H/Ct
TY=H2/Cty
print(f'Tx = {TX}')
print(f'Ty = {TY}')

# Exponente k
print("--------------------------------------------------")
print("KX Y KY GENERACION DE PATRONES DE CARGA X E Y SAP O ETABS")
print("--------------------------------------------------")
print("exponente k X")
k1 = 0
if TX < 0.5:
    k1 = 1.0
elif TX > 0.5:
    k1 = 0.75 + 0.5 * TX
    if k1 > 2.0:  # Limitar k1 a 2 si es mayor
        k1 = 2.0
    print(f'kx = {k1} <= 2.0')
print(f'Kx = {k1}')

print("exponente k Y")
k2 = 0
if TY < 0.5:
    k2 = 1.0
elif TY > 0.5:
    k2 = 0.75 + 0.5 * TY
    if k2 > 2.0:  # Limitar k2 a 2 si es mayor
        k2 = 2.0
    print(f'ky = {k2} < 2.0')
print(f'Ky = {k2}')
print("--------------------------------------------------")
#FACTOR DE AMPLIFICACION
print("FACTOR DE AMPLIFICACION")
CX=0
if TX < tp:
    CX=2.5
elif tp < TX < tl:
    CX=2.5*(tp/TX)
elif TX > tl:
    CX=2.5*((tp*tl)/(TX**2))
print(f'CX = {CX}')
# Cálculo de CY
CY=0
if TY < tp:
    CY=2.5
elif tp < TY < tl:
    CY=2.5*(tp/TY)
elif TY > tl:
    CY=2.5*((tp*tl)/(TY**2))
print(f'CY = {CY}')
print("--------------------------------------------------")
print("EL VALOR DE  C/R NO DEBERA CONSIDERARSE MENOR QUE 0.11")
v1 = 0  
if CX / r >= 0.11:  
    v1 = CX / r
else:  
    v1 = 0.11
print(f'CX / RX = {v1}')

v2 = 0  
if CY / r2 >= 0.11:  
    v2 = CY / r2
else:  
    v2 = 0.11
print(f'CX / RX = {v2}')

#coeficiente de la cortante basal
print("--------------------------------------------------")
print("insertar en sap 2000 o etabs")
print("DIRECCION X-X")
Z=zona
S=factor_s

CB=(Z*k1*v1*S)
# Asume que las variables están definidas previamente en el código

print(f"Z: {Z}")
print(f"U: {k1}")
print(f"C: {v1}")
print(f"S: {S}")
print(f"RX: {R1}")
print(f'coeficiente CB/RX = {CB} ')
print("--------------------------------------------------")
print("DIRECCION Y - Y")
CB2=(Z*k2*v2*S)
# Asume que las variables están definidas previamente en el código

print(f"Z: {Z}")
print(f"U: {k2}")
print(f"C: {v2}")
print(f"S: {S}")
print(f"RX: {R2}")
print(f'coeficiente CB/RX = {CB2} ')

# Asumiendo que las variables tp, tl, Z, S, r, k1, k2 ya están definidas

# Generar lista de valores para TX1 y TX2
TX1_list = [round(x, 2) for x in [i * 0.01 for i in range(1, 1001)]]
TX2_list = TX1_list[:]

# Calcular CX1 y CX2
def calcular_cx(TX, tp, tl):
    if TX < tp:
        return 2.5
    elif tp <= TX <= tl:
        return 2.5 * (tp / TX)
    else:
        return 2.5 * ((tp * tl) / (TX ** 2))

CX1_list = [calcular_cx(TX1, tp, tl) for TX1 in TX1_list]
CX2_list = [calcular_cx(TX2, tp, tl) for TX2 in TX2_list]

# Calcular SA, SV y SD para TX1 y TX2
SA_list = [(Z * k1 * CX1 * S / r) * 9.81 for CX1 in CX1_list]
SA2_list = [(Z * k2 * CX2 * S / r) * 9.81 for CX2 in CX2_list]

SV_list = [(TX1 / (2 * math.pi)) * SA for TX1, SA in zip(TX1_list, SA_list)]
SV2_list = [(TX2 / (2 * math.pi)) * SA2 for TX2, SA2 in zip(TX2_list, SA2_list)]

SD_list = [((TX1 / (2 * math.pi)) ** 2) * SA for TX1, SA in zip(TX1_list, SA_list)]
SD2_list = [((TX2 / (2 * math.pi)) ** 2) * SA2 for TX2, SA2 in zip(TX2_list, SA2_list)]

# Imprimir listas de TX1 y TX2 con sus valores calculados
print("Lista de TX1, CX1, SA, SV y SD en formato vertical:")
print("TX1 (s)    CX1        SA (m/s²)    SV (m/s)    SD (m)")
for TX1, CX1, SA, SV, SD in zip(TX1_list, CX1_list, SA_list, SV_list, SD_list):
    print(f"{TX1:7.2f}    {CX1:7.4f}    {SA:7.4f}    {SV:7.4f}    {SD:7.4f}")

print("--------------------------------------------------------------------------")
print("Lista de TX2, CX2, SA2, SV2 y SD2 en formato vertical:")
print("TX2 (s)    CX2        SA2 (m/s²)    SV2 (m/s)    SD2 (m)")
for TX2, CX2, SA2, SV2, SD2 in zip(TX2_list, CX2_list, SA2_list, SV2_list, SD2_list):
    print(f"{TX2:7.2f}    {CX2:7.4f}    {SA2:7.4f}    {SV2:7.4f}    {SD2:7.4f}")

# Generar gráficos organizados en dos columnas
fig, axs = plt.subplots(3, 2, figsize=(14, 12))

# Gráfico de SA vs TX1 (Izquierda)
axs[0, 0].plot(TX1_list, SA_list, label='SA vs TX1', color='blue', linewidth=2)
axs[0, 0].axvline(tp, color='green', linestyle='--', label=f'tp = {tp} s')
axs[0, 0].axvline(tl, color='red', linestyle='--', label=f'tl = {tl} s')
axs[0, 0].set_title('Relación entre SA y TX1', fontsize=14)
axs[0, 0].set_xlabel('TX1 (s)', fontsize=12)
axs[0, 0].set_ylabel('SA (m/s²)', fontsize=12)
axs[0, 0].grid(visible=True, which='both', linestyle='--', linewidth=0.5)
axs[0, 0].legend(fontsize=10)

# Gráfico de SV vs TX1 (Izquierda)
axs[1, 0].plot(TX1_list, SV_list, label='SV vs TX1', color='orange', linewidth=2)
axs[1, 0].axvline(tp, color='green', linestyle='--', label=f'tp = {tp} s')
axs[1, 0].axvline(tl, color='red', linestyle='--', label=f'tl = {tl} s')
axs[1, 0].set_title('Relación entre SV y TX1', fontsize=14)
axs[1, 0].set_xlabel('TX1 (s)', fontsize=12)
axs[1, 0].set_ylabel('SV (m/s)', fontsize=12)
axs[1, 0].grid(visible=True, which='both', linestyle='--', linewidth=0.5)
axs[1, 0].legend(fontsize=10)

# Gráfico de SD vs TX1 (Izquierda)
axs[2, 0].plot(TX1_list, SD_list, label='SD vs TX1', color='green', linewidth=2)
axs[2, 0].axvline(tp, color='green', linestyle='--', label=f'tp = {tp} s')
axs[2, 0].axvline(tl, color='red', linestyle='--', label=f'tl = {tl} s')
axs[2, 0].set_title('Relación entre SD y TX1', fontsize=14)
axs[2, 0].set_xlabel('TX1 (s)', fontsize=12)
axs[2, 0].set_ylabel('SD (m)', fontsize=12)
axs[2, 0].grid(visible=True, which='both', linestyle='--', linewidth=0.5)
axs[2, 0].legend(fontsize=10)

# Gráfico de SA2 vs TX2 (Derecha)
axs[0, 1].plot(TX2_list, SA2_list, label='SA2 vs TX2', color='blue', linewidth=2)
axs[0, 1].axvline(tp, color='green', linestyle='--', label=f'tp = {tp} s')
axs[0, 1].axvline(tl, color='red', linestyle='--', label=f'tl = {tl} s')
axs[0, 1].set_title('Relación entre SA2 y TX2', fontsize=14)
axs[0, 1].set_xlabel('TX2 (s)', fontsize=12)
axs[0, 1].set_ylabel('SA2 (m/s²)', fontsize=12)
axs[0, 1].grid(visible=True, which='both', linestyle='--', linewidth=0.5)
axs[0, 1].legend(fontsize=10)

# Gráfico de SV2 vs TX2 (Derecha)
axs[1, 1].plot(TX2_list, SV2_list, label='SV2 vs TX2', color='orange', linewidth=2)
axs[1, 1].axvline(tp, color='green', linestyle='--', label=f'tp = {tp} s')
axs[1, 1].axvline(tl, color='red', linestyle='--', label=f'tl = {tl} s')
axs[1, 1].set_title('Relación entre SV2 y TX2', fontsize=14)
axs[1, 1].set_xlabel('TX2 (s)', fontsize=12)
axs[1, 1].set_ylabel('SV2 (m/s)', fontsize=12)
axs[1, 1].grid(visible=True, which='both', linestyle='--', linewidth=0.5)
axs[1, 1].legend(fontsize=10)

# Gráfico de SD2 vs TX2 (Derecha)
axs[2, 1].plot(TX2_list, SD2_list, label='SD2 vs TX2', color='green', linewidth=2)
axs[2, 1].axvline(tp, color='green', linestyle='--', label=f'tp = {tp} s')
axs[2, 1].axvline(tl, color='red', linestyle='--', label=f'tl = {tl} s')
axs[2, 1].set_title('Relación entre SD2 y TX2', fontsize=14)
axs[2, 1].set_xlabel('TX2 (s)', fontsize=12)
axs[2, 1].set_ylabel('SD2 (m)', fontsize=12)
axs[2, 1].grid(visible=True, which='both', linestyle='--', linewidth=0.5)
axs[2, 1].legend(fontsize=10)

# Ajustar el espaciado entre gráficos
plt.tight_layout()
plt.show()
