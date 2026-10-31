# Informe de pruebas — API Académica

Autor: Libardo Morales Gutierrez

Pruebas ejecutadas contra la API real (Uvicorn + SQLite) y registradas con sus respuestas. Evidencia: capturas de Swagger en `evidencias/`.

| Caso | Endpoint | Datos enviados | Resultado esperado | Resultado obtenido | HTTP | Estado |
|---|---|---|---|---|---|---|
| P01 | POST /courses | `{"name": "Desarrollo Web II", "credits": 3, "active": true}` | 201 y curso con ID | `{"id": 1, "name": "Desarrollo Web II", "credits": 3, "active": true}` | 201 | APROBADO |
| P02 | POST /courses | `{"name": "Redes", "credits": 3, "active": true}` | 201 y curso con ID | `{"id": 2, "name": "Redes", "credits": 3, "active": true}` | 201 | APROBADO |
| P03 | POST /courses | `{"name": "Bases de Datos", "credits": 4, "active": true}` | 201 y curso con ID | `{"id": 3, "name": "Bases de Datos", "credits": 4, "active": true}` | 201 | APROBADO |
| P04 | GET /courses/1 | `—` | 200 y curso 1 | `{"id": 1, "name": "Desarrollo Web II", "credits": 3, "active": true}` | 200 | APROBADO |
| P05 | DELETE /courses/2 | `—` | 200 {message: Course deleted} | `{"message": "Course deleted"}` | 200 | APROBADO |
| P06 | GET /courses/2 | `—` | 404 Course not found | `{"detail": "Course not found"}` | 404 | APROBADO |
| P07 | GET /courses | `—` | Lista con cursos 1 y 3 | `[{"id": 1, "name": "Desarrollo Web II", "credits": 3, "active": true}, {"id": 3, "name": "Bases de Datos", ...` | 200 | APROBADO |
| P08 | DELETE /courses/2 | `—` | 404 Course not found | `{"detail": "Course not found"}` | 404 | APROBADO |
| P09 | DELETE /courses/abc | `—` | 422 | `{"detail": [{"type": "int_parsing", "loc": ["path", "course_id"], "msg": "Input should be a valid integer, ...` | 422 | APROBADO |
| P10 | PUT /courses/1 | `{"name": "Programación II", "credits": 4, "active": false}` | 200, id=1 y active=false | `{"id": 1, "name": "Programación II", "credits": 4, "active": false}` | 200 | APROBADO |
| P11 | GET /courses | `—` | Siguen 2 cursos (no aumenta) | `[{"id": 1, "name": "Programación II", "credits": 4, "active": false}, {"id": 3, "name": "Bases de Datos", "...` | 200 | APROBADO |
| P12 | PUT /courses/1 | `{"name": "Programación II", "credits": 0, "active": true}` | 422 credits=0 | `{"detail": [{"type": "greater_than_equal", "loc": ["body", "credits"], "msg": "Input should be greater than...` | 422 | APROBADO |
| P13 | PUT /courses/1 | `{"name": "Programación II", "credits": 7, "active": true}` | 422 credits=7 | `{"detail": [{"type": "less_than_equal", "loc": ["body", "credits"], "msg": "Input should be less than or eq...` | 422 | APROBADO |
| P14 | PUT /courses/1 | `{"name": "ab", "credits": 3, "active": true}` | 422 nombre corto | `{"detail": [{"type": "string_too_short", "loc": ["body", "name"], "msg": "String should have at least 3 cha...` | 422 | APROBADO |
| P15 | PUT /courses/1 | `{"name": "Programación II", "credits": 3}` | 422 falta active | `{"detail": [{"type": "missing", "loc": ["body", "active"], "msg": "Field required", "input": {"name": "Prog...` | 422 | APROBADO |
| P16 | PUT /courses/999 | `{"name": "Inexistente", "credits": 3, "active": true}` | 404 Course not found | `{"detail": "Course not found"}` | 404 | APROBADO |
| P17 | POST /students | `{"name": "Ana Pérez", "email": "ana@universidad.edu", "semester": 4}` | 201, active=true por defecto | `{"id": 1, "name": "Ana Pérez", "email": "ana@universidad.edu", "semester": 4, "active": true}` | 201 | APROBADO |
| P18 | POST /students | `{"name": "Luis Gómez", "email": "luis@universidad.edu", "semester": 2, "active": false}` | 201, active=false | `{"id": 2, "name": "Luis Gómez", "email": "luis@universidad.edu", "semester": 2, "active": false}` | 201 | APROBADO |
| P19 | GET /students | `—` | Lista con 2 estudiantes | `[{"id": 1, "name": "Ana Pérez", "email": "ana@universidad.edu", "semester": 4, "active": true}, {"id": 2, "...` | 200 | APROBADO |
| P20 | GET /students/1 | `—` | 200 estudiante 1 | `{"id": 1, "name": "Ana Pérez", "email": "ana@universidad.edu", "semester": 4, "active": true}` | 200 | APROBADO |
| P21 | GET /students/999 | `—` | 404 Student not found | `{"detail": "Student not found"}` | 404 | APROBADO |
| P22 | GET /students/abc | `—` | 422 | `{"detail": [{"type": "int_parsing", "loc": ["path", "student_id"], "msg": "Input should be a valid integer,...` | 422 | APROBADO |
| P23 | POST /students | `{"name": "Ana Pérez", "email": "a@u.edu", "semester": 0}` | 422 semester=0 | `{"detail": [{"type": "greater_than_equal", "loc": ["body", "semester"], "msg": "Input should be greater tha...` | 422 | APROBADO |
| P24 | POST /students | `{"name": "Ana Pérez", "email": "a@u.edu", "semester": 11}` | 422 semester=11 | `{"detail": [{"type": "less_than_equal", "loc": ["body", "semester"], "msg": "Input should be less than or e...` | 422 | APROBADO |
| P25 | POST /students | `{"name": "An", "email": "a@u.edu", "semester": 3}` | 422 nombre corto | `{"detail": [{"type": "string_too_short", "loc": ["body", "name"], "msg": "String should have at least 3 cha...` | 422 | APROBADO |
| P26 | POST /students | `{"name": "Ana Pérez", "email": "", "semester": 3}` | 422 email vacío | `{"detail": [{"type": "string_too_short", "loc": ["body", "email"], "msg": "String should have at least 1 ch...` | 422 | APROBADO |
| P27 | GET /courses | `—` | Tras reiniciar: curso 1 actualizado (Programación II, false), sin curso 2 | `[{"id": 1, "name": "Programación II", "credits": 4, "active": false}, {"id": 3, "name": "Bases de Datos", "...` | 200 | APROBADO |
| P28 | GET /students | `—` | Tras reiniciar: 2 estudiantes persisten | `[{"id": 1, "name": "Ana Pérez", "email": "ana@universidad.edu", "semester": 4, "active": true}, {"id": 2, "...` | 200 | APROBADO |
| P29 | GET /courses/2 | `—` | Tras reiniciar: curso 2 sigue eliminado | `{"detail": "Course not found"}` | 404 | APROBADO |

**Resumen:** 29/29 casos aprobados.

P27–P29 se ejecutaron después de detener y reiniciar Uvicorn (persistencia en `database.db`).

## Evidencias

| Archivo | Casos que respalda |
|---|---|
| `evidencias/00_swagger_rutas.png` | Swagger muestra las rutas de Courses y Students |
| `evidencias/01_post_courses_201.png` | P01–P03 (POST /courses, 201) |
| `evidencias/02_put_courses_200.png` | P10 (PUT, mismo id) |
| `evidencias/03_put_courses_422.png` | P12–P15 (validación 422) |
| `evidencias/04_delete_courses_200.png` | P05 (DELETE, 200) |
| `evidencias/05_delete_courses_404.png` | P06, P08 (404) |
| `evidencias/06_post_students_201.png` | P17–P18 (POST /students) |
| `evidencias/07_get_students_404.png` | P21 (Student not found) |
