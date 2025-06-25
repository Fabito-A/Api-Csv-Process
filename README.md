# 📦 Api‑Csv‑Process

API en Flask para procesar archivos CSV y gestionar una base de datos SQLite.

---

## 🗂️ Estructura del proyecto

```
Api‑Csv‑Process/
├── app/
│   ├── database/                # Carpeta para la base de datos SQLite
│   ├── src/
│   │   └── archivos/            # CSV de ejemplo
│   └── procesar_Csv.py         # Módulo de procesamiento CSV
└── controlador.py              # Servidor Flask y rutas API
```

---

## 🚀 Funcionalidades

### 1. `controlador.py`

Implementa las siguientes rutas en Flask:

- **`GET /creaDb`**  
  Crea `basedatos_001.sqlite3` en `app/database` si no existe.

- **`GET /insertarCsv/<nombre_archivo>`**  
  Inserta datos desde `app/src/archivos/<nombre_archivo>.csv` en una tabla con el mismo nombre (sin extensión).

- **`GET /borrarTb/<nombre_tabla>`**  
  Elimina la tabla especificada en la base de datos.

- **`GET /consultar`**  
  Devuelve todos los registros de la base de datos en formato JSON.

Para iniciar el servidor:
```bash
python controlador.py
```
Luego, accede a `http://127.0.0.1:5000`.

---

### 2. `procesar_Csv.py`

- Lee el archivo CSV con **pandas**.
- Inserta los datos directamente en la base de datos, creando una tabla con el nombre del archivo (sin extensión).
- Utiliza `DataFrame.to_sql()` para la inserción automática.

---

## 📌 Endpoints disponibles

| Ruta                                  | Método | Descripción                                                  |
|---------------------------------------|--------|--------------------------------------------------------------|
| `/creaDb`                             | GET    | Crear base de datos si no existe                            |
| `/insertarCsv/<nombre_archivo>`       | GET    | Insertar datos del CSV en tabla (nombre = archivo)          |
| `/borrarTb/<nombre_tabla>`            | GET    | Eliminar tabla en SQLite                                    |
| `/consultar`                          | GET    | Obtener todas las tablas y registros en formato JSON        |

---

## 📚 Dependencias

Agrega estas líneas en `requirements.txt`:

```
flask
pandas
```

Instalación:
```bash
pip install -r requirements.txt
```

---

## 🧪 Ejemplo de uso

1. Coloca tu archivo CSV en `app/src/archivos/`.
2. Inicia el servidor:
   ```bash
   python controlador.py
   ```
3. Accede a la API desde tu navegador o vía `curl`:
   - `GET /creaDb`
   - `GET /insertarCsv/mi_archivo`
   - `GET /consultar`
   - `GET /borrarTb/mi_archivo`

---

## ✅ Estado actual

- ✅ Creación de la base de datos automática  
- ✅ Lectura y procesamiento de CSV con pandas  
- ✅ Inserción en SQLite con nombre de tabla dinámico  
- ✅ Endpoints funcionales de creación, inserción, borrado y consulta
---

http://127.0.0.1:5000/consultar <-  consulta el contenido de la base de datos con un formato json
http://127.0.0.1:5000/borrarTb/"nombre base datos" <-borra el contenido de la base de datos
http://127.0.0.1:5000/insertarCsv/"nombre archivo" <-inserta los registros bajo el nombre del archivo que debe estar por el momento ubicado en Proyecto_web/app/src/archivos 
http://127.0.0.1:5000/creaDb  <-crea la base de datos si no existe bajo el nombre de basedatos_001.sqlite3
