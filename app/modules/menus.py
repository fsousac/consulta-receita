""" Menus interativos do programa """


def mainMenu():
    print(
        f"\n{' Bem-vindo! '.center(40, '*')}\n"
        f"\nEscolha uma das opções abaixo:\n"
    )

    option = int(input(
        "(1) Baixar e montar banco de dados\n"
        "(2) Baixar dados da Receita Federal\n"
        "(3) Montar banco de dados SQLite\n"
        "(4) Extrair .CSV de cada estado\n"
        "(5) Extrair dados do CFT\n"
        "(6) Gerar arquivo final .PARQUET com todos os estados\n"
        "(7) Filtrar cnae específico\n"
        "(8) Excluir dados locais\n"
        "(0) Sair\n"
        "Sua resposta: "
    ))
    print("\n" + "".center(40, "*"))
    return option


def confirmMenu(texto_exibido='Confirma?'):
    """
    Exibe menu de confirmação que valida respostas de S/N

        Parameters:
            texto_exibido (str): Pergunta breve

        Returns:
            True or False
    """
    option = input(
        f"\n{texto_exibido} S/N\n"
        "Sua resposta: "
    )
    return True if option.upper() == 'S' else False
