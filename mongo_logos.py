from pymongo import MongoClient
from datetime import datetime, timedelta
import random

# ============================================================
# CONEXIÓN A MONGO ATLAS
# Reemplaza la cadena con la tuya copiada de Atlas
# ============================================================
MONGO_URI = "mongodb+srv://wendydarletherrera_db_user:9dLrhFrikqoknCXa@cluster0.lvjxw22.mongodb.net/?retryWrites=true&w=majority"

# conectar al cluster
client  = MongoClient(MONGO_URI)
db      = client["universidad_virtual"]
logs    = db["logs_sistema"]


def insertar_logs():
    """Inserta 100 documentos de eventos del sistema."""

    usuarios = [
        "admin", "docente01", "docente02", "docente03",
        "estudiante001", "estudiante002", "estudiante003",
        "coordinador", "secretaria", "soporte"
    ]

    modulos = [
        "Estudiantes", "Cursos", "Inscripciones",
        "Calificaciones", "Docentes", "Reportes", "Seguridad"
    ]

    acciones = {
        "Estudiantes"   : ["Registro de estudiante",   "Actualización de datos",
                           "Consulta de estudiante",   "Baja de estudiante"],
        "Cursos"        : ["Registro de curso",         "Actualización de curso",
                           "Consulta de cursos",        "Cierre de curso"],
        "Inscripciones" : ["Registro de inscripción",  "Retiro de inscripción",
                           "Consulta de inscripciones"],
        "Calificaciones": ["Registro de nota",         "Actualización de nota",
                           "Consulta de calificaciones"],
        "Docentes"      : ["Registro de docente",      "Actualización de docente",
                           "Consulta de docentes"],
        "Reportes"      : ["Generación de reporte",    "Exportación PDF",
                           "Consulta de estadísticas"],
        "Seguridad"     : ["Inicio de sesión",         "Cierre de sesión",
                           "Cambio de contraseña",     "Intento fallido"],
    }

    ips = [f"192.168.1.{i}" for i in range(1, 21)]

    fecha_base = datetime(2026, 6, 1)
    documentos = []

    for i in range(100):
        modulo  = random.choice(modulos)
        usuario = random.choice(usuarios)
        fecha   = fecha_base + timedelta(
            days=random.randint(0, 15),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )

        doc = {
            "usuario"   : usuario,
            "accion"    : random.choice(acciones[modulo]),
            "modulo"    : modulo,
            "fecha"     : fecha.strftime("%Y-%m-%d"),
            "hora"      : fecha.strftime("%H:%M:%S"),
            "timestamp" : fecha,
            "ip"        : random.choice(ips),
            "nivel"     : random.choice(["INFO", "INFO", "WARN", "ERROR"]),
            "detalle"   : f"Evento #{i+1} ejecutado por {usuario} en módulo {modulo}",
            "session_id": f"sess_{random.randint(10000, 99999)}"
        }
        documentos.append(doc)

    # Limpiar colección antes de insertar
    logs.drop()

    resultado = logs.insert_many(documentos)
    print(f"\n✔ Se insertaron {len(resultado.inserted_ids)} documentos en logs_sistema")
    print(f"  Base de datos : universidad_virtual")
    print(f"  Colección     : logs_sistema")


if __name__ == "__main__":
    print("=" * 55)
    print("  ACTIVIDAD 9 - Inserción de documentos MongoDB")
    print("=" * 55)
    insertar_logs()
    client.close()
    print("\n✔ Conexión cerrada correctamente.")