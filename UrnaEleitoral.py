candidato = ['Bolsonaro', 'Lula', 'Sarney', 'Tiririca', 'Donald Trump', 'Vladmir Putin']
partido = ['20', '17', '45', '35', '14', '82']
voto = [0, 0, 0, 0, 0, 0]
votacao = open('Votação.txt', 'w')

def votar(candidato, partido):
    for c in range(len(candidato)):
        print(candidato[c], '-', partido[c])


def dec(s, candidato, partido, voto):
    conf = (input('Deseja confirmar seu voto em: ' + candidato[s] + ', do partido com ID: ' + partido[s] + '? (S/N)'))
    if conf == 's' or conf == 'S':
        voto[s] = (voto[s])+1
        print('Voto computado!')
    elif conf == 'n' or conf == 'N':
        print('Voto cancelado!')
        print('Selecione o candidato novamente!')
        selpartido(candidato, partido, voto)
    else:
        print('Comando inválido')
        print('Selecione o candidato!')
        votar(candidato, partido)
        selpartido(candidato, partido, voto)


def selpartido(candidato, partido, voto):
    print('Novo eleitor!')
    v = (input('Digite o ID do partido:'))
    if v in partido:
        if v == partido[0]:
            dec(0, candidato, partido, voto)
        elif v == partido[1]:
            dec(1, candidato, partido, voto)
        elif v == partido[2]:
            dec(2, candidato, partido, voto)
        elif v == partido[3]:
            dec(3, candidato, partido, voto)
        elif v == partido[4]:
            dec(4, candidato, partido, voto)
        elif v == partido[5]:
            dec(5, candidato, partido, voto)
    else:
            print('Comando inválido')
            print('Selecione o candidato!')
            votar(candidato, partido)
            selpartido(candidato, partido, voto)


def empate(candidato, voto, partido):
    candidatostemp = []
    partidostemp = []
    votosord = []
    for k in range(len(voto)):
        votosord.append(voto[k])
    votosord.sort()
    votosord.reverse()
    for r in range(len(votosord)):
        if votosord[0] == voto[r]:
            partidostemp.append(partido[voto.index(votosord[0])])
            candidatostemp.append(candidato[voto.index(votosord[0])])
            voto[voto.index(votosord[0])] = -1
    candidato = candidatostemp[:]
    votacao.write('Os candidatos que empataram foram:\n')
    for z in range(len(candidatostemp)):
        votacao.write('   -')
        votacao.write(str(candidato[z]))
        votacao.write('\n')
    votacao.write('\n\n\n')
    partido = partidostemp[:]
    voto = [0] * (len(candidato))
    vota(candidato, voto, partido)


def vota(candidato, voto, partido):

    maior = -1
    compara = 0
    continua = True
    while continua is True:

        try:
            num = int(input('Digite o número de eleitores que irão votar!'))

            for n in range(num):
                votar(candidato, partido)
                selpartido(candidato, partido, voto)

            print('Processo eleitoral finalizado!')


            for f in range(len(candidato)):
                comp = voto[f]
                if comp > maior:
                    z = f
                    maior = comp
            for prop in range(len(candidato)):
                comp = voto[prop]
                if comp == maior:
                    compara = compara + 1
            if compara > 1:
                print('Houve um empate! A votação irá reiniciar apenas com os candidatos empatados!')
                votacao.write('Houve um empate! A votacao ira reiniciar apenas com os candidatos empatados!')
                votacao.write('\n\n')
                empate(candidato, voto, partido)
            elif compara == 1:
                print('O candidato ganhador é: ', candidato[z], ', com: ', voto[z], ' votos.')
                votacao.write('O candidato ganhador eh: ')
                votacao.write(str(candidato[z]))
                votacao.write(', com: ')
                votacao.write(str(voto[z]))
                votacao.write(' votos.')
                votacao.write('\n\n\n')
                votacao.close()
                break
            continua = False

        except Exception as err:
            print("Apenas números são permitidos, tente novamente!")


vota(candidato, voto, partido)
