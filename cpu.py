import platform
import psutil

system_info= platform.uname()
print("Informacion del sistema:")
print(f"Sistema operativo: {system_info.system}")
print(f"Nombre del Equipo: {system_info.node}")
print(f"Version: {system_info.release}")
print(f"Version detallada: {system_info.version}")
print(f"Procesador: {system_info.processor}")

print("\nEstadisticas avanzadas: ")

cpu_percent= psutil.cpu_percent(interval=1)
print(f"Porcentaje de uso de la CPU: , {cpu_percent}%")

memory_info= psutil.virtual_memory()
print(f"Memoria total: {round(memory_info.total/1024**3, 2)} GB")
print(f"Memoria disponible: {round(memory_info.available/1024**3, 2)} GB")
print(f"Memoria usada: {round(memory_info.used/1024**3, 2)} GB")


