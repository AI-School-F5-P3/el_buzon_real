# El buzón real

## Chatbot de los Reyes Magos

Esta aplicación simula interacciones con los Reyes Magos (Melchor, Gaspar y Baltasar) y su asistente, el Paje Real. Utiliza la API de OpenAI GPT para generar respuestas en el estilo único de cada personaje. Además, permite guardar la lista de regalos de los niños en MongoDB y enviarla por correo electrónico a sus padres.

--- 

## Funcionalidades

### Chat con los Reyes Magos:
- Los niños pueden interactuar con personajes como **Melchor**, **Gaspar**, **Baltasar** o el **Paje Real**.
- Cada personaje tiene una personalidad y un estilo de respuesta únicos.

### Gestión de Listas de Regalos:
- La aplicación almacena las listas de regalos de los niños en una base de datos **MongoDB** para su fácil recuperación y organización.

#3## Notificaciones por Correo Electrónico:
- Una vez finalizada la lista de regalos, esta se envía por correo electrónico a los padres para informarles de los deseos de sus hijos.

---

## Cómo Funciona

### Selección de Personaje:
- El niño comienza la conversación con el **Paje Real**, quien puede transferir el chat a uno de los Reyes Magos según la preferencia del niño.

### Interacción en el Chat:
- Se utiliza la API de **OpenAI GPT** para generar respuestas. Las instrucciones de cada personaje definen su tono y comportamiento durante la conversación.

### Almacenamiento de la Lista de Regalos:
- Los regalos mencionados por el niño durante la conversación se recopilan y guardan en una base de datos **MongoDB**, organizados bajo el nombre del niño.

### Notificación a los Padres:
- Una vez compilada la lista de regalos, se envía un correo electrónico a los padres con un resumen de los regalos.

---