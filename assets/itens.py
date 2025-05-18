# File made by: Davi

from assets.things import Char

class Itens:
    tavern = [
        {"nome": "Pocao de Vida", "preco": 5},
        {"nome": "Pocao de Ataque", "preco": 3},
    ]

    blacksmith = [
        {"nome": "Espada de Madeira", "preco": 5, "dano": 0.3},
        {"nome": "Espada de Prata", "preco": 10, "dano": 1.0},
        {"nome": "Espada de Ouro", "preco": 20, "dano": 2.0},
        {"nome": "Espada de Platina", "preco": 40, "dano": 3.0},
        {"nome": "Espada de Diamante", "preco": 60, "dano": 4.5},
    ]

    base_itens = {
    "Espada": {
        "tipo": "arma",
        "dano": 10,
        "peso": 5,
        "utilizavel": False,
        "fundivel": True
    },
    "Pocao de cura": {
        "tipo": "consumível",
        "cura": 20,
        "utilizavel": True,
        "fundivel": True
    },
    "Pocao de mana": {
        "tipo": "consumível",
        "mana": 20,
        "utilizavel": True,
        "fundivel": True
    },
    "Pocao de forca": {
        "tipo": "consumível",
        "forca": 0.3,
        "utilizavel": True,
        "fundivel": True
    },
    }

    materials = {
    "Bola de slime": {
        "tipo": "material",
        "propriedades": ["pegajoso", "maleável"],
        "utilizavel": False,
        "fundivel": True
    },
    "Essencia de fogo": {
        "tipo": "material",
        "propriedades": ["inflamável", "energético"],
        "utilizavel": False,
        "fundivel": True
    },
    "Escama de dragao": {
        "tipo": "material",
        "propriedades": ["resistente", "rígido", "mágico"],
        "utilizavel": False,
        "fundivel": True
    },
    "Garra de lobo": {
        "tipo": "material",
        "propriedades": ["afiada", "leve", "letal"],
        "utilizavel": False,
        "fundivel": True
    },
    "Pluma de fenix": {
        "tipo": "material",
        "propriedades": ["leve", "místico", "regenerativo"],
        "utilizavel": False,
        "fundivel": True
    },
    }

    Itens_personalizados = {
    # Espadas personalizadas
    "Espada de Madeira Pegajosa": {
        "tipo": "arma",
        "dano": 0.5,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Madeira Inflamavel": {
        "tipo": "arma",
        "dano": 0.6,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Madeira Resistente": {
        "tipo": "arma",
        "dano": 0.8,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Madeira Afiada": {
        "tipo": "arma",
        "dano": 1.0,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Madeira Magica": {
        "tipo": "arma",
        "dano": 1.3,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Prata Pegajosa": {
        "tipo": "arma",
        "dano": 1.5,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Prata Inflamavel": {
        "tipo": "arma",
        "dano": 1.8,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Prata Resistente": {
        "tipo": "arma",
        "dano": 2.0,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Prata Afiada": {
        "tipo": "arma",
        "dano": 2.3,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Prata Magica": {
        "tipo": "arma",
        "dano": 2.5,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Ouro Pegajosa": {
        "tipo": "arma",
        "dano": 2.8,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Ouro Inflamavel": {
        "tipo": "arma",
        "dano": 3.0,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Ouro Resistente": {
        "tipo": "arma",
        "dano": 3.2,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Ouro Afiada": {
        "tipo": "arma",
        "dano": 3.4,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Ouro Magica": {
        "tipo": "arma",
        "dano": 3.5,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Platina Pegajosa": {
        "tipo": "arma",
        "dano": 3.7,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Platina Inflamavel": {
        "tipo": "arma",
        "dano": 3.8,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Platina Resistente": {
        "tipo": "arma",
        "dano": 4.0,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Platina Afiada": {
        "tipo": "arma",
        "dano": 4.2,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Platina Magica": {
        "tipo": "arma",
        "dano": 4.5,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Diamante Pegajosa": {
        "tipo": "arma",
        "dano": 4.8,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Diamante Inflamavel": {
        "tipo": "arma",
        "dano": 5.0,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Diamante Resistente": {
        "tipo": "arma",
        "dano": 5.2,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Diamante Afiada": {
        "tipo": "arma",
        "dano": 5.4,
        "utilizavel": False,
        "fundivel": False
    },
    "Espada de Diamante Magica": {
        "tipo": "arma",
        "dano": 5.5,
        "utilizavel": False,
        "fundivel": False
    },

    # Poções de cura personalizadas
    "Pocao Pegajosa de Cura": {
        "tipo": "consumivel",
        "cura": 25,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao Ardente de Cura": {
        "tipo": "consumivel",
        "cura": 30,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao Resistente de Cura": {
        "tipo": "consumivel",
        "cura": 35,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao Cortante de Cura": {
        "tipo": "consumivel",
        "cura": 40,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao Magica Regenerativa": {
        "tipo": "consumivel",
        "cura": 50,
        "utilizavel": True,
        "fundivel": False
    },

    # Poções de mana personalizadas
    "Pocao Pegajosa de Mana": {
        "tipo": "consumivel",
        "mana": 25,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao Energizante de Mana": {
        "tipo": "consumivel",
        "mana": 30,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao Encantada de Mana": {
        "tipo": "consumivel",
        "mana": 40,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao Aguçada de Mana": {
        "tipo": "consumivel",
        "mana": 50,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao de Mana Mistica": {
        "tipo": "consumivel",
        "mana": 60,
        "utilizavel": True,
        "fundivel": False
    },

    # Poções de força personalizadas
    "Pocao Flexivel de Forca": {
        "tipo": "consumivel",
        "forca": 0.7,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao de Forca Ardente": {
        "tipo": "consumivel",
        "forca": 1,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao de Forca Escamada": {
        "tipo": "consumivel",
        "forca": 1.3,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao de Forca Selvagem": {
        "tipo": "consumivel",
        "forca": 1.5,
        "utilizavel": True,
        "fundivel": False
    },
    "Pocao de Forca Renascente": {
        "tipo": "consumivel",
        "forca": 2,
        "utilizavel": True,
        "fundivel": False
    },
}




