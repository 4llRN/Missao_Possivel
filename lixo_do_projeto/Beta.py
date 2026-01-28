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
botao_mult.set_position(janela.width/2 - botao_sair.width/2 + 400, 650)

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
vermelho = (255, 0, 0)
verde = (0, 255, 0)

flavia = Sprite("fla.xcf")
flavia.set_position(900, 400)

cap_1_animacoes = {
    "anda_esquerda_1": Sprite("cap1_anim/andando_cap1 (esq).xcf", 8),
    "anda_direita_1": Sprite("cap1_anim/andando_cap1.xcf", 8),
    "toma_esquerda_1": Sprite("cap1_anim/dano_cap1 (esq).xcf", 6),
    "toma_direita_1": Sprite("cap1_anim/dano_cap1.xcf", 6),
    #"parado_esquerda": Sprite("wumb_anim/idle_w (esq).xcf", 8),
    #"parado_direita": Sprite("wumb_anim/idle_w.xcf", 8),
    "da_soco_esquerda_1": Sprite("cap1_anim/soco_cap1 (esq).xcf", 8),
    "da_soco_direita_1": Sprite("cap1_anim/soco_cap1.xcf", 8)
}

cap_1_animacoes["anda_esquerda_1"].set_total_duration(1000)
cap_1_animacoes["anda_direita_1"].set_total_duration(1000)
cap_1_animacoes["toma_esquerda_1"].set_total_duration(1000)
cap_1_animacoes["toma_direita_1"].set_total_duration(1000)
cap_1_animacoes["da_soco_esquerda_1"].set_total_duration(1000)
cap_1_animacoes["da_soco_direita_1"].set_total_duration(1000)

wumberto_animacoes = {
    "anda_esquerda": Sprite("wumb_anim/andando_w (esq).xcf", 8),
    "anda_direita": Sprite("wumb_anim/andando_w.xcf", 8),
    "toma_esquerda": Sprite("wumb_anim/dano_w (esq).xcf", 6),
    "toma_direita": Sprite("wumb_anim/dano_w.xcf", 6),
    "parado_esquerda": Sprite("wumb_anim/idle_w (esq).xcf", 8),
    "parado_direita": Sprite("wumb_anim/idle_w.xcf", 8),
    "da_soco_esquerda": Sprite("wumb_anim/soco_novo(esq).xcf", 8),
    "da_soco_direita": Sprite("wumb_anim/soco_novo.xcf", 8),
    "da_tiro_esquerda": Sprite("wumb_anim/tiro_w (esq).xcf", 4),
    "da_tiro_direita": Sprite("wumb_anim/tiro_w.xcf", 4)
}

wumberto_animacoes["parado_esquerda"].set_total_duration(1000)
wumberto_animacoes["parado_direita"].set_total_duration(1000)
wumberto_animacoes["toma_esquerda"].set_total_duration(1000)
wumberto_animacoes["toma_direita"].set_total_duration(1000)
wumberto_animacoes["anda_esquerda"].set_total_duration(1000)
wumberto_animacoes["anda_direita"].set_total_duration(1000)
wumberto_animacoes["da_soco_esquerda"].set_total_duration(1000)
wumberto_animacoes["da_soco_direita"].set_total_duration(1000)
wumberto_animacoes["da_tiro_esquerda"].set_total_duration(500)
wumberto_animacoes["da_tiro_direita"].set_total_duration(500)

for animacao in wumberto_animacoes.values():
    animacao.set_position(900, 600)

animacao_atual = "parado_direita"
wumberto_atual = wumberto_animacoes[animacao_atual]

# SISTEMA DE DANO E INVENCIBILIDADE
invencivel_flavia = False
invencivel_wumberto = False
timer_invencibilidade_flavia = 0.0
timer_invencibilidade_wumberto = 0.0
duracao_invencibilidade = 2.0
pisca_timer_flavia = 0.0
pisca_timer_wumberto = 0.0
pisca_intervalo = 0.15
vida_W = 3
vida_F = 3

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
Frangos = []
timer = 0
timerW = 0
vida_ini = 2
total_tela = 5

alvos = [(1317, 670), (29, 573), (1332, 526), (19, 689)]
fla_D, wum_D, vedade = True, True, True
esc_anterior, space_anterior = False, False
multiplayer = False

frames = 0.0
n_frames = 0
fps = 0
tempo_passado = 0.0 
ultimo_chamado = 0.0
state = "menu"
fase = "primeira"

Soco_Ativo = False
dando_tiro_w = False
passou_por_op = False
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

wumberto = wumberto_atual

def reset():
    global state, vida_F, vida_W, invencivel_flavia, invencivel_wumberto, personagens, Frangos
    state = "menu"
    # Reseta tudo
    vida_F = 3
    vida_W = 3
    invencivel_flavia = False
    invencivel_wumberto = False
    personagens = []
    inis_ativos.clear()
    vidas.clear()
    Frangos.clear()
    janela.set_background_color((0,0,0))

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

