class Empleado:
    def __init__(self, nombre, puesto, jefe_inmediato=None, estado="Activo"):
        self.nombre = nombre
        self.puesto = puesto
        self.jefe_inmediato = jefe_inmediato
        self.estado = estado

    def get_resumen(self):
        return f"{self.puesto}"
        
    def get_jefe_inmediato(self):
        return self.jefe_inmediato.nombre if self.jefe_inmediato else "No tiene"

    def get_estado(self):
        return self.estado
    
# Clases derivadas

#clase gerente
class Gerente(Empleado):
    def __init__(self, nombre, estado="Activo"):
        super().__init__(nombre, "Gerente", None, estado)
        
    def set_jefe_inmediato(self, jefe):
        raise ValueError("Un Gerente no puede tener jefe inmediato.")

#clase jefe de área
class JefeDeArea(Empleado):
    def __init__(self, nombre, area, jefe_inmediato, estado="Activo"):
        super().__init__(nombre, f"Jefe de {area}", jefe_inmediato, estado)

#clase técnico
class Tecnico(Empleado):
    def __init__(self, nombre, jefe_inmediato, experiencia, estado="Activo"):
        super().__init__(nombre, "Técnico", jefe_inmediato, estado)
        self.experiencia = experiencia

    def get_resumen(self):
        return f"Técnico ({self.experiencia} años de experiencia)"

#clase asistente
class Asistente(Empleado):
    def __init__(self, nombre, jefe_inmediato, estado="Activo"):
        super().__init__(nombre, "Asistente", jefe_inmediato, estado)
   