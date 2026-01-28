from PPlay.sprite import Sprite
from PPlay.window import Window
from PPlay.gameimage import GameImage
import random
#    /\     |       |--------| |     |    /\
#   /  \    |       |        | |     |   /  \ 
#  /    \   |       |--------| |-----|  /    \
# /\\\\\\\  |       |          |     | /\\\\\\\
#/        \ |______ |          |     |/        \
Tam_x, Tam_y = 1440, 900
janela = Window(Tam_x, Tam_y)
janela.set_title("Joguito")


#MENU
botao_jogar= Sprite ("claq_a.xcf")
botao_opcao= Sprite ("claq_a.xcf")
botao_sair= Sprite ("claq_a.xcf")
botao_single= Sprite ("claq_a.xcf")
botao_mult= Sprite ("claq_a.xcf")

botao_jogar.set_position(janela.width/2 - botao_opcao.width/2, 350)
botao_opcao.set_position(janela.width/2 - botao_opcao.width/2, 500) 
botao_sair.set_position(janela.width/2 - botao_sair.width/2, 650)
botao_single.set_position(janela.width/2 - botao_sair.width/2, 350)
botao_mult.set_position(janela.width/2 - botao_sair.width/2, 500)

mouse_livre = True
mouse = janela.get_mouse()
teclado = janela.get_keyboard()

menu_0 = GameImage("menu_0.jpg")
Fundo = GameImage("fundooooo.png")
menu = GameImage("menu.xcf")
menu_pausa = Sprite("pausa.xcf") 
menu_pausa.set_position(janela.width / 2 - menu_pausa.width / 2, janela.height / 2 - menu_pausa.height / 2)

vel_x, vel_y, vel_tiro = 300, 300, 800
branco = (255, 255, 255)
amarelo = (255, 255, 0)
'''
new_fla_D = Sprite("fla_dir.png")
new_fla_E = Sprite("fla_esq.png")
new_wum_D = Sprite("wum_dir.png")
new_wum_E = Sprite("wum_esq.png")
'''
flavia = Sprite("fla.xcf")
flavia.set_position(900, 400)
wumberto = Sprite("wum.xcf")
wumberto.set_position(900, 600)
Soco = Sprite("vazio.png")
sup_direito, sup_direito2 = 1317, 670
sup_esquerdo, sup_esquerdo2 = 29, 573
inf_direito, inf_direito2 = 1332, 526
inf_esquerdo, inf_esquerdo2 = 19, 689
spaws = [sup_direito, sup_esquerdo, inf_direito, inf_esquerdo, sup_direito2, sup_esquerdo2, inf_direito2, inf_esquerdo2]
inimigos = ["ini1.xcf", "ini2.xcf", "ini3.xcf"]
vidas = []
inis_ativos = []
personagens = []
tirosD = []
tirosE = []
timer = 0
vida_ini = 4
total_tela = 5

fla_D, wum_D, vedade = True, True, True
esc_anterior, space_anterior = False, False

frames = 0.0
n_frames = 0
fps = 0
tempo_passado = 0.0 
ultimo_chamado = 0.0
state = "menu"
fase = "primeira"

Soco_Ativo = False
tempo_soco = 0.0
DURACAO_SOCO = 0.15  
LARGURA_SOCO = 15
ALTURA_SOCO = 10  
Soco.width = LARGURA_SOCO
Soco.height = ALTURA_SOCO

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
raio_distância = 60
vel_i = 150
def andar_IA(inimigo):
    if multiplayer:
        dist_f = abs(inimigo.x - flavia.x) + abs(inimigo.y - flavia.y)
        dist_w = abs(inimigo.x - wumberto.x) + abs(inimigo.y - wumberto.y)
        if dist_f < dist_w:
            if inimigo.x <= flavia.x + raio_distância:
                inimigo.x += vel_i*delta_time
            if inimigo.x >= flavia.x - flavia.width - raio_distância:
                inimigo.x -= vel_i*delta_time
            if inimigo.y <= flavia.y + raio_distância:
                inimigo.y += vel_i*delta_time
            if inimigo.y >= flavia.y - flavia.width - raio_distância:
                inimigo.y -= vel_i*delta_time
        else:
            if inimigo.x <= wumberto.x + raio_distância:
                inimigo.x += vel_i*delta_time
            if inimigo.x >= wumberto.x + wumberto.width - raio_distância:
                inimigo.x -= vel_i*delta_time
            if inimigo.y <= wumberto.y + raio_distância:
                inimigo.y += vel_i*delta_time
            if inimigo.y >= wumberto.y + wumberto.width + raio_distância:
                inimigo.y -= vel_i*delta_time
    else:
        if inimigo.x <= flavia.x + raio_distância:
            inimigo.x += vel_i*delta_time
        if inimigo.x >= flavia.x - flavia.width - raio_distância:
            inimigo.x -= vel_i*delta_time
        if inimigo.y <= flavia.y + raio_distância:
            inimigo.y += vel_i*delta_time
        if inimigo.y >= flavia.y - flavia.width - raio_distância:
            inimigo.y -= vel_i*delta_time
def chama_ini():
    num_ra = random.randint(0, 2)
    posi_ra = random.randint(0, 3)
    ini_random = inimigos[num_ra]
    ini_gerado = Sprite(ini_random)
    inis_ativos.append(ini_gerado)
    ini_gerado.set_position(spaws[posi_ra], spaws[posi_ra+4])
