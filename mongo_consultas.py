from pymongo import MongoClient

MONGO_URI = "mongodb+srv://wendydarletherrera_db_user:9dLrhFrikqoknCXa@cluster0.lvjxw22.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db     = client["universidad_virtual"]
logs   = db["logs_sistema"]


# ── CONSULTA 1 ───────────────────────────────────────────────
def consulta_todos():
    """Muestra todos los documentos almacenados."""
    print("\n" + "=" * 55)
    print("  CONSULTA 1 - Todos los documentos")
    print("=" * 55)

    total = logs.count_documents({})
    print(f"  Total de documentos: {total}\n")

    for doc in logs.find({}, {"_id": 0}).sort("timestamp", 1):
        print(f"  [{doc['fecha']} {doc['hora']}] "
              f"Usuario: {doc['usuario']:<15} "
              f"Módulo: {doc['modulo']:<15} "
              f"Acción: {doc['accion']}")


# ── CONSULTA 2 ───────────────────────────────────────────────
def consulta_modulo_cursos():
    """Muestra solo los eventos del módulo Cursos."""
    print("\n" + "=" * 55)
    print("  CONSULTA 2 - Eventos del módulo 'Cursos'")
    print("=" * 55)

    filtro     = {"modulo": "Cursos"}
    proyeccion = {"_id": 0, "fecha": 1, "hora": 1,
                  "usuario": 1, "accion": 1, "ip": 1}

    resultados = list(logs.find(filtro, proyeccion).sort("timestamp", 1))
    print(f"  Total encontrados: {len(resultados)}\n")

    for doc in resultados:
        print(f"  [{doc['fecha']} {doc['hora']}] "
              f"Usuario: {doc['usuario']:<15} "
              f"Acción: {doc['accion']:<30} "
              f"IP: {doc['ip']}")


# ── CONSULTA 3 ───────────────────────────────────────────────
def consulta_por_usuario(usuario: str):
    """Muestra todos los eventos de un usuario específico."""
    print("\n" + "=" * 55)
    print(f"  CONSULTA 3 - Eventos del usuario: '{usuario}'")
    print("=" * 55)

    filtro     = {"usuario": usuario}
    proyeccion = {"_id": 0, "fecha": 1, "hora": 1,
                  "modulo": 1, "accion": 1, "nivel": 1}

    resultados = list(logs.find(filtro, proyeccion).sort("timestamp", 1))
    print(f"  Total encontrados: {len(resultados)}\n")

    for doc in resultados:
        print(f"  [{doc['fecha']} {doc['hora']}] "
              f"Módulo: {doc['modulo']:<15} "
              f"Acción: {doc['accion']:<35} "
              f"Nivel: {doc['nivel']}")


# ── EJECUCIÓN ────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  ACTIVIDAD 10 - Consultas MongoDB")
    print("  Universidad Virtual XXI - logs_sistema")
    print("=" * 55)

    consulta_todos()
    consulta_modulo_cursos()
    consulta_por_usuario("admin")
    consulta_por_usuario("docente01")

    client.close()
    print("\n✔ Consultas finalizadas correctamente.")