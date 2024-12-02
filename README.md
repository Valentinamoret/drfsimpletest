Esta API en Django permite gestionar proyectos a través de operaciones CRUD (Crear, Leer, Actualizar, Eliminar). 

Características
Crear proyectos: Añadir nuevos proyectos al sistema.
Listar proyectos: Obtener una lista de todos los proyectos disponibles.
Obtener un proyectos: Ver los detalles de un proyectos específico por su ID.
Actualizar proyectos: Editar la información de un proyectos existente.
Eliminar proyectos: Eliminar un proyectos del sistema.

Tecnologías Utilizadas
Framework: Django REST Framework
Servidor de aplicación: Gunicorn
Base de datos: PostgreSQL
Despliegue: Render.com

Endpoints
Crear un proyecto
POST /api/projects/

Listar todos los proyectos
GET /api/projects/

Obtener un proyecto por ID
GET /api/projects/{id}/

Actualizar un proyecto
PUT /api/projects/{id}/

Eliminar un proyecto
DELETE /api/projects/{id}/

Códigos de Estado HTTP
200 OK – Solicitud exitosa.
201 Created – Objeto creado exitosamente.
400 Bad Request – Error en la solicitud.
404 Not Found – Objeto no encontrado.
500 Internal Server Error – Error en el servidor.
