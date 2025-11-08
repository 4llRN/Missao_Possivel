from PPlay.sprite import Sprite
from PPlay.window import Window
from PPlay.gameimage import GameImage

Tam_x, Tam_y = 1440, 900
janela = Window(Tam_x, Tam_y)
janela.set_title("Joguito")

teclado = janela.get_keyboard()

Fundo = GameImage("fundooooo.png")
menu = GameImage("menu.xcf")
menu_pausa = Sprite("pausa.xcf") 
menu_pausa.set_position(janela.width / 2 - menu_pausa.width / 2, janela.height / 2 - menu_pausa.height / 2)

vel_x, vel_y, vel_tiro, tam = 500, 500, 800, 25
branco = (255, 255, 255)
amarelo = (255, 255, 0)

flavia = Sprite("fla.xcf")
flavia.set_position(900, 400)
wumberto = Sprite("wum.xcf")
wumberto.set_position(900, 600)
ini1 = Sprite("ini1.xcf")
ini1.set_position(100, 400)
ini2 = Sprite("ini2.xcf")
ini2.set_position(700, 400)
ini3 = Sprite("ini3.xcf")
ini3.set_position(50, 400)

tirosD = []
tirosE = []
timer = 0

fla_D, wum_D, vedade = True, True, True
esc_anterior, space_anterior = False, False

frames = 0.0
n_frames = 0
fps = 0
state = "menu"
fase = "primeira"

frac_dis_max = 0.66

def anda_generico(objeto, cima, baixo, esquerda, direita, dt):
    if teclado.key_pressed(cima):
        objeto.y -= vel_y * dt
    if teclado.key_pressed(baixo):
        objeto.y += vel_y * dt
    if teclado.key_pressed(esquerda):
        objeto.x -= vel_x * dt
    if teclado.key_pressed(direita):
        objeto.x += vel_x * dt
        
def n_sai_da_tela(person):
    if person.x <= 0:
        person.x = 0
    elif person.x + person.width >= janela.width:
        person.x = janela.width - person.width
        
    if person.y >= janela.height - person.height:
        person.y = janela.height - person.height

    elif person.y <= janela.height * frac_dis_max - person.height:
        person.y = janela.height * frac_dis_max - person.height

def da_tiro_D():
    tiroD = Sprite("bala.png")
    tiroD.set_position(flavia.x + flavia.width, flavia.y + 40) 
    tirosD.append(tiroD)

def da_tiro_E():
    tiroE = Sprite("bala_reverse.png")
    tiroE.set_position(flavia.x - tiroE.width, flavia.y + 40) 
    tirosE.append(tiroE)

while vedade:
    delta_time = janela.delta_time()
    esc_atual = teclado.key_pressed("ESC")
    
    if state == "menu":
        menu.draw()
        if teclado.key_pressed("esc"):
            exit()
        if teclado.key_pressed("Q"):
            state = "jogando"
            
    elif state == "jogando":
        Fundo.draw()
        timer += delta_time
        frames += delta_time
        n_frames += 1
        if frames >= 1:
            fps = n_frames/frames
            frames = 0.0
            n_frames = 0
        if teclado.key_pressed("space"):
            if timer >= 0.5:
                timer = 0
                if fla_D:
                    da_tiro_D()
                else:
                    da_tiro_E()
        
        for i in range(len(tirosD) - 1, -1, -1):
            tiro = tirosD[i]
            tiro.draw()
            tiro.x += vel_tiro * delta_time
            
            if tiro.x >= janela.width:
                tirosD.pop(i) 
                
        for i in range(len(tirosE) - 1, -1, -1):
            tiro = tirosE[i]
            tiro.draw()
            tiro.x -= vel_tiro * delta_time
            
            if tiro.x + tiro.width <= 0:
                tirosE.pop(i) 

        anda_generico(flavia, "W", "S", "A", "D", delta_time)
        anda_generico(wumberto, "UP", "DOWN", "LEFT", "RIGHT", delta_time)

        if teclado.key_pressed("D"):
            fla_D = True
        if teclado.key_pressed("A"):
            fla_D = False
        if teclado.key_pressed("RIGHT"):
            wum_D = True
        if teclado.key_pressed("LEFT"):
            wum_D = False

        personagens = [flavia, wumberto, ini1, ini2, ini3]
        for perssonagem in personagens:
            n_sai_da_tela(perssonagem)
            perssonagem.draw()

        if esc_atual and not esc_anterior:
            state = "pausa"
        janela.draw_text(f"FPS: {int(fps)}", 10, 10, size=24, color=(amarelo), bold=True)
            
    elif state == "pausa":
        menu_pausa.draw()
        janela.draw_text("Esc para voltar ao jogo", janela.width / 2 - 100, janela.height / 2 + 200, tam, branco, "Calibri", True)
        janela.draw_text("Espaço para voltar ao menu", janela.width / 2 - 120, janela.height / 2 + 250, tam, branco, "Calibri", True)
        
        if esc_atual and not esc_anterior:
            state = "jogando"

        space_atual = teclado.key_pressed("SPACE")
        if space_atual and not space_anterior:
             state = "menu"
        space_anterior = space_atual

    esc_anterior = esc_atual
    janela.update()