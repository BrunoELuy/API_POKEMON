import requests
from colorama import Fore
from PIL import Image #Importando para abrir/manipular/exibir imagens
from io import BytesIO #Mexe com os dados binários da imagem, para transofmrar num formato que Pillow entenda

url_base = 'https://pokeapi.co/api/v2/'

def get_pokemon_info(nome):

    #Retorna as informações de im Pokémon a partir do nome dado

    url = f"{url_base}/pokemon/{nome}"
    response = requests.get(url)

    if response.status_code == 200:
        dados_pokemon = response.json()
        #print(dados_pokemon.keys()) -> olhar as chaves principais
        return dados_pokemon
    else:
        print(Fore.RED + f'Ocorreu uma falha ao receber os dados {response.status_code}')
        exit()

def get_pokemon_info_por_url(url):

    ##Retorna as informações de im Pokémon a partir de uma URL

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(Fore.RED + f'Erro ao acessar URL: {response.status_code}')
        exit()

def get_cadeia_evolucao(evolution_url):

    #Retorna as informações da cadeia evolutiva do Pokémon

    response = requests.get(evolution_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(Fore.RED + f'Erro ao acessar cadeia evolutiva: {response.status_code}')

def mostrar_cadeia_evolucao(chain):

    #Mostra a cadeia de evolução do Pokémon organizada

    evolucao_atual = chain['species']['name']
    evolucao = [evolucao_atual.capitalize()]
    while 'evolves_to' in chain and len(chain['evolves_to']) > 0:
        chain = chain['evolves_to'][0]
        proxima_evolucao = chain['species']['name']
        evolucao.append(proxima_evolucao.capitalize())
    print(Fore.GREEN + f"Evoluções: ", Fore.BLUE + f"{' -> '.join(evolucao)}")

def mostrar_imagem_pokemon(url):

    #Mostra a Imagem do Pokémon a partir da URL do sprite

    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content)) #content transforma em Bytes / BytesIO transforma em Bytes que Pillow entende
        img.show()
    else:
        print(Fore.RED + f'Ocorreu uma falha ao receber os dados {response.status_code}')
        exit()