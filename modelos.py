from sqlalchemy import (
    Column, Integer, String, Date,
    Numeric, ForeignKey, UniqueConstraint, CheckConstraint
)
from sqlalchemy.orm import relationship
from conexion import Base
from datetime import date


class Estudiante(Base):
    __tablename__ = "estudiantes"
    __table_args__ = (
        UniqueConstraint("ci",     name="uq_estudiante_ci"),
        UniqueConstraint("correo", name="uq_estudiante_correo"),
        CheckConstraint(
            "estado IN ('ACTIVO','INACTIVO','SUSPENDIDO')",
            name="chk_estado_estudiante"
        ),
        {"schema": "examen_bd2"},
    )

    id_estudiante  = Column(Integer, primary_key=True, autoincrement=True)
    ci             = Column(String(20),  nullable=False)
    nombres        = Column(String(120), nullable=False)
    correo         = Column(String(120), nullable=False)
    fecha_registro = Column(Date, nullable=False, default=date.today)
    estado         = Column(String(20),  nullable=False, default="ACTIVO")

    inscripciones  = relationship("Inscripcion", back_populates="estudiante")

    def __repr__(self):
        return f"<Estudiante [{self.id_estudiante}] {self.nombres}>"


class Docente(Base):
    __tablename__ = "docentes"
    __table_args__ = (
        {"schema": "examen_bd2"},
    )

    id_docente   = Column(Integer, primary_key=True, autoincrement=True)
    nombres      = Column(String(120), nullable=False)
    especialidad = Column(String(100), nullable=False)
    correo       = Column(String(120), nullable=False)
    estado       = Column(String(20),  nullable=False, default="ACTIVO")

    cursos = relationship("Curso", back_populates="docente")

    def __repr__(self):
        return f"<Docente [{self.id_docente}] {self.nombres}>"


class Curso(Base):
    __tablename__ = "cursos"
    __table_args__ = (
        UniqueConstraint("nombre_curso", name="uq_curso_nombre"),
        CheckConstraint("creditos BETWEEN 1 AND 6", name="chk_creditos"),
        {"schema": "examen_bd2"},
    )

    id_curso     = Column(Integer, primary_key=True, autoincrement=True)
    nombre_curso = Column(String(120), nullable=False)
    creditos     = Column(Integer,     nullable=False)
    id_docente   = Column(Integer, ForeignKey("examen_bd2.docentes.id_docente"),
                          nullable=False)
    gestion      = Column(String(20),  nullable=False)
    estado       = Column(String(20),  nullable=False, default="ABIERTO")

    docente       = relationship("Docente",     back_populates="cursos")
    inscripciones = relationship("Inscripcion", back_populates="curso")

    def __repr__(self):
        return f"<Curso [{self.id_curso}] {self.nombre_curso}>"


class Inscripcion(Base):
    __tablename__ = "inscripciones"
    __table_args__ = (
        UniqueConstraint("id_estudiante", "id_curso", name="uq_estudiante_curso"),
        CheckConstraint(
            "estado IN ('INSCRITO','RETIRADO','APROBADO','REPROBADO')",
            name="chk_estado_inscripcion"
        ),
        {"schema": "examen_bd2"},
    )

    id_inscripcion    = Column(Integer, primary_key=True, autoincrement=True)
    id_estudiante     = Column(Integer,
                               ForeignKey("examen_bd2.estudiantes.id_estudiante"),
                               nullable=False)
    id_curso          = Column(Integer,
                               ForeignKey("examen_bd2.cursos.id_curso"),
                               nullable=False)
    fecha_inscripcion = Column(Date, nullable=False, default=date.today)
    estado            = Column(String(20), nullable=False, default="INSCRITO")

    estudiante = relationship("Estudiante", back_populates="inscripciones")
    curso      = relationship("Curso",      back_populates="inscripciones")

    def __repr__(self):
        return f"<Inscripcion [{self.id_inscripcion}] Est:{self.id_estudiante} Curso:{self.id_curso}>"