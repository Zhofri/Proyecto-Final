Nombre: Zhofri Guamán 
El objetivo de mi condigo es dar una buena experiencia de jugabalidad a nuestro usuario
Fecha de inicio: 19/12/2023
Fecha de finalización: 23/12/2023
Introducción:
¡Bienvenido al Juego de Piedra, Papel o Tijera implementado en Python!
Este proyecto se ha desarrollado como parte de Lógica de la Programación, explorando y aplicando los conocimientos adquiridos a lo largo de las cuatro unidades del curso.


Descripción del Juego
Este juego clásico, conocido como Piedra, Papel o Tijera, ofrece una experiencia interactiva y divertida para los jugadores. 
Desde la elección de la dificultad hasta la emoción de cada ronda, el juego incorpora principios de programación funcional y conceptos clave de la materia.


Funciones Principales:

obtener_numero_rondas(), obtener_nivel_dificultad(), obtener_nombre_jugador(): 
Estas funciones manejan la configuración inicial del juego, permitiendo al usuario establecer el número de rondas, el nivel de dificultad y su nombre. 
Proporcionan una interfaz clara y reutilizable para obtener información esencial del usuario.

jugar_ronda(): 
Coordina una ronda completa del juego. Dentro de esta función, se invocan otras funciones más específicas, como obtener_eleccion_jugador(), obtener_eleccion_computadora(), y determinar_ganador(). 
Esta abstracción permite una clara separación de responsabilidades, mejorando la legibilidad y mantenibilidad del código.

Funciones de Elección y Ganador
obtener_eleccion_jugador(), obtener_eleccion_computadora():
Estas funciones manejan la lógica de elección tanto para el jugador como para la computadora. 
La función obtener_eleccion_jugador() utiliza un enfoque interactivo y validación de entrada para garantizar elecciones válidas del usuario.

determinar_ganador(): Evalúa las elecciones del jugador y la computadora para determinar el resultado de la ronda. 
La lógica de determinación de ganador está claramente encapsulada en esta función, contribuyendo a la cohesión del código.

Funciones de Puntaje

actualizar_puntaje(): 
Actualiza el puntaje del jugador según el resultado de cada ronda. Esta función refleja la puntuación acumulativa del jugador a lo largo del juego.

Programación Funcional
La programación funcional se incorpora de manera efectiva en varias partes del código:

Uso de Funciones como Ciudadanos de Primera Clase
Las funciones como obtener_eleccion_jugador(), obtener_eleccion_computadora(), y determinar_ganador() son tratadas como ciudadanos de primera clase. 
Son pasadas como argumentos y devueltas por otras funciones, lo que facilita la composición y abstracción de la lógica del juego.

Evitar Efectos Secundarios
Las funciones están diseñadas para evitar efectos secundarios siempre que sea posible. 
La función jugar_ronda(), por ejemplo, coordina las acciones sin modificar directamente variables fuera de su alcance, siguiendo así los principios de programación funcional.
Uso de Funciones:

Eficiencia y Modularidad
La modularidad del código se destaca a través del uso de funciones que realizan tareas específicas. 
Cada función tiene una responsabilidad clara, lo que facilita el mantenimiento y la extensión del programa. 
Por ejemplo, el cambio en la lógica del juego podría manejarse modificando funciones individuales sin afectar otras partes del código.

Implementación de Conceptos Aprendidos:
Las funciones reflejan la aplicación de conceptos aprendidos en las unidades de la materia. 
Desde la entrada y validación del usuario hasta la determinación del ganador, se observa una aplicación efectiva de los principios de programación enseñados en la asignatura.

Manejo de Excepciones:
La función obtener_eleccion_jugador() demuestra el manejo de excepciones para garantizar una entrada válida del usuario.
Esto muestra una comprensión sólida de técnicas avanzadas de programación.

En resumen: la estructura del código y la implementación de la programación funcional demuestran una comprensión profunda de los conceptos de programación y la capacidad para desarrollar un software modular, eficiente y fácilmente mantenible.


Instrucciones de Ejecución

Sigue las instrucciones en pantalla para configurar el juego y disfruta de la experiencia.

Hemos preparado una presentación visual que destaca las características esenciales del juego y su desarrollo. 

Además, el video del proyecto proporciona una visión detallada, desde la exposición inicial hasta la ejecución del juego y la explicación de sus funciones clave.
