from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time


def RS():
    # Configurações do arquivo utilizado
    arquivo = pd.read_csv('app/resources/estados_csv/RS.csv', sep=";")
    arquivo_destino = pd.DataFrame()
    #arquivo_final.to_csv('app/resources/sitac_csv/AC.csv', sep=";")
    # Configurações da página de pesquisa
    driver = webdriver.Edge()
    driver.get(
        'https://apolo.crea-rs.org.br:8443/apoloaplsrv01/servlet/org.crears.apolo.prod.hsel_empresa_consulta_site')

    # Aguardand resolver o captcha
    if 'Verificação' in driver.page_source:
        input("Por favor, resolva o reCAPTCHA manualmente. Pressione Enter quando terminar.")
        time.sleep(10) 

    #driver.find_element(By.ID, "PJ").click()
    campo_cnpj = driver.find_element(By.ID, "_EMP_NROCPJ")
    botao_pesquisa = driver.find_element(By.NAME, "BUTTON1")
    colunaCNPJ = list(arquivo['cnpj'])
    colunaSITAC = list(arquivo['sitac_crea'])
    colunaSituacao = list(arquivo['sit_cadastro_crea'])
    # colunaSITAC = list(arquivo_destino['sitac_crea'])
    # colunaSituacao = list(arquivo_destino['sit_cadastro_crea'])

    def pesquisa(i):
        """ Realiza uma busca clicando no botão de pesquisa """
        campo_cnpj.clear()
        campo_cnpj.send_keys(arquivo['cnpj'][i])
        botao_pesquisa.click()

    def carregando():
        """ Verifica se está carregando os resultados da busca """
        return driver.execute_script(
            "return document.body.innerText.includes('Carregando')")

    '''def reCaptcha():
        """ Verifica se houve erro de reCAPTCHA """
        return driver.execute_script(
            "return document.body.innerText.includes('reCAPTCHA inválido')"
        )

    def resetar_pagina():
        driver.back()
        time.sleep(0.05)
        driver.forward()
        time.sleep(0.1)'''

    def captura_resultado_pesquisa(i):
        """ Captura o resultado da busca e atualiza na planilha """
        while carregando() == True:
             print('Carregando...')
             time.sleep(0.2)

        if not 'Para ver dados da empresa clique no número do Registro' in driver.page_source:
            print('Nada localizado')
            colunaSITAC[i] = 'Sem registro'
            colunaSituacao[i] = 'Sem registro'
        else:
            time.sleep(0.5)
            driver.find_element(By.ID, "span_EMP_NROREG_0001").click
            situacao = driver.find_element(
                By.ID, "span_EMP").text
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

        if arquivo['sitac_crea'][i] != "Registrada no SITAC":
            if verifica:
                if colunaSITAC[i] in ("Registrada no SITAC", 'Sem registro'):
                    continue
            if i > 0 and i % 100 == 0:
                arquivo_destino['cnpj'] = pd.DataFrame(colunaCNPJ)
                arquivo_destino['sit_cadastro_crea'] = pd.DataFrame(
                    colunaSituacao)
                arquivo_destino['sitac_crea'] = pd.DataFrame(colunaSITAC)
                arquivo_destino.to_csv(
                    'app/resources/sitac_csv/RS.csv', sep=";", index=False)
            #resetar_pagina()
            #driver.find_element(By.ID, "PJ").click()
            campo_cnpj = driver.find_element(By.ID, "_EMP_NROCPJ")
            botao_pesquisa = driver.find_element(By.NAME, "BUTTON1")
            pesquisa(i)

            '''while carregando() or reCaptcha():
                if reCaptcha():
                    print('reCaptcha inválido!')
                    botao_pesquisa.click()
                    time.sleep(0.2)
                else:
                    print('Carregando...')
                    time.sleep(0.2)'''

            captura_resultado_pesquisa(i)
            print('***************************************** \n')

    # Gerar novo arquivo com os resultados
    arquivo_destino = arquivo_destino.drop(columns=['cnpj'])
    arquivo = arquivo.drop(columns=['sitac_crea', 'sit_cadastro_crea'])
    arquivo_final = pd.concat([arquivo, arquivo_destino], axis=1)
    '''arquivo_destino['cnpj'] = pd.DataFrame(colunaCNPJ)
    arquivo_destino['sit_cadastro_crea'] = pd.DataFrame(colunaSituacao)
    arquivo_destino['sitac_crea'] = pd.DataFrame(colunaSITAC)'''
    arquivo_final.to_csv(
        'app/resources/sitac_csv/RS.csv', sep=";", index=False)
    print("\nConsulta Finalizada!")
    driver.quit()


RS()