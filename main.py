import pygame
import random
import time
import sys
import os

# Obtener la ruta del directorio actual
dir_actual = os.path.dirname(__file__)
dir_cien = os.path.join(dir_actual, "CIEN")

# Definir la clase Jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre  
        self.puntos = 0
        self.acumulado = 0
        self.tirada = None  # Almacenar la última tirada
        self.uno = False

# Función para mostrar información del jugador
def mostrar_info_jugador(jugador, x, y):
    # Definir colores
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    AZUL = (0, 0, 255)
    AMARILLO = (255, 255, 0)
    font = pygame.font.Font(None, 44)
    font2 = pygame.font.Font(None, 24)
    
    # Obtener el color del nombre del jugador según el turno
    color_nombre = AMARILLO if turno == 1 else NEGRO
    
    texto_nombre = font.render(jugador.nombre, True, color_nombre)
    ventana.blit(texto_nombre, (x, y))
    texto_puntos = font2.render(f"Puntos: {jugador.puntos}", True, MARRON_OSCURO)
    ventana.blit(texto_puntos, (x, y + 45))
    texto_acumulado = font2.render(f"Acumulado: {jugador.acumulado}", True, MARRON_OSCURO)
    ventana.blit(texto_acumulado, (x, y + 65))

# Función para obtener una tirada de tres dados
def triple_dado():
    return [random.randint(1, 6) for _ in range(3)]

# Función para tirar el dado y sumar los puntos
def tirar_dado(jugador):
    tirada = triple_dado()
    puntos = sum(tirada)
    jugador.puntos += puntos
    jugador.tirada = tirada  # Almacenar la última tirada
    return puntos