class Village:
    village_names = [
    "Eldoria", "Brumária", "Ventogard", "Skaldenheim", "Ravenspire",
    "Calthera", "Thornwick", "Montavela", "Dornbridge", "Luzern"
    ]

class Flashback:
    flashbacks = [
        # PRESENTE
        "Aton na praia sente o desconforto no ar. Há algo errado, mesmo num lugar tão pacífico.",
        "Enquanto treina com soldados, um deles comenta baixinho: 'Esse é o tal de Skalice... ouvi dizer que matou o próprio comandante.'",
        "Durante a primeira noite na taverna, Aton acorda suando frio — não por um pesadelo, mas por não ter sonhado com nada.",
        "Um garoto se aproxima e pergunta se Aton já matou alguém. Aton apenas abaixa os olhos e finge não ouvir.",
        "Enquanto caminha pelas ruas de Eldoria, percebe olhares. Alguns o admiram, outros o evitam. Ele já está marcado ali.",
        "Na primeira batalha de treino, Aton segura o golpe no último instante. Algo dentro dele hesitou — e ele não sabe por quê.",
        "Durante o jantar com os fazendeiros, ouve histórias sobre paz. Ele tenta sorrir, mas sente que está em um mundo que não entende mais.",
        "Ao observar as montanhas distantes, Aton sussurra: 'Será que algum dia volto pra casa?'. Ninguém responde.",

        # PASSADO
        "Skalice em chamas. Gritos, fumaça, o aço contra o aço. Aton tenta proteger os civis, mas chega tarde demais.",
        "O jovem aprendiz cai durante um treino. Aton, impaciente, ignora seu pedido de ajuda. Dias depois, o menino está morto.",
        "Um salão escuro. Nobres de Skalice cochicham sobre alianças com mercenários. Aton escuta — e escolhe o silêncio.",
        "A neve cobre um campo de batalha. Aton segura um corpo sem vida: era seu companheiro mais antigo.",
        "A mulher de cabelos castanhos entrega a ele um colar. 'Se for, não volte sem alma.' Ele parte mesmo assim.",
        "Aton desperta coberto de sangue. Ele mesmo matou um prisioneiro que implorava por perdão. Não foi justiça. Foi raiva.",
        "Chamas cercam a vila. Aton carrega uma criança ferida enquanto vozes gritam seu nome.",
        "Durante o treinamento, um companheiro chora. Aton o manda calar. Depois, descobre que o rapaz perdeu toda a família.",

        # FUTURO
        "Diante de um trono vazio, Aton hesita. Um dia, ele sentará ali. Mas com quais sacrifícios?",
        "Uma voz de criança ecoa: 'Papai, você voltou?' Aton olha em volta. Ele não tem filhos. Ainda.",
        "No reflexo de sua espada, vê-se mais velho, cansado, cercado por túmulos. Todos nomes que ele não conseguiu salvar.",
        "Caminhando pela feira de Vargrid, ouve gritos. É uma revolta. No meio da multidão, alguém grita: 'Aton traiu Skalice!'",
        "Durante um sonho, acorda em uma cela. Guardas o observam com medo. Um aviso ecoa: 'O futuro não te perdoa.'",
        "Diante do espelho d água em Várdann, vê a si mesmo como rei. Atrás, seu reino queimava.",
        "Aton caminha por um campo destruído — reconhece a armadura no chão. Era sua. Mas ele nunca esteve ali... ainda.",
        "Em uma fortaleza distante, alguém lê um livro. Na capa: 'Crônicas do Redentor de Skalice'. Mas Aton nunca escreveu isso."
    ]
