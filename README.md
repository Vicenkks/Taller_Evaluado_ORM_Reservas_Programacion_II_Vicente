# Sistema de Gestión de salas y reservas

Sistema de gestión de salas y reservas desarrollado en **Python**, utilizando **SQLAlchemy ORM** y **SQLite** como base de datos.

## Datos del estudiante

- **Nombre:** Vicente Huilcaman
- **Asignatura:** Programacion 2
- **Docente:** Pedro Gaete

## Requisitos previos
- uv.
- git.

### Instalación de uv

En Linux o macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

En Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Para comprobar la instalación:

```bash
uv --version
```

## Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Vicenkks/Taller_Evaluado_ORM_Reservas_Programacion_II.git
```

Ingresar a la carpeta

### 2. Instalar las dependencias

Ejecutar:

```bash
uv sync
```

### 3. Ejecutar el programa

```bash
uv run python menu.py
```

### Ejecución sin uv (Python normal)

**1. Crear el entorno virtual:**

```bash
python3 -m venv .venv
```

**2. Activar el entorno virtual (Linux/macOS):**

```bash
source .venv/bin/activate
```

**3. Instalar dependencias:**

```bash
python -m pip install sqlalchemy
```

**4. Ejecutar el sistema:**

```bash
python menu.py
```

**5. Desactivar el entorno virtual al finalizar:**

```bash
deactivate
```

### Casos de prueba
```

        ========== SISTEMA DE BIBLIOTECA ==========
        1. Registrar sala
        2. Consultar salas
        3. Registrar reserva
        4. Consultar reservas
        5. Cancelar reserva
        0. Salir
        
Seleccione una opción: 1
Nombre de la sala: A
Capacidad: 6

        ========== SISTEMA DE BIBLIOTECA ==========
        1. Registrar sala
        2. Consultar salas
        3. Registrar reserva
        4. Consultar reservas
        5. Cancelar reserva
        0. Salir
        
Seleccione una opción: 1
Nombre de la sala: B
Capacidad: 4

        ========== SISTEMA DE BIBLIOTECA ==========
        1. Registrar sala
        2. Consultar salas
        3. Registrar reserva
        4. Consultar reservas
        5. Cancelar reserva
        0. Salir
        
Seleccione una opción: 3
Nombre del estudiante: Ana
ID de la sala: 1
Fecha AAAA-MM-DD: 2026-11-09

        ========== SISTEMA DE BIBLIOTECA ==========
        1. Registrar sala
        2. Consultar salas
        3. Registrar reserva
        4. Consultar reservas
        5. Cancelar reserva
        0. Salir
        
Seleccione una opción: 3       
Nombre del estudiante: Pedro
ID de la sala: 1
Fecha AAAA-MM-DD: 2026-11-09  
Sala no disponible

        ========== SISTEMA DE BIBLIOTECA ==========
        1. Registrar sala
        2. Consultar salas
        3. Registrar reserva
        4. Consultar reservas
        5. Cancelar reserva
        0. Salir
        
Seleccione una opción: 4

        ---- Sala ----
        ID: 1
        Reservado por: Ana
        Sala: 1
        Fecha: 2026-11-09 00:00:00
    

        ========== SISTEMA DE BIBLIOTECA ==========
        1. Registrar sala
        2. Consultar salas
        3. Registrar reserva
        4. Consultar reservas
        5. Cancelar reserva
        0. Salir
        
Seleccione una opción: 5
ID de la reserva: 1
Reserva cancelada

        ========== SISTEMA DE BIBLIOTECA ==========
        1. Registrar sala
        2. Consultar salas
        3. Registrar reserva
        4. Consultar reservas
        5. Cancelar reserva
        0. Salir
        
Seleccione una opción: 3
Nombre del estudiante: Pedro
ID de la sala: 1 
Fecha AAAA-MM-DD: 2026-11-09

        ========== SISTEMA DE BIBLIOTECA ==========
        1. Registrar sala
        2. Consultar salas
        3. Registrar reserva
        4. Consultar reservas
        5. Cancelar reserva
        0. Salir
        
Seleccione una opción: 0 
```