# Función para dibujar la tirada de dados en la ventana
def dibujar_tirada(jugador, rect):
    if jugador.tirada is not None:
        tirada_str = ', '.join(map(str, jugador.tirada))
        font = pygame.font.Font(None, 24)
        texto_tirada = font.render(tirada_str, True, NEGRO)
        ventana.blit(texto_tirada, (rect.centerx - texto_tirada.get_width() // 2, rect.centery + 50))

# Dibujar título del juego
def ver_tirada(jugador,d=0):
    font_tirada = pygame.font.Font(None, 28)
    texto_tirada = font_tirada.render (f"Tirada {jugador.nombre}: {jugador.tirada}", True, ROJO)
    if d==1:
        rect_tirada = texto_tirada.get_rect(midleft=(50, ALTO - 150))
    else:
        rect_tirada = texto_tirada.get_rect(midright=(ANCHO - 50, ALTO - 150))
        
    ventana.blit(texto_tirada, rect_tirada)
    
# Definir una función para actualizar solo la tirada del jugador en la pantalla
def actualizar_tirada(jugador,d=0):
    ventana.blit(fondo_img, (0, 0))
    ver_tirada(jugador,d)
    mostrar_info_jugador(jugador_1, 110, 70)
    mostrar_info_jugador(jugador_2, ANCHO // 2 + 170, 70)
    dibujar_tirada(jugador_1, dado_izquierda_rect)
    dibujar_tirada(jugador_2, dado_derecha_rect)
    ventana.blit(dado_img, dado_izquierda_rect)
    ventana.blit(dado_img, dado_derecha_rect)
    
    # Dibujar línea divisoria en el margen superior
    pygame.draw.line(ventana, NEGRO, (0, 100), (ANCHO, 100), 5)

    # Dibujar línea vertical para separar a los jugadores
    pygame.draw.line(ventana, NEGRO, (ANCHO // 2, 100), (ANCHO // 2, ALTO), 5)
    # Dibujar título del juego
    font_titulo = pygame.font.Font(None, 58)
    texto_titulo = font_titulo.render("CIEN", True, ROJO)
    rect_titulo = texto_titulo.get_rect(center=(ANCHO // 2, 50))
    ventana.blit(texto_titulo, rect_titulo)
    pygame.display.flip()

def fin():
    sonido_ganador.play()
    # Mostrar ganador y cambiar el fondo de la pantalla
    ventana.blit(fondo_ganador, (0, 0))
    font_ganador = pygame.font.Font(None, 72)
    texto_ganador = font_ganador.render(f"¡GANADOR: {jugador_ganador.nombre}!", True, AZUL)
    rect_ganador = texto_ganador.get_rect(center=(ANCHO // 2, ALTO // 2))
    ventana.blit(texto_ganador, rect_ganador)
    pygame.display.flip()
    # Esperar un momento antes de cerrar la ventana
    time.sleep(5)
    pygame.quit()

#_____________________________________________________________
def tirar_dado_left():
    sonido_dado.play()
    while True:
        
        # Tirar el dado para el jugador 1
        puntos = tirar_dado(jugador_1)
        if jugador_1.uno and 1 in jugador_1.tirada:
            sonido_fallo.play()
            jugador_1.puntos=0
            jugador_1.uno=False
            break
        else:        
            ver_tirada(jugador_1, 1)
            actualizar_tirada(jugador_1,1)
            #time.sleep(1)  # Esperar 2 segundos después de mostrar la tirada
            # Preguntar al usuario si quiere volver a tirar
            font_opcion = pygame.font.Font(None, 58)
            texto_opcion = font_opcion.render("¿Quieres volver a tirar? (s/n): ", True, AZUL)
            rect_opcion = texto_opcion.get_rect(midright=(ANCHO - 70, ALTO - 85))
            ventana.blit(texto_opcion, rect_opcion)
            pygame.display.flip()
                
            respuesta = None
            while respuesta not in ('s', 'n'):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            respuesta = 's'
                        elif event.key == pygame.K_n:
                            respuesta = 'n'
                
            if respuesta == 'n':
                jugador_1.acumulado += jugador_1.puntos
                if jugador_1.acumulado > 99:
                    # Cambiar el jugador ganador
                    global jugador_ganador
                    jugador_ganador = jugador_1
                    fin()
                jugador_1.puntos = 0
                jugador_1.uno = False
                break  # Salir del bucle si el usuario no quiere volver a tirar
            else:
                jugador_1.uno = True
                actualizar_tirada(jugador_1, 1)
                tirar_dado_left()
        break

def tirar_dado_right(): 
    sonido_dado.play()   
    while True:
        # Tirar el dado para el jugador 2
        puntos = tirar_dado(jugador_2)
        if jugador_2.uno and 1 in jugador_2.tirada:
            sonido_fallo.play()
            jugador_2.puntos=0
            jugador_2.uno=False

            break
        else:        
            ver_tirada(jugador_2)
            actualizar_tirada(jugador_2)
            #time.sleep(1)  # Esperar 2 segundos después de mostrar la tirada
            # Preguntar al usuario si quiere volver a tirar
            font_opcion = pygame.font.Font(None, 58)
            texto_opcion = font_opcion.render("¿Quieres volver a tirar? (s/n): ", True, AZUL)
            rect_opcion = texto_opcion.get_rect(midright=(ANCHO - 70, ALTO - 85))
            ventana.blit(texto_opcion, rect_opcion)
            pygame.display.flip()
                
            respuesta = None
            while respuesta not in ('s', 'n'):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            respuesta = 's'
                        elif event.key == pygame.K_n:
                            respuesta = 'n'
                
            if respuesta == 'n':
                jugador_2.acumulado += jugador_2.puntos
                if jugador_2.acumulado > 99:
                    # Cambiar el jugador ganador
                    global jugador_ganador
                    jugador_ganador = jugador_2
                    fin()
                jugador_2.puntos = 0
                jugador_2.uno = False
                break  # Salir del bucle si el usuario no quiere volver a tirar
            else:
                jugador_2.uno = True
                actualizar_tirada(jugador_2)
                tirar_dado_right()
        break

def turno_juego(turno, p1, p2):
        if turno == 0:
            return p1
        else:
            return p2
        
def tirada_en_juego(player, turno):
        tirada = triple_dado()
        if player.uno == False:
            tirar_dado_left()
            player.uno = True
            font_opcion = pygame.font.Font(None, 58)
            texto_opcion = font_opcion.render(f'\n{player.player}, Quiere seguir tirando (s/n): ', True, ROJO)
            rect_opcion = texto_opcion.get_rect(midright=(ANCHO - 50, ALTO - 450))
            ventana.blit(texto_opcion, rect_opcion)
         
# Definir la función start()
def start():
    # Inicializar Pygame
    pygame.init()
    sonido_start.play()

    # Definir colores
    CRUDO = (230, 220, 200)
    MARRON_OSCURO = (100, 50, 0)
    ROJO = (200, 0, 0)
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    AZUL = (0, 0, 255)

    # Obtener la ruta de la carpeta de recursos
    ruta_carpeta = "CIEN"

    # Crear la ventana para pedir nombres
    ANCHO_PANTALLA_PEQUENA = 500
    ALTO_PANTALLA_PEQUENA = 400
    pantalla_pequena = pygame.display.set_mode((ANCHO_PANTALLA_PEQUENA, ALTO_PANTALLA_PEQUENA))
    pygame.display.set_caption("CIEN")

    # Cargar la imagen de fondo para la pantalla pequeña
    fondo_img_pequena = pygame.image.load(os.path.join(ruta_carpeta, 'cien.jpeg'))
    fondo_img_pequena = pygame.transform.scale(fondo_img_pequena, (ANCHO_PANTALLA_PEQUENA, ALTO_PANTALLA_PEQUENA))

    # Mostrar pantalla pequeña
    ejecutando_pequena = True
    nombre_jugador_1 = ""
    nombre_jugador_2 = ""
    while ejecutando_pequena:
        pantalla_pequena.blit(fondo_img_pequena, (0, 0))  # Mostrar el fondo de la pantalla pequeña

        # Dibujar el nombre del juego
        font_titulo = pygame.font.Font(None, 40)
        texto_titulo = font_titulo.render("CIEN", True, AZUL)
        rect_titulo = texto_titulo.get_rect(center=(ANCHO_PANTALLA_PEQUENA // 2, 50))
        pantalla_pequena.blit(texto_titulo, rect_titulo)

        # Pedir nombres de los jugadores
        font_input = pygame.font.Font(None, 30)
        texto_input1 = font_input.render("Nombre Jugador 1: " + nombre_jugador_1, True, NEGRO)
        rect_input1 = texto_input1.get_rect(center=(ANCHO_PANTALLA_PEQUENA // 2, 120))
        pantalla_pequena.blit(texto_input1, rect_input1)

        texto_input2 = font_input.render("Nombre Jugador 2: " + nombre_jugador_2, True, NEGRO)
        rect_input2 = texto_input2.get_rect(center=(ANCHO_PANTALLA_PEQUENA // 2, 180))
        pantalla_pequena.blit(texto_input2, rect_input2)

        # Dibujar botón de empezar
        pygame.draw.rect(pantalla_pequena, AZUL, (200, 250, 100, 50))
        font_boton = pygame.font.Font(None, 30)
        texto_boton = font_boton.render("EMPEZAR", True, BLANCO)
        rect_boton = texto_boton.get_rect(center=(ANCHO_PANTALLA_PEQUENA // 2, 275))
        pantalla_pequena.blit(texto_boton, rect_boton)

        # Actualizar la pantalla pequeña
        pygame.display.flip()

        # Manejo de eventos en la pantalla pequeña
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre_jugador_1 == "":
                        nombre_jugador_1 = input("Nombre Jugador 1: ")
                    else:
                        nombre_jugador_2 = input("Nombre Jugador 2: ")
                elif event.key == pygame.K_SPACE:  # Si presiona Espacio, comenzar el juego
                    ejecutando_pequena = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 200 <= x <= 300 and 250 <= y <= 300:
                    ejecutando_pequena = False

    # Crear jugadores
    jugador_1 = Jugador(nombre_jugador_1)
    jugador_2 = Jugador(nombre_jugador_2)

    # Salir de Pygame
    pygame.quit()

if __name__ == '__main__':
    # Cargar el sonido del dado
    pygame.mixer.init()  # Inicializar el módulo de mezcla de sonido
    ruta_carpeta_sonidos = "CIEN"
    sonido_dado = pygame.mixer.Sound(os.path.join(ruta_carpeta_sonidos, "dados.mp3"))
    sonido_ganador = pygame.mixer.Sound(os.path.join(ruta_carpeta_sonidos, "ganador.mp3"))
    sonido_fallo = pygame.mixer.Sound(os.path.join(ruta_carpeta_sonidos, "fallo.mp3"))
    sonido_start = pygame.mixer.Sound(os.path.join(ruta_carpeta_sonidos, "start.mp3"))
    sonido_cambio = pygame.mixer.Sound(os.path.join(ruta_carpeta_sonidos, "cambio.mp3"))

    jugador_1 = Jugador('jugador_1')
    jugador_2 = Jugador('jugador_2')
    start()

    # Inicializar Pygame
    pygame.init()

    # Definir colores
    CRUDO = (230, 220, 200)
    MARRON_OSCURO = (100, 50, 0)
    ROJO = (200, 0, 0)
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    AZUL = (0, 0, 255)

    # Crear la ventana
    ANCHO = 800
    ALTO = 600
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("CIEN")

    # Cargar imagen del dado y definir su posición
    ruta_carpeta_imagenes = "CIEN"
    dado_img = pygame.image.load(os.path.join(ruta_carpeta_imagenes, 'dados.jpeg'))
    dado_img = pygame.transform.scale(dado_img, (90, 90))  # Escalar el dado
    dado_izquierda_rect = dado_img.get_rect(midleft=(50, ALTO - 50))  # Dado izquierdo
    dado_derecha_rect = dado_img.get_rect(midright=(ANCHO - 50, ALTO - 50))  # Dado derecho

    turno = 0

    # Variables para almacenar la última tirada
    ultima_tirada_jugador_1 = None
    ultima_tirada_jugador_2 = None

    # Cargar la imagen de fondo
    fondo_img = pygame.image.load(os.path.join(ruta_carpeta_imagenes, 'fondo.jpeg'))
    fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))  # Ajustar al tamaño de la ventana

    fondo_ganador = pygame.image.load(os.path.join(ruta_carpeta_imagenes, 'ganador.jpeg'))
    fondo_ganador = pygame.transform.scale(fondo_ganador, (ANCHO, ALTO))

    # Ajustar la transparencia (opcional)
    transparencia = 255  # Valor de 0 a 255, donde 0 es completamente transparente y 255 es opaco
    fondo_img.set_alpha(transparencia)

    # Bucle principal del juego
    ejecutando = True
    while ejecutando:
        ventana.blit(fondo_img, (0, 0))

        # Dibujar línea divisoria en el margen superior
        pygame.draw.line(ventana, NEGRO, (0, 100), (ANCHO, 100), 5)

        # Dibujar línea vertical para separar a los jugadores
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2, 100), (ANCHO // 2, ALTO), 5)

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if dado_izquierda_rect.collidepoint(evento.pos) and turno == 0:
                    tirar_dado_left()
                    turno = 1
                    sonido_cambio.play()
                elif dado_derecha_rect.collidepoint(evento.pos) and turno == 1:
                    tirar_dado_right()
                    turno = 0
                    sonido_cambio.play()

        # Dibujar jugadores y sus marcadores
        mostrar_info_jugador(jugador_1, 110, 70)
        mostrar_info_jugador(jugador_2, ANCHO // 2 + 170, 70)

        # Dibujar título del juego
        font_titulo = pygame.font.Font(None, 58)
        texto_titulo = font_titulo.render("CIEN", True, ROJO)
        rect_titulo = texto_titulo.get_rect(center=(ANCHO // 2, 50))
        ventana.blit(texto_titulo, rect_titulo)

        # Dibujar la tirada de dados
        dibujar_tirada(jugador_1, dado_izquierda_rect)
        dibujar_tirada(jugador_2, dado_derecha_rect)

        # Dibujar las imágenes de los dados
        ventana.blit(dado_img, dado_izquierda_rect)
        ventana.blit(dado_img, dado_derecha_rect)

        # Actualizar la pantalla
        pygame.display.flip()

    # Salir de Pygame
    pygame.quit()

