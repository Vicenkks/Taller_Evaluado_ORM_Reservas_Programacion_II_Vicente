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
uv run python main.py
```