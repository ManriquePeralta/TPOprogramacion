"""
Módulo para mostrar estadísticas sobre los paquetes turísticos.
Incluye funciones para calcular totales, promedios, máximos, mínimos, conteos y porcentajes por tipo de paquete.
"""
from Paquetes_Pack.lista_paquetes import paquetes

# Función para calcular el total de paquetes
def total_paquetes():
	"""Calcula el total de paquetes registrados"""
	return len(paquetes)

# Función para calcular el promedio de precio de los paquetes
def promedio_precio():
	"""Calcula el precio promedio de los paquetes"""
	if not paquetes:
		return 0
	return sum(p["precio"] for p in paquetes) / total_paquetes()

# Función para encontrar el máximo precio de paquete
def max_precio():
	"""Devuelve el precio máximo entre los paquetes"""
	if not paquetes:
		return 0
	return max(p["precio"] for p in paquetes)

# Función para encontrar el mínimo precio de paquete
def min_precio():
	"""Devuelve el precio mínimo entre los paquetes"""
	if not paquetes:
		return 0
	return min(p["precio"] for p in paquetes)

# Función para calcular el conteo por tipo de paquete
def conteo_por_tipo():
	"""Devuelve un diccionario con el conteo de paquetes por tipo"""
	conteo = {}
	for p in paquetes:
		if p["tipo"] in conteo:
			conteo[p["tipo"]] += 1
		else:
			conteo[p["tipo"]] = 1
	return conteo

# Función para calcular los porcentajes por tipo de paquete
def porcentajes_por_tipo():
	"""Devuelve un diccionario con el porcentaje de paquetes por tipo"""
	conteo = conteo_por_tipo()
	total = total_paquetes()
	return {tipo: (cant / total) * 100 for tipo, cant in conteo.items()}

# Función principal para mostrar las estadísticas de paquetes
def estadisticas_paquetes():
	"""Muestra por consola todas las estadísticas calculadas sobre los paquetes"""
	if not paquetes:
		print("\nNo hay paquetes registrados para calcular estadísticas.\n")
		return

	print("\n\n=== ESTADÍSTICAS DE PAQUETES ===")
	print(f"Total de paquetes: {total_paquetes()}")
	print(f"Promedio de precio: ${promedio_precio():.2f}")
	print(f"Precio máximo: ${max_precio()}")
	print(f"Precio mínimo: ${min_precio()}")

	print("\nConteo por tipo:")
	for tipo, cant in conteo_por_tipo().items():
		print(f"  {tipo}: {cant} paquetes")

	print("\nPorcentajes por tipo:")
	for tipo, porcentaje in porcentajes_por_tipo().items():
		print(f"  {tipo}: {porcentaje:.2f}%")

	print()
