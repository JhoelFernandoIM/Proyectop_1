import streamlit as st
import pandas as pd
import clsEmpleado as empleado 


st.title("BUSINESS CORPORATION - Área de Recursos Humanos")
st.header("Historia de usuario")
st.write("Lista de empleados y su información")


# Crear el gerente
gerente = empleado.Gerente("Carlos López")

# Crear los jefes de área
jefes = [
    empleado.JefeDeArea("Ana Pérez", "Marketing", gerente),
    empleado.JefeDeArea("Juan Gómez", "Sistemas", gerente),
    empleado.JefeDeArea("Luis Méndez", "Producción", gerente),
    empleado.JefeDeArea("Marta Rojas", "Logística", gerente),
    empleado.JefeDeArea("Pedro Ramírez", "Finanzas", gerente)
]

# Crear asistentes (máximo 2 por área)
asistentes = [
    empleado.Asistente("María Torres", jefes[0]),
    empleado.Asistente("Javier Vargas", jefes[0]),
    empleado.Asistente("Luis Ramírez", jefes[1]),
    empleado.Asistente("Andrea Soto", jefes[2]),
    empleado.Asistente("Elena Ortiz", jefes[3]),
]

# Crear técnicos (mínimo 3, máximo 5 por área)
tecnicos = [
    empleado.Tecnico("Pedro Castillo", jefes[0], 3),
    empleado.Tecnico("Javier Díaz", jefes[0], 5),
    empleado.Tecnico("Fernando Sánchez", jefes[1], 2),
    empleado.Tecnico("Hugo Paredes", jefes[1], 4),
    empleado.Tecnico("Erick Pérez", jefes[1], 1),
    empleado.Tecnico("Rosa Medina", jefes[2], 3),
    empleado.Tecnico("Daniel Suárez", jefes[3], 5),
    empleado.Tecnico("Gabriel Fuentes", jefes[4], 2),
    empleado.Tecnico("Cristina Vargas", jefes[4], 4)
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