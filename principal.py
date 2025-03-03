import streamlit as st
import pandas as pd
import clsEmpleado as empleado 


st.title("BUSINESS CORPORATION - Área de Recursos Humanos")
st.header("Historia de usuario")
st.write("Lista de empleados y su información")


# Crear el gerente
gerente = empleado.Gerente("Carlos López Sarmiento")

# Crear los jefes de área
jefes = [
    empleado.JefeDeArea("Ana Pérez Gonzales", "Marketing", gerente,),
    empleado.JefeDeArea("Juan Elver Gómez Chura", "Sistemas", gerente),
    empleado.JefeDeArea("Luis Méndez Castro", "Producción", gerente),
    empleado.JefeDeArea("Marta María Rojas Paredes", "Logística", gerente),
    empleado.JefeDeArea("Pedro Diego Ramírez Vizcarra", "Finanzas", gerente)
]

# Crear asistentes (máximo 2 por área)
asistentes = [
    empleado.Asistente("María Josefina Torres Mamani", jefes[0]),
    empleado.Asistente("Javier Pedro Vargas Mustinso", jefes[0], "R(Renuncia)"),
    empleado.Asistente("Luis Ramírez Cueva", jefes[1]),
    empleado.Asistente("Andrea Soto Aguilar", jefes[2]),
    empleado.Asistente("Elena Ortiz Rivera", jefes[3]),
    empleado.Asistente("Pedro Quiñones Bautizan", jefes[1], "TC (Término de Contrato)"),
    empleado.Asistente("Ronaldo Sergio Lopez Rivera", jefes[4])
]

# Crear técnicos (mínimo 3, máximo 5 por área)
tecnicos = [
    empleado.Tecnico("Pedro Castillo Segarra", jefes[0], 3),
    empleado.Tecnico("Javier Díaz Paredes", jefes[0], 5),
    empleado.Tecnico("Fernando Sánchez Sánchez", jefes[1], 2),
    empleado.Tecnico("Edson Flores Sanchez", jefes[4], 2),
    empleado.Tecnico("Hugo Paredes Crisanto", jefes[1], 4),
    empleado.Tecnico("Erick Pérez Domingo", jefes[1], 1),
    empleado.Tecnico("Rosa Medina Huallpa", jefes[2], 3),
    empleado.Tecnico("Daniel Suárez Ortiz", jefes[3], 5),
    empleado.Tecnico("Gabriel Fuentes Cavero", jefes[4], 2),
    empleado.Tecnico("Soledad Aquitania Polo", jefes[0], 2),
    empleado.Tecnico("Regina Lopez Albujar", jefes[2], 3),
    empleado.Tecnico("Rigoberto Bustinsa Selva", jefes[3], 5),
    empleado.Tecnico("Hernan Robles Crisanto", jefes[3], 4),
    empleado.Tecnico("Ericka Apaza Domingo", jefes[2], 1),
    empleado.Tecnico("Cristina Vargas Sipan", jefes[4], 4)
]

# Unir todos los empleados en una lista
empleados = [gerente] + jefes + asistentes + tecnicos

# Crear DataFrame para mostrar en Streamlit
data = {
    "Nombre": [e.nombre for e in empleados],
    "Resumen": [e.get_resumen() for e in empleados],
    "Jefe Inmediato": [e.get_jefe_inmediato() for e in empleados],
    "Estado": [e.get_estado() for e in empleados],
}

df = pd.DataFrame(data)
# Mostrar DataFrame en Streamlit
st.dataframe(df)