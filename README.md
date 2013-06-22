<h1>Pantalla maestra + pantallas esclavas</h1>

<h2>Todas las pantallas tienen la capacidad de</h2>

a. recibir un mensaje OSC ( direccion, "mensaje", x, y, fontsize )

b. dibujarlo

c. asignarse una posición dentro de un conjunto ( propuesta: utilizando un keypad )


<h2>hay una pantalla central que:</h2>

a. saber cuántas otras pantallas esclavas tiene ( al principio será hardcodeado, más adelante las "autodscubrirá"

b. generar un objeto "Canvas" con base en el número total de pantallas

c. recibe todos los mensajes

d. genera las animaciones utilizando puras variables

e. envía mensajes a cada una de las pantallas esclavas para que grafiquen su parte de la animación

f. dibuja también la parte que le corresponde a su pantalla física
