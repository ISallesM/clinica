# Listas para armazenar as senhas
senha_comum_n_conveniado = []  # lista para senhas comuns não conveniadas
senha_comum_conveniado = []  # lista para senhas comuns conveniadas
senha_prioritario_n_conveniado = []  # lista para senhas prioritárias não conveniadas
senha_prioritario_conveniado = []  # lista para senhas prioritárias conveniadas
def gerar_senha(idade, conveniado): # Função para gerar a senha com base na idade e se é conveniado ou não
    try:
        if idade >= 65: # Se a idade for maior ou igual a 65, é considerado prioritário
            if conveniado: #
                senha = f"PC1{len(senha_prioritario_conveniado) + 1:02d}" # Gera senha prioritária conveniada
                senha_prioritario_conveniado.append(senha)
            else:
                senha = f"PN2{len(senha_prioritario_n_conveniado) + 1:02d}" # Gera senha prioritária não conveniada
                senha_prioritario_n_conveniado.append(senha)
        else:
            if conveniado:
                senha = f"CC3{len(senha_comum_conveniado) + 1:02d}" # Gera senha comum conveniada
                senha_comum_conveniado.append(senha)
            else:
                senha = f"CN4{len(senha_comum_n_conveniado) + 1:02d}" # Gera senha comum não conveniada
                senha_comum_n_conveniado.append(senha)
        
        return senha
    except Exception as e: # Captura qualquer erro que ocorra durante a geração da senha
        raise ValueError(f"Erro ao gerar senha: {str(e)}") 
    
def remover_senha(): # Função para remover todas as senhas das listas
    print("\n" + "=" * 50)
    print(f"Senhas Prioritárias Conveniadas: ".center(50))
    print("=" * 50)
    while senha_prioritario_conveniado: # Enquanto houver senhas prioritárias conveniadas removemos uma por uma
        elemento_removido = senha_prioritario_conveniado.pop(0) # remove o primeiro elemento da lista
        print(f"Senha removida: {elemento_removido}") # Exibe a senha removida
        print(f"Senhas prioritárias conveniadas após remoção: {senha_prioritario_conveniado}") # Exibe o estado atual da lista após a remoção
    print("\n" + "=" * 50)
    print(f"Senhas Prioritárias Não Conveniadas: ".center(50))  
    print("=" * 50) 
       
    while senha_prioritario_n_conveniado: # Enquanto houver senhas prioritárias não conveniadas removemos uma por uma
        elemento_removido = senha_prioritario_n_conveniado.pop(0) # remove o primeiro elemento da lista
        print(f"Senha removida: {elemento_removido}") # Exibe a senha removida
        print(f"Senhas prioritárias não conveniadas após remoção: {senha_prioritario_n_conveniado}")  # Exibe o estado atual da lista após a remoção
    print("\n" + "=" * 50)
    print(f"Senhas Comuns Conveniadas: ".center(50))    
    print("=" * 50)
    
    while senha_comum_conveniado: # Enquanto houver senhas comuns conveniadas removemos uma por uma
        elemento_removido = senha_comum_conveniado.pop(0) # remove o primeiro elemento da lista
        print(f"Senha removida: {elemento_removido}") # Exibe a senha removida
        print(f"Senhas comuns conveniadas após remoção: {senha_comum_conveniado}")   # Exibe o estado atual da lista após a remoção
    print(f"Senhas Comuns Não Conveniadas: ".center(50))
    print("=" * 50)
    
    while senha_comum_n_conveniado: # Enquanto houver senhas comuns não conveniadas removemos uma por uma
        elemento_removido = senha_comum_n_conveniado.pop(0) # remove o primeiro elemento da lista
        print(f"Senha removida: {elemento_removido}") # Exibe a senha removida
        print(f"Senhas comuns não conveniadas após remoção: {senha_comum_n_conveniado}") # Exibe o estado atual da lista após a remoção
    print("\n" + "=" * 50)
    print("\nTodas as senhas foram removidas com sucesso!")
        

def main(): #Função principal que controla o fluxo do programa
    print("\n" + "=" * 50)
    print("Bem-vindo ao sistema de senhas!".center(50)) # Exibe o título do sistema centralizado
    print("=" * 50)

    while True: # Loop para manter o programa em execução até que o usuário decida sair
        try: # try para capturar erros de entrada
            idade = int(input("Digite sua idade ou digite um número NEGATIVO para sair: ")) # Solicita a idade do usuário
            if idade < 0: # Se a idade for negativa, encerra o programa
                print("Saindo do programa...")
                break
            
            conveniado_input = input("É conveniado? (s/n): ").strip().lower() # Solicita se o usuário é conveniado ou não e normaliza a entrada. strip()
            #remove espaços em branco no início e no final, e lower() converte para minúsculas.
            if conveniado_input not in ['s', 'n']: # Verifica se a entrada é válida
                print("Entrada inválida. Use 's' para conveniado e 'n' para não conveniado.")
                continue
            
            conveniado = conveniado_input == 's' # Converte a entrada para um booleano (True se 's', False se 'n')
            
            senha = gerar_senha(idade, conveniado) # Chama a função para gerar a senha com base na idade e se é conveniado ou não
            print(f"\nSenha gerada: {senha}") # Exibe a senha gerada
            print("\n" + "=" * 50)
            print(f"Senhas prioritárias conveniadas: {senha_prioritario_conveniado}") # Exibe as senhas prioritárias conveniadas
            print(f"Senhas prioritárias não conveniadas: {senha_prioritario_n_conveniado}") # Exibe as senhas prioritárias não conveniadas
            print(f"Senhas comuns conveniadas: {senha_comum_conveniado}")  # Exibe as senhas comuns conveniadas
            print(f"Senhas comuns não conveniadas: {senha_comum_n_conveniado}")  # Exibe as senhas comuns não conveniadas          
            print("=" * 50 + "\n")
            
        except ValueError as e:
            print(f"\n❌ Erro: {e}\n")
        except Exception as e:
            print(f"\n❌ Ocorreu um erro inesperado: {e}\n")
            
    print("Deseja remover todas as senhas? (s/n)") # Pergunta ao usuário se deseja remover todas as senhas
    if input("Digite sua opção: ").strip().lower() == 's': # Se o usuário digitar 's', chama a função para remover as senhas strip() e lower() 
        #são usados para normalizar a entrada
        remover_senha() # Chama a função para remover as senhas
    else:
        print("Nenhuma senha foi removida.") # Informa que nenhuma senha foi removida
        print("\n" + "=" * 50)    
        print("\nObrigado por usar o sistema de senhas!") # Exibe mensagem de agradecimento
        print("Fim do programa!\n")
        print("=" * 50)
if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    main()