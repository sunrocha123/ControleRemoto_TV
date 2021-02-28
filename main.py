class Televisao(object):

    canal_atual = 0
    volume_atual_som = 0

    pass

class ControleRemoto(object):
    
    caminho_tv = Televisao()

    def diminuir_volume_som(self, potencia_volume):
        if (self.caminho_tv.volume_atual_som - potencia_volume) >= 0:
            print('Volume sendo diminuído...\n')
            for i in range(self.caminho_tv.volume_atual_som, self.caminho_tv.volume_atual_som - potencia_volume, -1):
                print('|', end="")
            print('\n\nVolume do som diminuído, conforme solicitado :)\n')
            self.caminho_tv.volume_atual_som -= potencia_volume
        else:
            print('O valor informado menos o volume atual é inferior a 0. Por gentileza, digite um valor válido!\n')

    def aumentar_volume_som(self, potencia_volume):
        if (self.caminho_tv.volume_atual_som + potencia_volume) <= 100:
            print('Volume sendo aumentado...\n')
            for i in range(self.caminho_tv.volume_atual_som, self.caminho_tv.volume_atual_som + potencia_volume, 1):
                print('|', end = "")
            print('\n\nVolume do som aumentado, conforme solicitado :)\n')
            self.caminho_tv.volume_atual_som += potencia_volume
        else:
            print('O valor informado mais o volume atual é maior que 100. Por gentileza, digite um valor válido!\n')

    def trocar_canal(self, canal):
        novo_canal = self.caminho_tv.canal_atual = canal
        print(f'Canal trocado para {novo_canal}, conforme solicitado :)\n')
        pass

    def consultar_som_canal(self):
        print(f'Canal atual: {self.caminho_tv.canal_atual}\n'
              f'Volume atual do som: {self.caminho_tv.volume_atual_som}\n')
        pass

    pass

if __name__ == '__main__':

    def menu():
        print(f'MENU\n'
              f'1. Aumentar volume do som\n'
              f'2. Diminuir volume do som\n'
              f'3. Trocar de canal\n'
              f'4. Consultar canal e volume do som atual\n'
              f'5. Sair\n')

    print(f'--------------------\n'
          f'CONTROLE REMOTO\n'
          f'--------------------\n'
          f'Bem-vindo a nossa ferramenta de controle remoto :)\n')

    objeto_controleRemoto = ControleRemoto()

    while True:
        menu()

        while True:
            escolha_opcao = int(input('Digite uma opção (1 - 5): '))
            if int(escolha_opcao) <= 0 or int(escolha_opcao) > 5:
                print('Opção inválida! Por gentileza, digite novamente.')
            else:
                print()
                break

        if escolha_opcao == 1:
            aumentar_volume = int(input('Digite quanto deseja aumentar: '))
            objeto_controleRemoto.aumentar_volume_som(aumentar_volume)
            pass
        elif escolha_opcao == 2:
            diminuir_volume = int(input('Digite quanto deseja diminuir: '))
            objeto_controleRemoto.diminuir_volume_som(diminuir_volume)         
            pass
        elif escolha_opcao == 3:
            novo_canal = int(input('Digite o novo canal: '))
            objeto_controleRemoto.trocar_canal(novo_canal)
            pass
        elif escolha_opcao == 4:
            objeto_controleRemoto.consultar_som_canal()
            pass
        else:
            print('Obrigado por usar nossa ferramenta!!!! :)')
            break

        while True:
            validar_uso = input('Deseja realizar outra operação (S/N)? ').title().strip()
            if validar_uso != 'S' and validar_uso != 'Sim' and validar_uso != 'N' and validar_uso != 'Não' and validar_uso != 'Nao':
                print('Opção inválida! Por gentileza, digite novamente')
            else:
                break

        if validar_uso == 'N' or validar_uso == 'Não' or validar_uso == 'Nao':
            print('Obrigado por usar nossa ferramenta!!!! :)')
            break
        print()   