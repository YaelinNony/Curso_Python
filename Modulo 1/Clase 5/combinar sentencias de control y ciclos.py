#combinar sentencias if con bucles for
mediciones_ph = [7.1, 7.3, 6.4, 7.0, 7.6, 7.2, 5.9]
conteo_anomalias = 0
anomalias_detectadas = []
print(f"{mediciones_ph}")
print("\nIniciando monitor de calidad de pH...")
for ph in mediciones_ph:
    # Este 'if' se ejecuta en CADA iteración
    if ph < 6.5 or ph > 7.5:
        print(f"  ALERTA: Se detectó valor anómalo: {ph}")
        conteo_anomalias = conteo_anomalias + 1
        anomalias_detectadas.append(ph)

print("--- Análisis de Calidad Completado ---")
print(f"Total de mediciones: {len(mediciones_ph)}")
print(f"Total de anomalías: {conteo_anomalias}")
print(f"Valores anómalos registrados: {anomalias_detectadas}")