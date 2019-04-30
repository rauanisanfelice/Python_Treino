import random
import os

def jogar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*--------------------------------*")
    print("*-------- JOGO DE FORCA ---------*")
    print("*--------------------------------*")

    vida = 6

    ## ADICIONA NIVEL
    print("Qual nível de dificuldade?")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")

    nivel = int(input("Defina o nível: "))
    print("")
    print("")

    list_completa = importar_palavras(nivel)
    palavra = random.choice(list_completa)
    tamanho = len(palavra)
    letras_digitadas = []
    acertos = 0
    
    desc_pala = ""
    for x in range(0,tamanho):
        desc_pala = desc_pala + "__ "
    desc_pala = desc_pala.strip()

    os.system('cls' if os.name == 'nt' else 'clear')
    while vida > 0:
        print("A palvra possui", tamanho, " caracteres!")
        print("Letras digitadas: ", letras_digitadas)
        print("Voce possui somente", vida, "vidas!!!")
        print("")
        print(desc_pala)

        print("")
        print("")
        letra = input("Digite uma letra: ")

        # VERIFICA SE JÁ FOI DIGITADA A LETRA
        if (letra.upper() in letras_digitadas):
            print("Letra ja foi digitada!!")
        elif (letra in palavra):
            c = palavra.find(letra) + 1
            for x in range(1,tamanho + 1):
                if (x == c):
                    lista = desc_pala.split(" ")
                    lista[x - 1] = str(letra).upper()
                    desc_pala = " ".join(lista)
                    acertos = acertos + 1
                    c = palavra.find(letra, c) + 1
                    if (c == -1):
                        break
                else:
                    pass

            letras_digitadas.append(letra.upper())
            
            if (acertos == tamanho):
                print ("Parabéns você acertou!!")
                resp = input("Deseja jogar novamente ? (S/N)").upper()
                if (resp == "S"):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    jogar()
                else:
                    break
        else:
            print("Não possui esta letra na palavra!")
            letras_digitadas.append(letra.upper())
            vida = vida - 1
        os.system('cls' if os.name == 'nt' else 'clear')

    
    print ("Acabou suas vidas!!")
    print("A palavra era: ", palavra)
    resp = input("Deseja jogar novamente ? (S/N)").upper()
    if (resp == "S"):
        os.system('cls' if os.name == 'nt' else 'clear')
        jogar()
    else:
        pass


