#Paciente de una clinica

class Paciente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: str):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
    
    def obtener_dni(self) -> str:
        return self.dni
    
    def __str__(self) -> str:
        return f"Paciente: {self.nombre} (DNI: {self.dni}) - Nacimiento: {self.fecha_nacimiento}"