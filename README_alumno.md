# 🏥 Sistema de Gestión para una Clínica Médica

Trabajo práctico final – Computación I – Universidad de Mendoza  
Carrera: Ingeniería en Informática – Año: 2025

---

## 📁 Estructura del Proyecto

```
/trabajo_clinica/
│
├── clases/                # Lógica del modelo
│   ├── paciente.py
│   ├── medico.py
│   ├── especialidad.py
│   ├── turno.py
│   ├── receta.py
│   ├── historiaclinica.py
│   ├── clinica.py
│   └── excepciones.py
│
├──  cli.py                  # Interfaz por consola
│ 
├── test/                  # Pruebas unitarias por clase
│   ├── test_paciente.py
│   ├── test_medico.py
│   ├── test_especialidad.py
│   ├── test_turno.py
│   ├── test_receta.py
│   ├── test_historiaclinica.py
│   ├── test_clinica.py
│   ├── test_excepciones.py
│   └── test_cli.py
│
├── README_alumno.md              # Documentación
```

---

## ▶️ Ejecución del sistema

Desde consola, **siempre ejecutar desde el directorio raíz**:

```bash
python cli.py

Menú disponible:
- Agregar paciente o médico
- Agendar turno (valida fecha, día y disponibilidad)
- Emitir receta (verifica existencia y contenido)
- Ver historia clínica
- Listar pacientes, médicos y turnos

---

## ✅ Ejecutar los tests

Desde el directorio raíz:

```bash
python -m unittest discover -s test
```

O ejecutar uno en particular:

```bash
python test/test_clinica.py
```

---

## 🧠 Diseño general

### Separación por responsabilidades
- `clases/`: contiene las entidades del dominio.
- `cli.py`: contiene la interfaz que usa el usuario final.
- `test/`: tests organizados por clase con `unittest`.

### Principales clases y responsabilidades

| Clase              | Rol principal                                 |
|-------------------|-----------------------------------------------|
| `Paciente`        | Datos del paciente                            |
| `Medico`          | Datos del médico y sus especialidades         |
| `Especialidad`    | Tipo y días de atención                       |
| `Turno`           | Relación paciente-médico en fecha y hora      |
| `Receta`          | Lista de medicamentos recetados               |
| `HistoriaClinica` | Registro de turnos y recetas por paciente     |
| `Clinica`         | Orquesta todo el sistema                      |
| `CLI`             | Interfaz por consola del sistema              |

### Excepciones personalizadas
- `PacienteNoEncontradoException`
- `MedicoNoEncontradoException`
- `TurnoDuplicadoException`
- `RecetaInvalidaException`

---

## 🧪 Cobertura de pruebas
- Cada clase tiene su propio archivo de test.
- Se utilizan `unittest.TestCase`, mocks y `assert` personalizados.
- El CLI se prueba mediante `unittest.mock.patch` simulando entradas.

---

## 👨‍💻 Autor

- Sebastian Meirno 
- Legajo: 63284  
- Fecha: Junio 2025
