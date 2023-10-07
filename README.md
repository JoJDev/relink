# Relink

Pequeño proyecto de Django para acortar enlaces de internet y compartirlos.

*ver. 1.0.0 (prototipo MVP)*

>Relink es un sitio web para crear URLs de redireccionamiento, permite crear tus propias URLs y personalizarlas para que sean cortas y faciles de recordar, y que estas redireccionen a otro enlace en especifico para mejorar su presentación y mantenimiento.

## Usos

Relink puede ser especialmente util para los siguientes casos:

- **Actualizar URLs:** Para no tener que repostear un link si este dejase de estar disponible o estuviese roto el enlace.
- **Facil de compartir:** Al ser corto y personalizable, es facil de compartir con otros y de recordar.
- **Tener tu dominio en el URL:** Permitir que varios nombres de dominio pertenecientes al mismo propietario hagan referencia a un único sitio web.
- **Publicidad:** Para promocionar tu sitio web y/o marca al tener que pasar por tu redireccionador de URL.
- **Navegación:** Para guiar la navegación dentro y fuera de un sitio web.
- **Protección de la privacidad:** Para proteger la privacidad tanto del usuario como del admin, al ocultar datos del URL destino.

## Tecnologias

- Python *3.10.9*
- Django *4.2.5*
- Django Bootstrap5 *23.3*
- SQLite


# Modo de uso

Una vez instaladas sus dependencias (`requirements.txt`) e implementadas las migraciones y un superusuario (Instalación de un proyecto Django promedio), puedes ir al *admin page* por defecto y empezar a crear y modificar tus enlaces.