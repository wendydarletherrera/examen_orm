from conexion import get_session
from crud import (
    registrar_estudiante,
    registrar_curso,
    registrar_inscripcion,
    buscar_estudiante_por_id,
    cursos_por_estudiante,
    listar_estudiantes
)

def main():
    session = get_session()

    print("=" * 60)
    print("  EXAMEN FINAL - PARTE III: SQLAlchemy ORM")
    print("  Universidad Virtual XXI")
    print("=" * 60)

    # 1. Registrar estudiante
    print("\n--- 1. REGISTRAR ESTUDIANTE ---")
    est = registrar_estudiante(
        session,
        ci="CI998877",
        nombres="Carlos ORM Prueba",
        correo="carlos.orm@universidad.edu"
    )

    # 2. Registrar curso
    print("\n--- 2. REGISTRAR CURSO ---")
    curso = registrar_curso(
        session,
        nombre_curso="Curso SQLAlchemy Test",
        creditos=3,
        id_docente=1
    )

    # 3. Registrar inscripción
    print("\n--- 3. REGISTRAR INSCRIPCIÓN ---")
    registrar_inscripcion(session, est.id_estudiante, curso.id_curso)

    # 3b. Intentar inscripción duplicada
    print("\n--- 3b. INSCRIPCIÓN DUPLICADA ---")
    registrar_inscripcion(session, est.id_estudiante, curso.id_curso)

    # 4. Buscar estudiante por ID
    print("\n--- 4. BUSCAR ESTUDIANTE POR ID ---")
    buscar_estudiante_por_id(session, est.id_estudiante)
    buscar_estudiante_por_id(session, 9999)   # inexistente

    # 5. Cursos por estudiante
    print("\n--- 5. CURSOS DEL ESTUDIANTE ---")
    cursos_por_estudiante(session, est.id_estudiante)
    cursos_por_estudiante(session, 1)          # estudiante del SQL base

    # 6. Listado general
    print("\n--- 6. LISTADO GENERAL ---")
    listar_estudiantes(session)

    session.close()
    print("\n✔ Todas las operaciones completadas correctamente.")

if __name__ == "__main__":
    main()