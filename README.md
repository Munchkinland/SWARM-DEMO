# Idiom Bot Manager

## Descripción
El "Idiom Bot Manager" es una aplicación de escritorio que utiliza agentes inteligentes para explicar modismos en inglés y español. Utiliza la biblioteca PyQt6 para la interfaz de usuario y permite a los usuarios seleccionar un modismo y recibir explicaciones proporcionadas por expertos en cada idioma.

## Concepto de Swarm de OpenAI
El enfoque de *swarm* de OpenAI se basa en la colaboración y coordinación entre múltiples agentes o modelos que trabajan en conjunto para resolver problemas complejos. Este concepto se inspira en la forma en que los grupos de organismos (como bandadas de pájaros o enjambres de insectos) se organizan y colaboran para alcanzar objetivos comunes.

En el contexto del "Idiom Bot Manager", se aplica el concepto de *swarm* al permitir que diferentes agentes, como el *English Expert*, *Spanish Expert*, y *Game Master*, trabajen de manera coordinada para proporcionar explicaciones precisas y útiles sobre los modismos seleccionados por el usuario. Cada agente aporta su especialización y conocimiento, permitiendo un flujo de trabajo eficiente y una mejor experiencia de usuario.

## Características
- Interfaz gráfica de usuario (GUI) intuitiva.
- Selección de modismos en inglés y español.
- Explicaciones generadas por expertos en sus respectivos idiomas.
- Registro de historial de tareas asignadas.
- Capacidad para restablecer el estado de los agentes.

## Requisitos
Asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- PyQt6
- NumPy
- Pandas

Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt

## Uso

    Clona el repositorio o descarga los archivos del proyecto.
    Navega al directorio del proyecto.
    Ejecuta la aplicación utilizando el siguiente comando:

    python main.py

    Selecciona un modismo de la lista y haz clic en "Get Explanation" para recibir la explicación correspondiente.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un "issue" o envía un "pull request".

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.