from PPlay.sprite import Sprite
from PPlay.window import Window
from PPlay.gameimage import GameImage
import random

Tam_x, Tam_y = 1440, 900
janela = Window(Tam_x, Tam_y)
janela.set_title("Joguito")

botao_jogar= Sprite ("claq_a.xcf")
botao_opcao= Sprite ("claq_a.xcf")
botao_sair= Sprite ("claq_a.xcf")
botao_single= Sprite ("claq_a.xcf")
botao_mult= Sprite ("claq_a.xcf")

HUB_W = Sprite("Hub_W.xcf")
HUB_W.set_position(20, 20)
HUB_F = Sprite("HUB_F.xcf")
HUB_F.set_position(janela.width - HUB_F.width - 20,20)

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

flavia = Sprite("fla.xcf")
flavia.set_position(900, 400)

wumberto = Sprite("assets.wuberto/parado.xcf")
wumberto.set_position(900, 600)

wumberto_animacoes = {
    "parado": Sprite("assets.wuberto/parado.xcf"),
    "cima": Sprite("assets.wuberto/cima.xcf", 5),
    "baixo": Sprite("assets.wuberto/baixo.xcf", 7),
    "esquerda": Sprite("assets.wuberto/esquerda.xcf", 4),
    "direita": Sprite("assets.wuberto/direita.xcf", 4)
}

wumberto_animacoes["cima"].set_total_duration(1000)
wumberto_animacoes["baixo"].set_total_duration(1000)
wumberto_animacoes["esquerda"].set_total_duration(1000)
wumberto_animacoes["direita"].set_total_duration(1000)

for animacao in wumberto_animacoes.values():
    animacao.set_position(900, 600)

animacao_atual = "parado"
wumberto_atual = wumberto_animacoes[animacao_atual]

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

alvos = [(1317, 670), (29, 573), (1332, 526), (19, 689)]
vida_W = 3
vida_F = 3
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

raio_distância = 250
vel_i = 180
raio_separacao = 70

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

def andar_IA(inimigo):
    if multiplayer:
        dist_f = ((inimigo.x - flavia.x)**2 + (inimigo.y - flavia.y)**2)**0.5
        dist_w = ((inimigo.x - wumberto.x)**2 + (inimigo.y - wumberto.y)**2)**0.5
        if dist_f < dist_w:
            alvo_x, alvo_y = flavia.x + flavia.width/2, flavia.y + flavia.height/2
            distancia = dist_f
        else:
            alvo_x, alvo_y = wumberto.x + wumberto.width/2, wumberto.y + wumberto.height/2
            distancia = dist_w
    else:
        alvo_x, alvo_y = flavia.x + flavia.width/2, flavia.y + flavia.height/2
        distancia = ((inimigo.x - flavia.x)**2 + (inimigo.y - flavia.y)**2)**0.5
    
    if distancia <= raio_distância and distancia > 20:
        dir_x = (alvo_x - (inimigo.x + inimigo.width/2)) / distancia
        dir_y = (alvo_y - (inimigo.y + inimigo.height/2)) / distancia
        
        inimigo.x += dir_x * vel_i * delta_time
        inimigo.y += dir_y * vel_i * delta_time
    elif distancia > raio_distância:
        if alvo_x > inimigo.x:
            inimigo.x += vel_i * 0.3 * delta_time
        else:
            inimigo.x -= vel_i * 0.3 * delta_time
            
        if alvo_y > inimigo.y:
            inimigo.y += vel_i * 0.3 * delta_time
        else:
            inimigo.y -= vel_i * 0.3 * delta_time
    
    for outro in inis_ativos:
        if outro != inimigo:
            centro_x1 = inimigo.x + inimigo.width/2
            centro_y1 = inimigo.y + inimigo.height/2
            centro_x2 = outro.x + outro.width/2
            centro_y2 = outro.y + outro.height/2
            
            dist_x = centro_x1 - centro_x2
            dist_y = centro_y1 - centro_y2
            dist_entre = (dist_x**2 + dist_y**2)**0.5
            
            min_dist = (inimigo.width + outro.width)/2 + 10
            
            if dist_entre < min_dist and dist_entre > 0:
                push_force = (min_dist - dist_entre) / min_dist
                inimigo.x += (dist_x / dist_entre) * push_force * 50 * delta_time
                inimigo.y += (dist_y / dist_entre) * push_force * 50 * delta_time
            
            #if outro.collided(wumberto) or outro.collided(flavia):
                #random em alvos e o inimigo vai pra lá
    
    if inimigo.x < 0:
        inimigo.x = 0
    if inimigo.x > janela.width - inimigo.width:
        inimigo.x = janela.width - inimigo.width
    limite_superior = janela.height * frac_dis_max - inimigo.height
    if inimigo.y < limite_superior:
        inimigo.y = limite_superior
    if inimigo.y > janela.height - inimigo.height:
        inimigo.y = janela.height - inimigo.height