def da_tiro_D(person):
    tiroD = Sprite("bala.png")
    tiroD.set_position(person.x + person.width*6/10, person.y + 77) 
    tirosD.append(tiroD)

def da_tiro_E(person):
    tiroE = Sprite("bala_reverse.png")
    tiroE.set_position(person.x + person.width*2/10, person.y + 77) 
    tirosE.append(tiroE)

def tomar_dano_flavia():
    global vida_F, invencivel_flavia, timer_invencibilidade_flavia, state
    
    if invencivel_flavia:
        return
    
    vida_F -= 1
    
    if vida_F <= 0:
        if multiplayer and vida_W > 0:
            personagens.remove(flavia)
        else:
            state = "game_over"
        return
    
    invencivel_flavia = True
    timer_invencibilidade_flavia = 0.0

def tomar_dano_wumberto():
    global vida_W, invencivel_wumberto, timer_invencibilidade_wumberto, state
    
    if invencivel_wumberto:
        return
    
    vida_W -= 1
    
    if vida_W <= 0:
        if multiplayer and vida_F > 0:
            personagens.remove(wumberto)
        else:
            state = "game_over"
        return
    
    invencivel_wumberto = True
    timer_invencibilidade_wumberto = 0.0

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

def chama_frango(x, y):
    frango = Sprite("Icon-Floor_Chicken (1).xcf")
    frango.set_position(x, y+100)
    Frangos.append(frango)

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

def atualizar_animacao_wumberto():
    global animacao_atual, wumberto_atual, wum_D
    
    if wum_D:
        nova_animacao = "parado_direita"
    else:
        nova_animacao = "parado_esquerda"

    if teclado.key_pressed("LEFT"):
        nova_animacao = "anda_esquerda"
        wum_D = False
    elif teclado.key_pressed("RIGHT"):
        nova_animacao = "anda_direita"
        wum_D = True
    
    if Soco_Ativo and wum_D:
        nova_animacao = "da_soco_direita"
    elif Soco_Ativo and not wum_D:
        nova_animacao = "da_soco_esquerda"

    if dando_tiro_w and wum_D:
        nova_animacao = "da_tiro_direita"
    elif dando_tiro_w and not wum_D:
        nova_animacao = "da_tiro_esquerda"

    if nova_animacao != animacao_atual:
        animacao_atual = nova_animacao
        wumberto_atual = wumberto_animacoes[animacao_atual]
    
    if animacao_atual != "parado":
        wumberto_atual.update()
    
    wumberto_atual.set_position(wumberto.x, wumberto.y)

def sorteia():
    return random.randint(1, 5) == 1

def mostrar_game_over():
    janela.draw_text("GAME OVER", janela.width/2 - 150, janela.height/2 - 50, 60, vermelho, "Calibri", True)
    janela.draw_text("Pressione ESPAÇO para voltar ao menu", janela.width/2 - 200, janela.height/2 + 50, 30, branco, "Calibri", True)

