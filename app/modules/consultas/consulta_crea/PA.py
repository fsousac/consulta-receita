from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time


def PA():
    # Configurações do arquivo utilizado
    arquivo = pd.read_csv('app/resources/estados_csv/PA.csv', sep=";")
    arquivo_destino = pd.read_csv('app/resources/sitac_csv/PA.csv', sep=";")
    global hora
    hora = datetime.now()
    hora = hora.strftime("%d/%m/%Y, %H:%M")
    # Configurações da página de pesquisa
    driver = webdriver.Edge()
    driver.get(
        'https://crea-pa.sitac.com.br/app/view/sight/externo?form=PesquisarProfissionalEmpresa')

    # Aguardand resolver o captcha
    while 'Verificação' in driver.page_source:
        time.sleep(2)
    time.sleep(2)

    driver.find_element(By.ID, "PJ").click()
    campo_cnpj = driver.find_element(By.ID, "CNPJ")
    botao_pesquisa = driver.find_element(By.ID, "PESQUISAR")
    colunaCNPJ = list(arquivo['cnpj'])
    colunaSITAC = list(arquivo['sitac_crea'])
    colunaSituacao = list(arquivo['sit_cadastro_crea'])

    def token():
        return driver.execute_script(
            "return document.body.innerText.includes('token')")

    def pesquisa(i):
        """ Realiza uma busca clicando no botão de pesquisa """
        campo_cnpj.clear()
        campo_cnpj.send_keys(colunaCNPJ[i])
        botao_pesquisa.click()

    def carregando():
        """ Verifica se está carregando os resultados da busca """
        return driver.execute_script(
            "return document.body.innerText.includes('Carregando')")

    def reCaptcha():
        """ Verifica se houve erro de reCAPTCHA """
        return driver.execute_script(
            "return document.body.innerText.includes('reCAPTCHA inválido')"
        )

    def resetar_pagina():
        driver.back()
        time.sleep(0.05)
        driver.forward()
        time.sleep(0.1)

    def captura_resultado_pesquisa(i):
        """ Captura o resultado da busca e atualiza na planilha """

        if 'Nada localizado' in driver.page_source:
            print('Nada localizado')
            colunaSITAC[i] = 'Sem registro'
            colunaSituacao[i] = 'Sem registro'
        else:
            situacao = "Situação desconhecida"
            print(situacao)
            colunaSituacao[i] = situacao
            colunaSITAC[i] = 'Registrada no SITAC'

    verifica = ''
    while verifica not in ('S', 'N'):
        verifica = input(
            '\n\n\n\nDeseja pular para o ultimo verificado? (S/N)\n')
        verifica = verifica.upper()

    verifica = verifica == 'S'

    # Executar as buscas percorrendo a planilha
    for i in range(len(arquivo)):

        if colunaSITAC[i] != "Registrada no SITAC":
            if verifica:
                if colunaSITAC[i] in ("Registrada no SITAC", 'Sem registro'):
                    continue
            if i > 0 and i % 100 == 0:
                arquivo_destino['cnpj'] = pd.DataFrame(colunaCNPJ)
                arquivo_destino['sit_cadastro_crea'] = pd.DataFrame(
                    colunaSituacao)
                arquivo_destino['sitac_crea'] = pd.DataFrame(colunaSITAC)
                arquivo['sit_cadastro_crea'] = pd.DataFrame(
                    colunaSituacao)
                arquivo['sitac_crea'] = pd.DataFrame(colunaSITAC)

                arquivo.to_csv(
                    'app/resources/estados_csv/PA.csv', sep=";", index=False)
                arquivo_destino.to_csv(
                    'app/resources/sitac_csv/PA.csv', sep=";", index=False)
            hora = datetime.now()
            hora = hora.strftime("%d/%m/%Y, %H:%M")
            resetar_pagina()
            driver.find_element(By.ID, "PJ").click()
            campo_cnpj = driver.find_element(By.ID, "CNPJ")
            botao_pesquisa = driver.find_element(By.ID, "PESQUISAR")
            pesquisa(i)

            if token():
                print('Token inválido!')
                resetar_pagina()
                pesquisa(i)

            count = 0
            while carregando() or reCaptcha():
                if count > 1000:
                    resetar_pagina()
                    driver.find_element(By.ID, "PJ").click()
                    campo_cnpj = driver.find_element(By.ID, "CNPJ")
                    botao_pesquisa = driver.find_element(By.ID, "PESQUISAR")
                    pesquisa(i)
                    count = 0
                if reCaptcha():
                    print('reCaptcha inválido!')
                    botao_pesquisa.click()
                    time.sleep(0.2)
                else:
                    print('Carregando...')
                    time.sleep(0.2)
                count += 1
            print()
            captura_resultado_pesquisa(i)
            print('*****************************************\n')

    # Gerar novo arquivo com os resultados
    arquivo_destino['cnpj'] = pd.DataFrame(colunaCNPJ)
    arquivo_destino['sit_cadastro_crea'] = pd.DataFrame(colunaSituacao)
    arquivo_destino['sitac_crea'] = pd.DataFrame(colunaSITAC)
    arquivo['sit_cadastro_crea'] = pd.DataFrame(
        colunaSituacao)
    arquivo['sitac_crea'] = pd.DataFrame(colunaSITAC)

    arquivo.to_csv(
        'app/resources/estados_csv/PA.csv', sep=";", index=False)
    arquivo_destino.to_csv(
        'app/resources/sitac_csv/PA.csv', sep=";", index=False)
    driver.quit()


PA()