def chama_ini():
    num_ra = random.randint(0, 2)
    posi_ra = random.randint(0, 3)
    
    ini_random = inimigos[num_ra]
    ini_gerado = Sprite(ini_random)
    
    x_pos = spaws[posi_ra]
    y_pos = spaws[posi_ra+4]
    
    x_pos = max(0, min(x_pos, janela.width - ini_gerado.width))
    y_pos = max(janela.height * frac_dis_max - ini_gerado.height, 
                min(y_pos, janela.height - ini_gerado.height))
    
    ini_gerado.set_position(x_pos, y_pos)
    inis_ativos.append(ini_gerado)
    vidas.append(vida_ini)

def testa_colisao():
    for j in range(len(inis_ativos) - 1, -1, -1):
        inimigo = inis_ativos[j]
        if Soco.collided(inimigo):
            inis_ativos.pop(j)
            vidas.pop(j)

def letras_no_menu_pausa():
    janela.draw_text("JOGAR", janela.width/2 - botao_opcao.width/2+ 20, 450, 20, branco, "Calibri", True)
    janela.draw_text("OPÇÕES", janela.width/2 - botao_opcao.width/2+ 20, 600, 20, branco, "Calibri", True)
    janela.draw_text("SAIR", janela.width/2 - botao_opcao.width/2+ 20, 750, 20, branco, "Calibri", True)

def letras_no_menu_players():
    janela.draw_text("SINGLE", janela.width/2 - botao_opcao.width/2 + 20, 450, 20, branco, "Calibri", True)
    janela.draw_text("MULTPLAYER", janela.width/2 - botao_opcao.width/2 + 20, 600, 15, branco, "Calibri", True)

def atualizar_animacao_wumberto():
    global animacao_atual, wumberto_atual, wum_D
    
    nova_animacao = "parado"
    
    if teclado.key_pressed("UP"):
        nova_animacao = "cima"
    elif teclado.key_pressed("DOWN"):
        nova_animacao = "baixo"
    elif teclado.key_pressed("LEFT"):
        nova_animacao = "esquerda"
        wum_D = False
    elif teclado.key_pressed("RIGHT"):
        nova_animacao = "direita"
        wum_D = True
    
    if nova_animacao != animacao_atual:
        animacao_atual = nova_animacao
        wumberto_atual = wumberto_animacoes[animacao_atual]
    
    if animacao_atual != "parado":
        wumberto_atual.update()
    
    wumberto_atual.set_position(wumberto.x, wumberto.y)

while vedade:   
    delta_time = janela.delta_time()
    esc_atual = teclado.key_pressed("ESC")
    
    if state == "menu":
        menu_0.draw()        
        botao_jogar.draw()                                                          
        botao_opcao.draw()
        botao_sair.draw()
        letras_no_menu_pausa()
       
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
        letras_no_menu_players()
        
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
            
    elif state == "jogando":
        Fundo.draw()
        timer += delta_time
        frames += delta_time
        n_frames += 1
        
        if frames >= 1:
            fps = n_frames/frames
            frames = 0.0
            n_frames = 0
        
        if flavia in personagens:
            anda_generico(flavia, "W", "S", "A", "D", delta_time)
            janela.draw_text(str(vida_F), janela.width*88/100, 20, 50, (255, 0, 0), "Calibri", True)
            HUB_F.draw()
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
                continue
                
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
                continue
                
            for j in range(len(inis_ativos) -1 , -1, -1):
                n_amigo = inis_ativos[j]
                if tiro.collided(n_amigo):
                    vidas[j] -= 1
                    if vidas[j] <= 0:
                        inis_ativos.pop(j)
                        vidas.pop(j)
                    tirosE.pop(i)
                    break
        
        if wumberto in personagens:    
            anda_generico(wumberto, "UP", "DOWN", "LEFT", "RIGHT", delta_time)
            atualizar_animacao_wumberto()
            janela.draw_text(str(vida_W), janela.width*12/100, 20, 50, (255, 0, 0), "Calibri", True)
            HUB_W.draw()
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
        
        for object in inis_ativos:
            n_sai_da_tela(object)
            object.draw()
            andar_IA(object)
            if wumberto.collided(object):
                vida_W -= 1
            if flavia.collided(object):
                vida_F -= 1
            
        
        for personagem in personagens:
            n_sai_da_tela(personagem)
            if personagem == wumberto:
                wumberto_atual.draw()
            else:
                personagem.draw()

        if esc_atual and not esc_anterior:
            state = "pausa"
        
        janela.draw_text(f"FPS: {int(fps)}", 10, 10, size=10, color=amarelo, bold=True)
            
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

print("Jogo encerrado")