from modelos import Estudiante, Curso, Inscripcion
from datetime import date


# ── CREATE ──────────────────────────────────────────────

def registrar_estudiante(session, ci, nombres, correo):
    nuevo = Estudiante(
        ci=ci,
        nombres=nombres,
        correo=correo,
        fecha_registro=date.today(),
        estado="ACTIVO"
    )
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    print(f"\n✔ Estudiante registrado: {nuevo}")
    return nuevo


def registrar_curso(session, nombre_curso, creditos, id_docente, gestion="2026-I"):
    nuevo = Curso(
        nombre_curso=nombre_curso,
        creditos=creditos,
        id_docente=id_docente,
        gestion=gestion,
        estado="ABIERTO"
    )
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    print(f"\n✔ Curso registrado: {nuevo}")
    return nuevo


def registrar_inscripcion(session, id_estudiante, id_curso):
    # Verificar duplicado
    existe = session.query(Inscripcion).filter_by(
        id_estudiante=id_estudiante,
        id_curso=id_curso
    ).first()

    if existe:
        print(f"\n⚠ El estudiante {id_estudiante} ya está inscrito en el curso {id_curso}.")
        return existe

    nueva = Inscripcion(
        id_estudiante=id_estudiante,
        id_curso=id_curso,
        fecha_inscripcion=date.today(),
        estado="INSCRITO"
    )
    session.add(nueva)
    session.commit()
    session.refresh(nueva)
    print(f"\n✔ Inscripción registrada: {nueva}")
    return nueva


# ── READ ─────────────────────────────────────────────────

def buscar_estudiante_por_id(session, id_estudiante):
    est = session.query(Estudiante).filter_by(
        id_estudiante=id_estudiante
    ).first()

    if est:
        print(f"\n✔ Estudiante encontrado:")
        print(f"   ID     : {est.id_estudiante}")
        print(f"   Nombre : {est.nombres}")
        print(f"   CI     : {est.ci}")
        print(f"   Correo : {est.correo}")
        print(f"   Estado : {est.estado}")
    else:
        print(f"\n✘ No existe estudiante con ID {id_estudiante}")
    return est


def cursos_por_estudiante(session, id_estudiante):
    est = session.query(Estudiante).filter_by(
        id_estudiante=id_estudiante
    ).first()

    if not est:
        print(f"\n✘ Estudiante {id_estudiante} no encontrado.")
        return

    print(f"\n📋 Cursos inscritos de '{est.nombres}':")
    if not est.inscripciones:
        print("   (Sin inscripciones)")
        return

    for insc in est.inscripciones:
        c = insc.curso
        print(f"   • [{c.id_curso}] {c.nombre_curso:<30} "
              f"| {c.creditos} créditos "
              f"| Estado: {insc.estado}")


def listar_estudiantes(session):
    todos = session.query(Estudiante).order_by(Estudiante.id_estudiante).all()
    print(f"\n📋 LISTADO GENERAL DE ESTUDIANTES ({len(todos)} registros):")
    print(f"   {'ID':<5} {'Nombre':<30} {'CI':<12} {'Estado'}")
    print("   " + "-" * 60)
    for e in todos:
        print(f"   {e.id_estudiante:<5} {e.nombres:<30} {e.ci:<12} {e.estado}")
    return todos