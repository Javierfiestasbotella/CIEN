<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Juego de CIEN</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #FF5733;
            text-align: center;
        }
        h2 {
            color: #FF5733;
        }
        p {
            margin-bottom: 10px;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li::before {
            content: "•";
            color: #FF5733;
            display: inline-block;
            width: 1em;
            margin-left: -1em;
        }
    </style>
</head>
<body>
    <h1>Juego de CIEN</h1>
    <p>El juego de CIEN es una emocionante experiencia implementada en Python utilizando la biblioteca Pygame. Este juego recrea la diversión de lanzar dados y acumular puntos mientras compites contra un oponente para alcanzar la meta de 100 puntos primero.</p>

    <h2>Requisitos</h2>
    <ul>
        <li>Python 3.x: Asegúrate de tener Python instalado. Puedes descargarlo desde <a href="https://www.python.org/downloads/">python.org</a>.</li>
        <li>Pygame: Pygame es una biblioteca de Python diseñada para la creación de videojuegos. Puedes instalar Pygame utilizando el siguiente comando en tu terminal:</li>
    </ul>
    <pre><code>pip install pygame</code></pre>

    <h2>Instrucciones de Instalación y Ejecución</h2>
    <ul>
        <li>Descarga del Repositorio: Clona o descarga este repositorio en tu máquina local.</li>
        <li>Instalación de Pygame: Una vez descargado el repositorio, instala Pygame utilizando el comando mencionado anteriormente.</li>
        <li>Ejecución del Juego: Navega hasta el directorio donde has clonado o descargado el repositorio y ejecuta el script <code>main.py</code> utilizando Python:</li>
    </ul>
    <pre><code>python main.py</code></pre>

    <h2>Descripción del Juego</h2>
    <p>El juego de CIEN es una adaptación digital del juego de dados clásico. El objetivo principal es ser el primer jugador en acumular 100 puntos o más. Cada jugador tira un dado y suma los puntos obtenidos en cada lanzamiento. Sin embargo, si un jugador obtiene un uno en su tirada, pierde todos los puntos acumulados en esa ronda y pasa el turno al otro jugador.</p>

    <h2>Controles</h2>
    <ul>
        <li>Tirar Dado Izquierdo: Haz clic en el dado izquierdo cuando sea tu turno para lanzar los dados y acumular puntos.</li>
        <li>Tirar Dado Derecho: Haz clic en el dado derecho cuando sea el turno de tu oponente para permitirle lanzar los dados y acumular puntos.</li>
        <li>Responder a la Pregunta de Continuar: Después de cada lanzamiento, se te pedirá que decidas si quieres continuar lanzando o detenerte. Responde "s" para continuar tirando o "n" para detenerte y sumar tus puntos acumulados en esa ronda.</li>
    </ul>

    <h2>Interfaz de Usuario</h2>
    <p>La ventana del juego muestra la disposición del tablero con dos áreas para los jugadores. Cada jugador tiene su nombre, puntos acumulados y puntos de la última tirada visibles en la pantalla. Además, hay dos dados representados gráficamente que se actualizan con los resultados de los lanzamientos.</p>

    <h2>¡A Jugar!</h2>
    <p>Disfruta de la emoción del juego de CIEN mientras compites contra un amigo o contra la inteligencia artificial. ¡Buena suerte y que gane el mejor!</p>
</body>
</html>