while vedade:   
    delta_time = janela.delta_time()
    esc_atual = teclado.key_pressed("ESC")
    
    if invencivel_flavia:
        timer_invencibilidade_flavia += delta_time
        pisca_timer_flavia += delta_time
        
        if timer_invencibilidade_flavia >= duracao_invencibilidade:
            invencivel_flavia = False
            pisca_timer_flavia = 0.0
        
        if pisca_timer_flavia >= pisca_intervalo:
            pisca_timer_flavia = 0.0
            flavia.visivel = not flavia.visivel
    else:
        flavia.visivel = True
    
    if invencivel_wumberto:
        timer_invencibilidade_wumberto += delta_time
        pisca_timer_wumberto += delta_time
        
        if timer_invencibilidade_wumberto >= duracao_invencibilidade:
            invencivel_wumberto = False
            pisca_timer_wumberto = 0.0
        
        if pisca_timer_wumberto >= pisca_intervalo:
            pisca_timer_wumberto = 0.0
            wumberto.visivel = not wumberto.visivel
            wumberto_atual.visivel = wumberto.visivel
    else:
        wumberto.visivel = True
        wumberto_atual.visivel = True
    
    if state == "menu":
        reset()
        menu_0.draw()        
        botao_jogar.draw()                                                          
        botao_opcao.draw()
        botao_sair.draw()
        letras_no_menu_pausa()
       
        if mouse.is_over_object(botao_jogar) and mouse.is_button_pressed (1) and mouse_livre:
            state = "jogando"
            mouse_livre = False
        if mouse.is_over_object(botao_opcao) and mouse.is_button_pressed (1) and mouse_livre:
            state = "opcao"
            mouse_livre = False
        if mouse.is_over_object(botao_sair) and mouse.is_button_pressed (1) and mouse_livre:
            mouse_livre = False
            break
        
    if state == "opcao":
        menu_0.draw()
        botao_mult.draw()
        passou_por_op = True
        if mouse.is_over_object(botao_mult) and mouse.is_button_pressed (1) and mouse_livre:
            personagens = [flavia, wumberto]
            multiplayer = True
            mouse_livre = False
            state = "jogando"
            vida_F = 3
            vida_W = 1000
            
    elif state == "jogando":
        if not passou_por_op:
            personagens = [wumberto]
        mouse_livre = False
        if multiplayer:
            vida_W = 1000
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
            HUB_F.draw()
            if teclado.key_pressed("space"):
                if timer >= 0.5:
                    timer = 0
                    if fla_D:
                        da_tiro_D(flavia)
                    else:
                        da_tiro_E(flavia)
        
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
                        inimigo_morto = inis_ativos[j]
                        if sorteia():
                            chama_frango(inimigo_morto.x, inimigo_morto.y)
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
                        inimigo_morto = inis_ativos[j]
                        if sorteia():
                            chama_frango(inimigo_morto.x, inimigo_morto.y)
                        inis_ativos.pop(j)
                        vidas.pop(j)
                    tirosE.pop(i)
                    break
        
        if wumberto in personagens: 
            timerW += delta_time   
            anda_generico(wumberto, "UP", "DOWN", "LEFT", "RIGHT", delta_time)
            atualizar_animacao_wumberto()
            HUB_W.draw()
            if teclado.key_pressed("K"):
                Soco_Ativo = True
                tempo_soco = 0.0
                if wum_D:
                    Soco.set_position(wumberto.x + wumberto.width + 10, wumberto.y + 30)
                else:
                    Soco.set_position(wumberto.x - Soco.width +10, wumberto.y + 30)
            if teclado.key_pressed("L"):
                dando_tiro_w = True
                if timerW >= 0.5:
                    timerW = 0
                    if wum_D:
                        da_tiro_D(wumberto)
                    else:
                        da_tiro_E(wumberto)
            else:
                dando_tiro_w = False
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
        
        for inimigo in inis_ativos:
            inimigo.draw()
            andar_IA(inimigo)
            n_sai_da_tela(inimigo)
            
            if flavia in personagens and inimigo.collided(flavia) and not invencivel_flavia:
                tomar_dano_flavia()
                if inimigo.x > flavia.x:
                    flavia.x -= 50
                else:
                    flavia.x += 50
            
            if wumberto in personagens and inimigo.collided(wumberto) and not invencivel_wumberto:
                tomar_dano_wumberto()
                if inimigo.x > wumberto.x:
                    wumberto.x -= 50
                else:
                    wumberto.x += 50
        
        # CORREÇÃO: Remover frangos usando índice numérico
        frangos_a_remover = []
        for idx, frango in enumerate(Frangos):
            frango.draw()
            
            # Verifica colisão com Flavia
            if flavia in personagens and frango.collided(flavia):
                vida_F = min(vida_F + 1, 3)  # Cura 1 vida, máximo 3
                frangos_a_remover.append(idx)
            
            # Verifica colisão com Wumberto
            elif wumberto in personagens and frango.collided(wumberto):
                vida_W = min(vida_W + 1, 3)  # Cura 1 vida, máximo 3
                frangos_a_remover.append(idx)
        
        # Remove frangos coletados (do último para o primeiro)
        for idx in sorted(frangos_a_remover, reverse=True):
            if idx < len(Frangos):
                Frangos.pop(idx)
        
        for personagem in personagens:
            n_sai_da_tela(personagem)
            if personagem == wumberto and wumberto.visivel:
                wumberto_atual.draw()
            elif personagem == flavia and flavia.visivel:
                personagem.draw()

        if flavia in personagens:
            cor_vida = vermelho if invencivel_flavia else branco
            janela.draw_text(f"♥ {vida_F}", janela.width - HUB_F.width - 100, 50, 50, cor_vida, "Calibri", True)
        
        if wumberto in personagens:
            cor_vida = vermelho if invencivel_wumberto else branco
            janela.draw_text(f"{vida_W} ♥", 130, 50, 50, cor_vida, "Calibri", True)
        
        if invencivel_flavia:
            tempo_restante = duracao_invencibilidade - timer_invencibilidade_flavia
            janela.draw_text(f"INV: {tempo_restante:.2f}s", janela.width - 130, 100, 20, amarelo, "Calibri", True)
        
        if invencivel_wumberto:
            tempo_restante = duracao_invencibilidade - timer_invencibilidade_wumberto
            janela.draw_text(f"INV: {tempo_restante:.2f}s", 130, 100, 20, amarelo, "Calibri", True)

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
    
    elif state == "game_over":
        Fundo.draw()
        mostrar_game_over()
        
        if teclado.key_pressed("SPACE"):
            reset()
    
    esc_anterior = esc_atual

    if not mouse.is_button_pressed(1):
        mouse_livre = True
    
    janela.update()

print("Jogo encerrado")