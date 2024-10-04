
import time
from colorama import init, Fore
from util import get_pokemon_info, get_pokemon_info_por_url, get_cadeia_evolucao, mostrar_cadeia_evolucao, mostrar_imagem_pokemon

init()


def main():
    #Entrada do usuário
    nome_pokemon = str(input(Fore.GREEN + f'Escolha o Pokémon para ver sua Pokedéx: ' + Fore.BLUE   )).lower()
    pokemon_info = get_pokemon_info(nome_pokemon)

    #URL da espécie para acessar evoluções
    species_url = pokemon_info['species']['url']
    especie_info = get_pokemon_info_por_url(species_url)

    #URL da cadeia de evolução
    evolucao_chain_url = especie_info['evolution_chain']['url']
    evolucao_chain_info = get_cadeia_evolucao(evolucao_chain_url)

    #Tipos e habilidades
    types = [tipo['type']['name'].capitalize() for tipo in pokemon_info['types']]
    abilities_visiveis = [ability['ability']['name'].capitalize() for ability in pokemon_info['abilities'] if not ability['is_hidden']]
    abilities_ocultas = [ability['ability']['name'].capitalize() for ability in pokemon_info['abilities'] if ability['is_hidden']]
    especie = pokemon_info['species']['name'].capitalize()

    #Imagens
    sprite_default = pokemon_info['sprites']['front_default']
    sprite_shiny = pokemon_info['sprites']['front_shiny']

    #Exibir informações do Pokémon
    print(Fore.GREEN + 'ANALISANDO A POKÉDEX...')
    time.sleep(3)
    print(Fore.GREEN + "Nome: ", Fore.BLUE + f'{pokemon_info['name'].capitalize()}')
    print(Fore.GREEN + f'Id: ', Fore.BLUE + f'{pokemon_info['id']}')
    print(Fore.GREEN + f'Altura: ', Fore.BLUE + f'{pokemon_info['height'] / 10:.2f} metros')
    print(Fore.GREEN + f'Peso: ', Fore.BLUE + f'{pokemon_info['weight'] / 10:.2f} kg')
    print(Fore.GREEN + f'Tipos: ', Fore.BLUE + f'{", ".join(types)}')
    print(Fore.GREEN + f'Espécie: ', Fore.BLUE + f'{especie}')

    #Exibir habilidades
    print(Fore.GREEN + f'Habilidades Visíveis: ', Fore.BLUE + f'{", ".join(abilities_visiveis)}')
    if abilities_ocultas:
        print(Fore.GREEN + f'Habilidades Ocultas: ', Fore.BLUE + f'{", ".join(abilities_ocultas)}')
    else:
        print(Fore.GREEN + 'Não há Habilidades Ocultas')
    
    #Exibir cadeia de evolução
    mostrar_cadeia_evolucao(evolucao_chain_info['chain'])

    #Escolher a imagem do Pokémon
    escolha_sprite = input(Fore.GREEN + 'Gostaria de ver qual foto do Pokémon [Normal(1)/Shiny(2)]: ' + Fore.BLUE)
    if escolha_sprite == '1':
        mostrar_imagem_pokemon(sprite_default)
    elif escolha_sprite == '2':
        mostrar_imagem_pokemon(sprite_shiny)
    else:
        print(Fore.RED + 'Escolha Inválida!')

if __name__ == '__main__':
    main()