def importar_palavras(nivel):

    if (nivel == 1 ):
        list_04 = ['fato','agir','algo','alta','alto','alva','alvo','amar','amor','ante','apto','asco','ater','auge','auto','base','belo','bens','bojo','bolo','brio','caos','casa','cedo','cela','como','cota','coxo','crer','cujo','deus','doce','ente','ermo','esmo','face','fase','frio','gama','gana','gozo','grau','guia','haja','halo','hera','hoje','idem','jaez','jeca','jipe','jogo','joia','joio','jugo','juiz','juro','kart','kilo','kiwi','lida','logo','lume','luta','mais','medo','meio','mero','mito','mote','nada','nato','nexo','nojo','nome','novo','numa','onde','opor','orla','para','pois','pose','prol','pude','puta','qual','quem','quer','quis','quiz','rege','rima','rito','rude','ruim','saga','sede','seio','sela','sina','soar','suma','teor','tese','teve','todo','tolo','traz','tudo','unir','urbe','urge','usar','vale','veio','vida','vide','voga','xale','xepa','xero','xeta','xexo','xila','xilo','xixi','xota','xote','xuxo','yagi','yang','zebu','zelo','zero','zoar','zona','zoom','zulu']
        list_05 = ['afago','afeto','algoz','anexo','ardil','assaz','assim','atroz','audaz','banal','bando','beata','bicho','birra','botar','brado','bravo','brega','breve','brisa','bruma','burro','causa','ceder','censo','cerne','clava','comum','corja','coser','cozer','crivo','culto','denso','desde','dever','digno','dizer','expor','falar','falso','falta','fardo','farsa','fator','favor','fazer','feixe','feliz','fluir','fluxo','forma','forte','fosse','fugaz','furor','garbo','genro','gente','geral','gerar','gerir','gesto','gleba','glosa','gozar','grato','grave','grota','grupo','guisa','haste','haver','havia','hiato','homem','honra','horda','hoste','houve','ideia','impor','inato','jaula','jazer','jazia','jegue','jeito','jejum','jirau','jogar','jovem','judeu','junco','junta','junto','jurar','justa','justo','kalio','kebab','krill','kyrie','labor','laico','lapso','lavra','lazer','leigo','leite','leito','levar','liame','limbo','louco','lugar','manso','matiz','mesmo','mexer','moral','muito','mundo','narco','navio','negro','nesse','nicho','nobre','noite','norma','nossa','nunca','obter','olhar','ontem','ordem','orgia','outro','ouvir','pesar','plena','pleno','poder','porra','posse','prole','quais','quase','queda','queto','quilo','quite','quota','regra','saber','sagaz','sanar','seara','senso','seria','sutil','tange','tecer','temer','temor','tempo','tenaz','tende','tenro','termo','terno','toada','tomar','torpe','ufano','ultra','ungir','untar','urdir','urgia','urgir','urubu','usual','usura','valha','valia','valor','vasto','velar','vendo','vigor','vimos','viril','visar','vital','vivaz','viver','vulto','weber','xampu','xaxim','xelim','xeque','xerez','xerox','xibio','xibiu','xiita','xingo','xisto','xotar','xucro','zagal','zaino','zanga','zebra','zelar','zerar','zesto','zimbo','zinco','zinho','zoada','zonzo','zorra','zumbi','zunir','zurro']
        list_06 = ['abster','acento','adorno','aferir','alento','alheio','alocar','aludir','anseio','apogeu','asseio','astuto','avidez','baiuca','baleia','beleza','biltre','bocado','boceta','boemia','bonito','bradar','branda','brando','brasil','brecha','burlar','buscar','casual','ciente','coagir','decoro','desejo','difuso','dispor','eficaz','embora','ensejo','escopo','escusa','esteio','exceto','eximir','faceta','flanco','forjar','formal','formos','franco','fraude','frisar','frugal','fulgor','gaiato','galera','galgar','ganhar','geleia','gentil','gitano','glosar','goiaba','gostar','gozado','grafar','grande','grosso','guarda','guerra','guilda','herege','horror','hostil','humano','idiota','infame','isento','jabuti','jactar','jamais','janela','janota','jardim','jazida','jazigo','jiboia','jocoso','joelho','jornal','jorrar','jovial','julgar','juntar','kaiser','kelvin','kibutz','kirsch','kitsch','klaxon','kummel','labuta','lacuna','ladino','larica','lastro','lavrar','legado','lesado','limiar','limite','linear','lisura','lograr','loquaz','lotado','manter','maroto','matriz','mazela','melhor','mister','motriz','nascer','nativo','neutro','nocivo','normal','noutro','nuance','objeto','obstar','obtuso','ocioso','ofensa','omisso','omitir','onerar','oposto','origem','ousado','outrem','perene','pressa','prover','quadra','quadro','quando','quanto','quarto','quebra','quedar','queijo','queira','queixa','queixo','quenga','quente','querer','quiabo','quieto','quiser','quisto','quitar','quorum','rancor','receio','remoto','rotina','sisudo','solene','talvez','teoria','tirano','tolher','tornar','torpor','tratar','trazer','trevas','triste','trouxa','trouxe','ufanar','umbral','ungido','urbano','urdido','utente','utopia','vedado','venham','vereda','vermos','vetado','viagem','vieram','voltar','vulgar','walter','xadrez','xarada','xarope','xaveco','xaxado','xeique','xereca','xereta','xerife','xilema','xingar','xinxim','xixixi','xoxota','yakuza','yogurt','yuppie','zagaia','zangar','zanzar','zapear','zarpar','zeloso','zelote','zerado','zeugma','zigoto','zimbro','zoeira','zombar','zombou','zumbir','zunido','zureta','zurrar','zurzir']
        list_07 = ['embuste','quimera','abrange','abrupto','ademais','alcunha','alegria','almejar','ansioso','arcaico','aspecto','assento','atenuar','auferir','austero','balizar','basilar','beldade','benesse','benigno','bizarro','bondade','bondoso','bravata','burrice','butique','candura','cinismo','cogitar','colosso','conciso','conduta','contudo','coragem','cordial','deboche','deferir','definir','deleite','demanda','demasia','destoar','devasso','deveras','diferir','dirimir','emergir','emotivo','empatia','escasso','estirpe','excerto','excesso','exilado','exortar','falange','fidalgo','fizesse','flagelo','fomento','formoso','furtivo','galante','galhofa','garboso','garrida','genioso','genitor','gorjear','gostoso','gracejo','gradual','guardar','guarida','habitar','herdade','heresia','heroico','hesitar','higidez','higiene','honesto','honrado','humilde','imputar','incauto','incitar','indagar','inferir','intenso','intriga','intuito','jacente','jeitoso','jerimum','jornada','jubilar','jubileu','jugular','julgado','jurista','jusante','justeza','juvenil','ketchup','kichute','kilobit','laicato','lamento','lapidar','lascivo','latente','lavrado','legenda','lembrar','leviano','lisonja','literal','litigar','lucidez','luzindo','mancebo','mandato','matilha','mitigar','modesto','moleque','momento','mostrar','naquela','naquele','natural','nazismo','nefasto','nenhuma','ninfeta','nitidez','nobreza','nojento','nominal','nortear','novilho','obsceno','obscuro','ocorrer','ofuscar','ojeriza','olvidar','oneroso','ordenar','orgulho','oriundo','oscilar','ousadia','outrora','padecer','parcial','preciso','profano','prolixo','quantas','quantia','quantum','quartel','quebrar','queixar','querela','querida','querido','quesito','quisera','quitute','receoso','recesso','redimir','refutar','regular','remeter','revogar','salutar','secular','sensato','sentido','sincero','singelo','soberba','soberbo','soturno','sublime','sucesso','sucinto','talento','ternura','tinhoso','todavia','torpeza','triagem','trivial','ultraje','umidade','unidade','unissex','untuoso','urgente','usurpar','vaidade','varonil','vassalo','venerar','ventura','verbete','verdade','vigente','virtude','vontade','vultoso','walkman','warrant','western','xavante','xavecar','xeretar','xerocar','xexeiro','xibungo','xifoide','ximbica','xistoso','zabumba','zangado','zarolho','zelador','zepelim','zinabre','zoonose','zumbido','zurrapa']
        list_08 = ['yakisoba','abnegado','abstrair','abstrato','alegoria','alicerce','alienado','analisar','analogia','anomalia','apetecer','apologia','ardiloso','arrojado','ascender','ativismo','ativista','baluarte','banzeiro','barganha','bastante','bastardo','belicoso','bochecha','brandura','coadunar','complexo','conceder','conceito','concerne','concerto','conhecer','conserto','consiste','contenda','contexto','deferido','deleitar','demagogo','denegrir','desfecho','designar','despeito','despojar','desprezo','destarte','destreza','devaneio','difundir','discreto','disperso','dissipar','distinto','elucidar','eminente','enxergar','equidade','escrever','espectro','excitado','exonerar','expedido','extravio','fabuloso','faccioso','fascismo','fomentar','fornicar','fortuito','fulguras','fustigar','garantir','garatuja','generoso','genitora','gentalha','germinar','girassol','gracioso','grandeza','granjear','gratuito','grotesco','habitual','harmonia','hediondo','hodierno','homicida','horrendo','humilhar','imanente','iminente','importar','impugnar','incisivo','inerente','inspirar','instigar','invasivo','jenipapo','joaninha','jubilado','jubiloso','judicial','justapor','kafkiano','kamikaze','kantiano','kantismo','kantista','kartismo','kartista','lactante','lavrador','lealdade','lenitivo','letargia','lusitano','maestria','mediante','melindre','meretriz','moderado','molestar','mormente','natureza','neonatal','niilismo','novidade','obcecado','obedecer','objetivo','observar','obsoleto','obstante','obstruir','oferecer','onanismo','oportuno','opressor','opulento','orientar','original','ortodoxo','ostentas','otimizar','outorgar','paradoxo','paralelo','peculiar','perplexo','perverso','pleitear','ponderar','portanto','preceder','preceito','premissa','prendado','presteza','primazia','problema','proceder','processo','promover','prosaico','prudente','qualquer','quatorze','quebrado','queimada','queixume','querigma','quietude','quilombo','quinzena','quisesse','quitanda','racional','rapariga','realizar','refletir','reiterar','relativo','remediar','reportar','repudiar','requerer','resignar','resoluto','respaldo','respeito','ressalva','restrito','revogado','saliente','sanidade','segmento','sensatez','singular','soberano','subjugar','submeter','submisso','sucumbir','suprimir','surpresa','suscitar','sutileza','titubear','trabalho','traduzir','transpor','tristeza','ufanismo','ufanista','ulterior','ultimato','ultrajar','ululante','unguento','unificar','uniforme','universo','urdidura','usufruir','usufruto','usurpado','utilizar','vantagem','veemente','veredito','vertente','vigoroso','virtuoso','visceral','volitivo','wildiano','workshop','wurtzita','xaroposo','xilofone','xofrango','zagueiro','zaragata','zigurate','zombador','zombaria','zoofagia','zoofilia','zoologia','zoomorfo']
        list_completa = list_04 + list_05 + list_06 + list_07 + list_08

    if (nivel == 2):
        list_09 = ['kafkaesco','xenofobia','adjacente','admoestar','ambicioso','arraigado','bajulador','balbuciar','beatitude','benquisto','bilateral','brevidade','brilhante','companhia','consoante','constante','convergir','deliberar','demasiado','descrever','desdenhar','desumilde','deturpado','dicotomia','diferente','diligente','dinamismo','discorrer','dissuadir','efeminado','eloquente','emergente','empecilho','enfadonho','entediado','essencial','estagnado','exacerbar','excedente','excelente','extasiado','facultado','falcatrua','fidedigno','filosofia','flagrante','florescer','fragmento','galhardia','gentileza','gradativo','grosseria','habilitar','hedonismo','hegemonia','hesitante','homenagem','homofobia','homologar','horizonte','humildade','imparcial','impetuoso','imponente','incidente','indolente','insensato','insolente','interesse','inusitado','judicante','judicioso','juventude','kieserita','krausismo','liberdade','ludibriar','magnitude','manancial','mecanismo','mesquinho','ministrar','minucioso','moribundo','narrativa','nepotismo','normativo','norteador','nosologia','nostalgia','notificar','obliterar','obstinado','obtivemos','ontologia','orgulhoso','ostensivo','outorgado','outrossim','paradigma','perspicaz','persuadir','plenitude','precursor','probidade','quadrante','quadrilha','quaisquer','qualidade','quebranto','querelado','quociente','ratificar','rebuscado','redarguir','referente','regozijar','relevante','relutante','renunciar','requisito','rescindir','resignado','ressaltar','restituir','retificar','salientar','sancionar','seriedade','subjetivo','subjugado','subsistir','suplantar','taciturno','tipificar','tranquilo','translado','tratativa','ultrajado','ultrassom','umedecido','unicidade','unificado','universal','usurpador','utilidade','utilizado','vagabunda','vagabundo','verificar','vinculado','wagnerita','warrantar','weberiano','windsurfe','wulfenita','xamanismo','xenelasia','xenofilia','xenologia','xexelento','zafimeiro','zaragatoa','zeladoria','ziquizira','zoomorfia','zootecnia']
        list_10 = ['atribulado','auspicioso','banalidade','brasileiro','burocracia','coercitivo','compassivo','concessivo','conjuntura','consolidar','constituir','contemplar','conturbado','corroborar','democracia','depreender','desprovido','desvanecer','detrimento','disciplina','disruptivo','disseminar','distinguir','divergente','entretanto','equivocado','estupefato','exacerbado','excludente','extremista','famigerado','fascinante','fatalidade','felicidade','fidelidade','filantropo','finalidade','fisionomia','forasteiro','fundamento','genealogia','habilidade','harmonioso','heterodoxo','hierarquia','hipocrisia','holocausto','hombridade','hostilizar','humanidade','importante','incipiente','indulgente','iniquidade','jornaleiro','julgamento','juntamente','justamente','justaposto','justificar','kaiserismo','kaiserista','kardecismo','kardecista','kepleriano','keynesiano','kimberlito','kneippismo','kneippista','lancinante','leviandade','libidinoso','lisonjeado','locupletar','logradouro','ludibriado','martirizar','maturidade','melancolia','melindrosa','melindroso','mentecapto','mesquinhez','meticuloso','mobilidade','modalidade','morosidade','mutuamente','necessitar','necrofilia','nefelibata','negligente','neologismo','nosocomial','nosografia','obliterado','ociosidade','oligarquia','ostracismo','pejorativo','permanente','pernicioso','pertinente','precedente','preconizar','preliminar','prepotente','prescindir','primordial','qualificar','quantidade','quebrantar','querelante','questionar','quiescente','quilograma','quilombola','quinhentos','quixotesco','quotidiano','redundante','relacionar','repreender','requerente','respectivo','restringir','retroativo','retumbante','reverberar','sagacidade','saudosista','sentimento','serenidade','sintetizar','sobrepujar','subestimar','subjacente','subversivo','supremacia','tecnologia','tempestivo','tenacidade','transeunte','transmutar','transviado','ubiquidade','ultrajante','unilateral','urbanidade','usurpadora','vangloriar','veracidade','viabilizar','vislumbrar','vitalidade','voluptuoso','wagneriano','wagnerismo','wagnerista','warrantado','winchester','workaholic','wronskiano','xadrezista','xerocopiar','xerodermia','xerografia','xerostomia','xilografia','xingamento','xiquexique','zarabatana','zendicista','ziguezague','zombeteiro','zoneamento']
        list_11 = ['significado','ambiguidade','animosidade','antagonismo','antagonista','beligerante','benevolente','benignidade','brincadeira','complacente','compreender','comprimento','concernente','consecutivo','contencioso','contingente','contundente','conveniente','convergente','cumprimento','delinquente','descriminar','desenvolver','determinado','dificuldade','discriminar','dispendioso','displicente','dissimulado','enfermidade','estabelecer','excepcional','expectativa','facultativo','fragmentado','frivolidade','fundamental','galanteador','galardoador','generalista','generalizar','grandemente','homossexual','honestidade','hostilidade','identificar','indiferente','integridade','intensidade','jactancioso','jovialidade','kitchenette','longevidade','maravilhoso','menosprezar','mobilizador','necessidade','oportunista','perspectiva','preconceito','pressuposto','pretensioso','proeminente','proveniente','qualificado','qualitativo','quantificar','quebrantado','recrudescer','reivindicar','relativizar','sensacional','subordinado','subsequente','substancial','superficial','supracitado','tendencioso','tergiversar','tradicional','transcender','transcrever','transformar','transgredir','transladado','transpassar','transversal','ultimamente','ultrapassar','unanimidade','uniformizar','univocidade','verborragia','vertiginoso','vicissitude','warrantagem','xenofilismo','xenofobismo','xilogravura','zoomorfismo']
        list_12 = ['caracterizar','circunspecto','compartilhar','complementar','complexidade','concomitante','condicionado','conformidade','conhecimento','constrangido','convencional','cordialidade','cumplicidade','desenvoltura','deslumbrante','enclausurado','entendimento','estabilidade','estigmatizar','extrovertido','fraternidade','generalidade','generalizado','generosidade','genuinamente','gratificante','impertinente','incolumidade','incongruente','independente','ininterrupto','intempestivo','interessante','interlocutor','intermitente','introvertido','juridicidade','legitimidade','liberalidade','libertinagem','longitudinal','mediocridade','naturalidade','negligenciar','nomenclatura','oportunidade','parcialidade','parcialmente','perplexidade','perseverante','prerrogativa','procedimento','procrastinar','proporcionar','proselitismo','protagonista','quantitativo','racionalizar','remanescente','resplandecer','sistematizar','sobremaneira','superestimar','terminologia','trivialidade','ultrapassado','uniformidade','univocamente','urgentemente','utilitarismo','vilipendiado','volatilidade','windsurfista','wollastonita']
        list_13 = ['aprovisionado','arrefecimento','autenticidade','comportamento','consciencioso','conscientizar','consentimento','contentamento','contrapartida','convalescente','correlacionar','credibilidade','desmistificar','discernimento','diversificado','elegibilidade','epistemologia','espalhafatoso','estereotipado','eventualmente','heterossexual','hodiernamente','homogeneidade','incandescente','incondicional','inconsequente','inconsistente','inconveniente','incredulidade','indeterminado','instabilidade','integralmente','interestadual','intransigente','introspectivo','juridicamente','jurisconsulto','jurisdicional','justificativa','keynesianismo','longanimidade','multifacetado','nacionalidade','peculiaridade','perpendicular','personalidade','pormenorizado','possibilidade','precipuamente','preponderante','promiscuidade','provavelmente','quilometragem','quinquilharia','recalcitrante','recenseamento','reciprocidade','remanejamento','ressarcimento','ressentimento','ressignificar','sensibilidade','significativo','singularidade','sobressalente','solidariedade','subjetividade','superestimado','supersticioso','superveniente','transcendente','unidirecional','uniformemente','veementemente']
        list_completa =  list_09 + list_10 + list_11 + list_12 + list_13

    if (nivel == 3):
        list_14 = ['abundantemente','acessibilidade','aleatoriamente','ancestralidade','aplicabilidade','arbitrariedade','arrependimento','atenciosamente','coercitividade','condescendente','constantemente','consubstanciar','contextualizar','credenciamento','demasiadamente','desestabilizar','desprendimento','despretensioso','diligentemente','disponibilizar','dissolutamente','empreendimento','entretenimento','esclarecimento','especificidade','espontaneidade','excentricidade','exclusivamente','exequibilidade','frequentemente','funcionalidade','grandiloquente','hermeticamente','idiossincrasia','imparcialidade','impessoalidade','implicitamente','impressionante','indiscriminado','infraestrutura','insignificante','intermunicipal','jurisdicionado','licenciosidade','minuciosamente','multiplicidade','ocasionalmente','paulatinamente','perecibilidade','perfeccionista','periodicamente','plausibilidade','posteriormente','potencialidade','prestatividade','principalmente','procrastinador','pusilanimidade','questionamento','reciprocamente','reconhecimento','relacionamento','resplandecente','semianalfabeto','sobrecarregado','socioambiental','transcendental','universalidade','weltanschauung']
        list_15 = ['desenvolvimento','encarecidamente','heterogeneidade','hipossuficiente','hipoteticamente','intrinsecamente','respectivamente','simultaneamente','suscetibilidade']
        list_16 = ['responsabilidade']
        list_17 = ['concomitantemente','quantitativamente']
        list_completa =  list_14 + list_15 + list_16 + list_17

    return list_completa


if (__name__ == "__main__"):
    jogar()