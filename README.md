# Sistema de Información - Cultura, Recreación y Deporte  
**Universidad del Valle**

Sistema de gestión desarrollado con React.js + Vite en el frontend y Django + PostgreSQL en el backend.

## 📋 Tabla de Contenidos
- [Tecnologías](#tecnologías)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
  - [Backend (Django)](#backend-django)
  - [Frontend (React + Vite)](#frontend-react--vite)
- [Ejecución en Local](#ejecución-en-local)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Características](#características)
- [Paleta de Colores](#paleta-de-colores)

## 🛠 Tecnologías

### Frontend
- **React.js** 18.3.1 - Construcción de Interfaces Web Modulares
- **Vite** 5.0 - Herramienta de desarrollo y empaquetado
- **Node.js** 20.19.0 - Entorno de ejecución
- **Material UI** 6.1.3 - Biblioteca de componentes
- **Zustand** 4.5.5 - Gestión del estado global
- **React Router DOM** 7.x - Enrutamiento

### Backend
- **Django** 5.2 - Framework web
- **Django REST Framework** 3.16.0 - APIs RESTful
- **Python** 3.12+ - Lenguaje de programación
- **PostgreSQL** 17.4 - Base de Datos Relacional
- **django-cors-headers** 4.3.1 - Manejo de CORS

## 📦 Requisitos Previos

### Para el Backend:
- Python 3.12 o superior
- PostgreSQL 17.4 (o SQLite para desarrollo)
- pip (gestor de paquetes de Python)

### Para el Frontend:
- Node.js 20.19.0 o superior
- npm 10.x o superior

## 🚀 Instalación y Configuración

### Backend (Django)

1. **Navegar al directorio del backend**
   ```bash
   cd backend
   ```

2. **Crear y activar entorno virtual**
   ```bash
   # En Linux/Mac
   python3 -m venv venv
   source venv/bin/activate

   # En Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   
   **Opción A: PostgreSQL (Producción)**
   - Instalar PostgreSQL 17.4
   - Crear base de datos:
     ```sql
     CREATE DATABASE univalle_db;
     CREATE USER postgres WITH PASSWORD 'postgres';
     GRANT ALL PRIVILEGES ON DATABASE univalle_db TO postgres;
     ```
   - El archivo `config/settings.py` ya está configurado para PostgreSQL

   **Opción B: SQLite (Desarrollo)**
   - Editar `backend/config/settings.py` y descomentar la configuración de SQLite:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
     ```

5. **Ejecutar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```
   
   El backend estará disponible en: `http://localhost:8000`
   Admin panel: `http://localhost:8000/admin`
   API Browsable: `http://localhost:8000/api/`

### Frontend (React + Vite)

1. **Navegar al directorio del frontend**
   ```bash
   cd frontend
   ```

2. **Instalar dependencias**
   ```bash
   npm install
   ```

3. **Ejecutar servidor de desarrollo**
   ```bash
   npm run dev
   ```
   
   El frontend estará disponible en: `http://localhost:5173`

4. **Para compilar para producción**
   ```bash
   npm run build
   ```

## ▶️ Ejecución en Local

### Iniciar ambos servidores

1. **Terminal 1 - Backend:**
   ```bash
   cd backend
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   python manage.py runserver
   ```

2. **Terminal 2 - Frontend:**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Acceder a la aplicación:**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000/api/
   - Admin Django: http://localhost:8000/admin

### Credenciales por defecto para desarrollo:
- Las credenciales se configuran al crear el superusuario
- El login del frontend actualmente usa autenticación mock (para desarrollo)

## 📁 Estructura del Proyecto

```
Pruebastesis/
├── backend/
│   ├── config/              # Configuración de Django
│   │   ├── settings.py      # Configuración principal
│   │   ├── urls.py          # URLs principales
│   │   └── wsgi.py
│   ├── core/                # App principal con tablas base
│   │   ├── models.py        # Modelos de datos
│   │   ├── serializers.py   # Serializers DRF
│   │   ├── views.py         # ViewSets API
│   │   ├── urls.py          # URLs de la app
│   │   └── admin.py         # Admin Django
│   ├── users/               # App de usuarios
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── manage.py
│   └── requirements.txt     # Dependencias Python
│
└── frontend/
    ├── src/
    │   ├── components/      # Componentes reutilizables
    │   │   └── Sidebar.jsx
    │   ├── layouts/         # Layouts de página
    │   │   └── DashboardLayout.jsx
    │   ├── pages/           # Páginas principales
    │   │   ├── Login.jsx
    │   │   ├── Dashboard.jsx
    │   │   └── Users.jsx
    │   ├── store/           # Estado global (Zustand)
    │   │   └── authStore.js
    │   ├── theme.js         # Tema de Material UI
    │   ├── App.jsx          # Componente principal
    │   └── main.jsx         # Punto de entrada
    ├── package.json
    └── vite.config.js
```

## ✨ Características

### Funcionalidades Implementadas:

1. **Sistema de Autenticación**
   - Login con diseño split-screen
   - Gestión de sesión con Zustand
   - Protección de rutas

2. **Dashboard Responsivo**
   - Sidebar navegable
   - Vista general con estadísticas
   - Diseño adaptativo para mobile y desktop

3. **CRUD de Usuarios**
   - Listado de usuarios
   - Crear nuevo usuario
   - Editar usuario existente
   - Eliminar usuario
   - Validación de formularios

4. **Tablas Base del Sistema**
   - Estados
   - Áreas y Sedes
   - Campus
   - Roles del Sistema
   - Tipos de Préstamo, Actividad, Solicitud
   - Y más... (ver models.py)

5. **API RESTful**
   - Endpoints para todas las entidades
   - Paginación
   - Autenticación de sesión
   - API navegable (Django REST Framework)

## 🎨 Paleta de Colores

Basada en la identidad visual de la Universidad del Valle:

### Colores Principales:
- **Rojo Principal**: `#C20E1A` - Color institucional
- **Rojo Oscuro**: `#841F1C` - Color funcional

### Colores Funcionales:
- **Gris**: `#636363` - Texto secundario
- **Azul**: `#RD5AA2` - Información

### Colores Expresivos:
- **Verde**: `#599876` - Éxito
- **Naranja**: `#DC911B` - Advertencia

### Tipografía:
- **Fuente Principal**: Open Sans
- **Tamaños**:
  - Títulos principales: 400-50px
  - Títulos de pantalla: 200-50px
  - Títulos secundarios: 200-35px
  - Subtítulos: 200-46px
  - Cuerpo principal: 400-15px
  - Cuerpo secundario: 200-13px

## 🔧 Scripts Disponibles

### Backend:
```bash
python manage.py makemigrations  # Crear migraciones
python manage.py migrate         # Aplicar migraciones
python manage.py createsuperuser # Crear admin
python manage.py runserver       # Iniciar servidor
```

### Frontend:
```bash
npm run dev      # Servidor de desarrollo
npm run build    # Compilar para producción
npm run preview  # Vista previa de producción
npm run lint     # Linter de código
```

## 📝 Notas Adicionales

- El frontend usa autenticación mock para desarrollo. Conectar con el backend Django para producción.
- PostgreSQL es recomendado para producción, pero SQLite funciona para desarrollo local.
- Todos los componentes son responsivos y siguen las guías de Material UI.
- El código sigue las convenciones de Django y React/ES6.

## 🤝 Contribución

Para contribuir al proyecto:
1. Crear una rama feature desde main
2. Realizar los cambios
3. Enviar un pull request

## 📄 Licencia

Este proyecto es propiedad de la Universidad del Valle.

---

**Desarrollado para la Sección de Cultura, Recreación y Deporte - Universidad del Valle**