def testa_colisao():
    for j in range(len(inis_ativos) - 1, -1, -1):
        inimigo = inis_ativos[j]
        if Soco.collided(inimigo):
            inis_ativos.pop(j)
            vidas.pop(j)

while vedade:   
    delta_time = janela.delta_time()
    esc_atual = teclado.key_pressed("ESC")
    if state == "menu":
        menu_0.draw()        

        botao_jogar.draw()                                                          
        botao_opcao.draw()
        botao_sair.draw()

       
        if mouse.is_over_object(botao_jogar) and mouse.is_button_pressed (1) and mouse_livre:
            state = "modo_de_jogo"
            mouse_livre = False
        if mouse.is_over_object(botao_opcao) and mouse.is_button_pressed (1) and mouse_livre:
            state = "opcao"
            mouse_livre = False
        if mouse.is_over_object(botao_sair) and mouse.is_button_pressed (1) and mouse_livre:
            mouse_livre = False
            break
        
        
    if state == "modo_de_jogo":
        menu_0.draw()

        botao_single.draw()
        botao_mult.draw()

        if mouse.is_over_object(botao_single) and mouse.is_button_pressed (1) and mouse_livre:
            personagens = [flavia]
            multiplayer = False
            mouse_livre = False
            state = "jogando"
        
        if mouse.is_over_object(botao_mult) and mouse.is_button_pressed (1) and mouse_livre:
            personagens = [flavia, wumberto]
            multiplayer = True
            mouse_livre = False
            state = "jogando"
            
    #if state == "pausa":
     #   menu.draw()
      #  if teclado.key_pressed("esc"):
       #     exit()
        #if teclado.key_pressed("Q"):
         #   state = "jogando"
        #if teclado.key_pressed("X"):
         #   personagens = [flavia]
          #  multiplayer = False
        #if teclado.key_pressed("C"):
        #    personagens = [flavia, wumberto]
        #    multiplayer = True
            
    elif state == "jogando":
        Fundo.draw()
        timer += delta_time
        frames += delta_time
        n_frames += 1
        if frames >= 1:
            fps = n_frames/frames
            frames = 0.0
            n_frames = 0
        #==================================================================================
        if flavia in personagens:
            anda_generico(flavia, "W", "S", "A", "D", delta_time)
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
            for j in range(len(inis_ativos) -1 , -1, -1):
                n_amigo = inis_ativos[j]
                if tiro.collided(n_amigo):
                    vidas[j] -= 1
                    if vidas[j] <= 0:
                        inis_ativos.pop(j)
                        vidas.pop(j)
                    tirosD.pop(i)
                    break     
        for i in range(len(tirosE) - 1, -1, -1):
            tiro = tirosE[i]
            tiro.draw()
            tiro.x -= vel_tiro * delta_time
            if tiro.x + tiro.width <= 0:
                tirosE.pop(i) 
            for j in range(len(inis_ativos) -1 , -1, -1):
                n_amigo = inis_ativos[j]
                if tiro.collided(n_amigo):
                    vidas[j] -= 1
                    if vidas[j] <= 0:
                        inis_ativos.pop(j)
                        vidas.pop(j)
                    tirosE.pop(i)
                    break
        #==================================================================================
        #==================================================================================
        if wumberto in personagens:    
            anda_generico(wumberto, "UP", "DOWN", "LEFT", "RIGHT", delta_time)
            if teclado.key_pressed("K"):
                Soco_Ativo = True
                tempo_soco = 0.0
                if wum_D:
                    Soco.set_position(wumberto.x + wumberto.width + 10, wumberto.y + 30)
                else:
                    Soco.set_position(wumberto.x - Soco.width +10, wumberto.y + 30)
        if Soco_Ativo:
            tempo_soco += delta_time
            if tempo_soco >= DURACAO_SOCO:
                Soco_Ativo = False
            else:
                testa_colisao()
        #==================================================================================

        if teclado.key_pressed("D"):
            fla_D = True
        if teclado.key_pressed("A"):
            fla_D = False
        if teclado.key_pressed("RIGHT"):
            wum_D = True
        if teclado.key_pressed("LEFT"):
            wum_D = False

        tempo_passado += delta_time
        q_ativos = len(inis_ativos)
        if q_ativos < total_tela:
            if (tempo_passado - ultimo_chamado) >= 3.0:
                chama_ini()
                ultimo_chamado = tempo_passado
                vidas.append(vida_ini)
        for object in inis_ativos:
            n_sai_da_tela(object)
            object.draw()
            andar_IA(object)
        for personagem in personagens:
            n_sai_da_tela(personagem)
            personagem.draw()   

        if esc_atual and not esc_anterior:
            state = "pausa"
        janela.draw_text(f"FPS: {int(fps)}", 10, 10, size=10, color=(amarelo), bold=True)
            
    elif state == "pausa":
        menu_pausa.draw()
        janela.draw_text("Esc para voltar ao jogo", janela.width / 2 - 100, janela.height / 2 + 150, 20, branco, "Calibri", True)
        janela.draw_text("Espaço para voltar ao menu", janela.width / 2 - 120, janela.height / 2 + 180, 20, branco, "Calibri", True)
        
        if esc_atual and not esc_anterior:
            state = "jogando"

        space_atual = teclado.key_pressed("SPACE")
        if space_atual and not space_anterior:
             state = "menu"
        space_anterior = space_atual
    esc_anterior = esc_atual

    if not mouse.is_button_pressed(1):
        mouse_livre = True
    janela.update()
